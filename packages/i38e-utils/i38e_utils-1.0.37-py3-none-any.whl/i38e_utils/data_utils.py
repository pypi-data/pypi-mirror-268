#  Copyright (c) 2023. ISTMO Center S.A.  All Rights Reserved
#

import datetime
import os
import time
from typing import Any, Dict, Type
import pandas as pd

from .df_utils import add_df_totals

from .log_utils import Logger

logger = Logger(log_dir='./logs/', logger_name=__name__, log_file=f'{__name__}.log')


def convert_value_pairs(row):
    if row['value_type'] == "datetime":
        converted_value = datetime.datetime.strptime(row['value'], '%Y-%m-%d %H:%M:%S')
    elif row['value_type'] == 'str':
        converted_value = row['value']
    else:
        converted_value = eval(f"{row['value_type']}({row['value']})")
    return converted_value


def get_timeseries_params(df_params) -> Any:
    index_col = None
    ts_params = df_params
    if ts_params.get("datetime_index", False):
        index_col = ts_params.get('index_col', None)
        pop_cols = ['datetime_index', 'index_col']
        for p in pop_cols:
            ts_params.pop(p, None)
    return index_col, ts_params


def format_fields(df, format_options):
    for fld_name, fld_type in format_options.items():
        if fld_name in df.columns:
            df[fld_name] = df[fld_name].values.astype(fld_type)
    return df


def fillna_fields(df, fill_options):
    for fld_name, fill_value in fill_options.items():
        if fld_name in df.columns:
            df.fillna({fld_name: fill_value}, inplace=True)
    return df


def cast_cols_as_categories(df, threshold=100):
    for col in df.columns:
        if df[col].dtype in ['object', 'string'] and len(df[col].unique()) < threshold:
            df[col] = df[col].astype(pd.CategoricalDtype())
    return df


def load_as_timeseries(df, **options):
    index_col = options.get("index_col", None)
    if index_col is not None and df.index.name != index_col:
        if index_col in df.columns:
            df.reset_index(inplace=True)
            df.set_index(index_col, inplace=True)
    rule = options.pop("rule", "D")
    index = options.pop("index", df.index)
    cols = options.pop("cols", None)
    vals = options.pop("vals", None)
    totals = options.pop("totals", False)
    agg_func = options.pop("agg_func", 'count')
    df = df.pivot_table(index=index, columns=cols, values=vals, aggfunc=agg_func).fillna(0)
    df = df.resample(rule=rule).sum()
    df.sort_index(inplace=True)
    if totals:
        df = add_df_totals(df)
    return df


def fix_fields(df, fields_to_fix, field_type):
    field_attributes = {
        'str': {'default_value': '', 'dtype': str},
        'int': {'default_value': 0, 'dtype': int},
        'date': {'default_value': pd.NaT, 'dtype': 'datetime64[ns]'},
        'datetime': {'default_value': pd.NaT, 'dtype': 'datetime64[ns]'}
    }

    if field_type not in field_attributes:
        raise ValueError("Invalid field type: {}".format(field_type))

    attr = field_attributes[field_type]
    fields = [field for field in fields_to_fix if field in df.columns]
    df[fields] = df[fields].fillna(attr['default_value']).astype(attr['dtype'])


def merge_lookup_data(classname, df, **kwargs):
    """
    kwargs={
        'source_col':'marital_status_id',
        'lookup_description_col':'description',
        'lookup_col':'id',
        'source_description_alias':'marital_status_description',
        'fillna_source_description_alias': True
    }
    :param classname:
    :param df:
    :param kwargs:
    :return:
    """
    if df.empty:
        return df
    source_col = kwargs.pop('source_col', None)
    lookup_col = kwargs.pop('lookup_col', None)
    lookup_description_col = kwargs.pop('lookup_description_col', None)
    source_description_alias = kwargs.pop('source_description_alias', None)
    fillna_source_description_alias = kwargs.pop('fillna_source_description_alias', False)
    fieldnames = kwargs.get('fieldnames', None)
    column_names = kwargs.get('column_names', None)

    if source_col is None or lookup_description_col is None or source_description_alias is None or lookup_col is None:
        raise ValueError(
            'source_col, lookup_col, lookup_description_col and source_description_alias must be specified')
    if source_col not in df.columns:
        # raise ValueError(f'{source_col} not in dataframe columns')
        return df
    ids = list(df[source_col].dropna().unique())
    if not ids:
        return df
    if fieldnames is None:
        kwargs['fieldnames'] = (lookup_col, lookup_description_col)
    if column_names is None:
        kwargs['column_names'] = ['temp_join_col', source_description_alias]
    kwargs[f'{lookup_col}__in'] = ids
    result = classname(live=True).load(**kwargs)
    if 'temp_join_col' in kwargs.get("column_names"):
        temp_join_col = 'temp_join_col'
    else:
        temp_join_col = lookup_col

    df = df.merge(result, how='left', left_on=source_col, right_on=temp_join_col)
    if fillna_source_description_alias:
        if source_description_alias in df.columns:
            df.fillna({source_description_alias: ''}, inplace=True)
    if 'temp_join_col' in df.columns:
        df.drop(columns='temp_join_col', inplace=True)
    return df


class DataWrapper:
    DEFAULT_MAX_AGE_MINUTES = 1440
    DEFAULT_HISTORY_DAYS_THRESHOLD = 30

    def __init__(self, dataclass: Type, date_field: str, data_path: str, parquet_filename: str,
                 start_date: Any, end_date: Any, verbose: bool = False, load_params: Dict = None,
                 reverse_order: bool = False, overwrite: bool = False,
                 max_age_minutes: int = DEFAULT_MAX_AGE_MINUTES,
                 history_days_threshold: int = DEFAULT_HISTORY_DAYS_THRESHOLD):
        self.dataclass = dataclass
        self.date_field = date_field
        self.data_path = self.ensure_forward_slash(data_path)
        self.parquet_filename = parquet_filename
        self.verbose = verbose
        self.load_params = load_params or {}
        self.reverse_order = reverse_order
        self.overwrite = overwrite
        self.max_age_minutes = max_age_minutes
        self.history_days_threshold = history_days_threshold

        self.start_date = self.convert_to_date(start_date)
        self.end_date = self.convert_to_date(end_date)
        self.remove_empty_directories(self.data_path)

    @staticmethod
    def convert_to_date(date: Any) -> datetime.date:
        try:
            return datetime.datetime.strptime(date, '%Y-%m-%d').date() if isinstance(date, str) else date
        except ValueError as e:
            logger.error(f"Error converting {date} to datetime: {e}")
            raise

    @staticmethod
    def ensure_forward_slash(path: str) -> str:
        return path if path.endswith('/') else path + '/'

    @staticmethod
    def ensure_directory_exists(path: str):
        try:
            os.makedirs(path, exist_ok=True)
        except OSError as e:
            logger.error(f"Error creating directory {path}: {e}")
            raise

    def generate_date_range(self):
        step = -1 if self.reverse_order else 1
        start, end = (self.end_date, self.start_date) if self.reverse_order else (self.start_date, self.end_date)
        current_date = start
        while current_date != end + datetime.timedelta(days=step):
            yield current_date
            current_date += datetime.timedelta(days=step)

    def process(self):
        for current_date in self.generate_date_range():
            self.process_date(current_date)

    def is_file_older_than(self, file_path: str, current_date: datetime.date) -> bool:
        if not os.path.exists(file_path):
            return True

        file_modification_date = datetime.date.fromtimestamp(os.path.getmtime(file_path))
        file_age_days = (datetime.date.today() - file_modification_date).days

        if self.overwrite:
            return True

        if file_age_days <= self.history_days_threshold:
            file_age_seconds = time.time() - os.path.getmtime(file_path)
            if self.verbose:
                logger.info(f"File {file_path} is {round((file_age_seconds / 60), 0)} minutes old")
            return file_age_seconds / 60 > self.max_age_minutes or self.max_age_minutes == 0

        return False

    def process_date(self, date: datetime.date):
        folder = f'{self.data_path}{date.year}/{date.month:02d}/{date.day:02d}/'
        full_parquet_filename = os.path.join(folder, self.parquet_filename)

        start_time = time.time()  # Start timing before processing

        if self.verbose:
            logger.info(f"Processing {full_parquet_filename}...")

        today = datetime.date.today()
        days_difference = (today - date).days

        if days_difference > self.history_days_threshold and not self.overwrite:
            if os.path.exists(full_parquet_filename):
                if self.verbose:
                    logger.info(f"File exists and date is beyond history days threshold without overwrite. Skipping.")
                return
            else:
                if self.verbose:
                    logger.info(
                        f"File does not exist for date beyond history days threshold. Proceeding with generation.")

        if not self.is_file_older_than(full_parquet_filename, date):
            if self.verbose:
                logger.info("File exists and conditions for regeneration are not met. Skipping.")
            return

        data_object = self.dataclass(live=True)
        date_filter_params = {f'{self.date_field}__year': date.year, f'{self.date_field}__month': date.month,
                              f'{self.date_field}__day': date.day}
        df = data_object.load(**self.load_params, **date_filter_params)

        if df.empty:
            if self.verbose:
                logger.info("No data found for the specified date.")
            return

        # Create directory structure only if df is not empty
        self.ensure_directory_exists(folder)
        df.to_parquet(full_parquet_filename)

        end_time = time.time()  # End timing after processing
        duration_seconds = end_time - start_time  # Calculate duration

        if self.verbose:
            logger.info(f"Data saved to {full_parquet_filename}. Processing time: {duration_seconds:.2f} seconds")
        self.remove_empty_directories(os.path.dirname(folder))
    def remove_empty_directories(self, path: str):
        if not os.path.isdir(path) or os.path.realpath(path) == os.path.realpath(self.data_path):
            return

        if not os.listdir(path):
            try:
                os.rmdir(path)
                if self.verbose:
                    logger.info(f"Removed empty directory: {path}")
                self.remove_empty_directories(os.path.dirname(path))
            except OSError as e:
                if self.verbose:
                    logger.error(f"Error removing directory {path}: {e}")
        else:
            if self.verbose:
                logger.info(f"Directory not empty, stopping: {path}")

# Usage:
# wrapper = DataWrapper(dataclass=YourDataClass, date_field="created_at", data_path="/path/to/data", parquet_filename="data.parquet", start_date="2022-01-01", end_date="2022-12-31")
# wrapper.process()
