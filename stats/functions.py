import pandas as pd
from pandas.core.dtypes.common import is_numeric_dtype


def _avg(df: pd.DataFrame, args, grouped_by, named_as=None):
    if len(args) > 1:
        raise ValueError(f'avg function may have only 1 argument, we have got {len(args)}: {args}.')
    if len(grouped_by) > 0:
        raise ValueError(f'avg function does not support using [grouped_by] option.')
    column_name = args[0]
    if not is_numeric_dtype(df[column_name]):
        raise ValueError(f'avg function support only numeric values in columns.')
    named_as = column_name if named_as is None else named_as
    result = df[column_name].mean()
    return pd.DataFrame([[result]], columns=[named_as])


FUNCTIONS = {
    'avg': _avg
}


def generate(dataframe, name, **params):
    fn = FUNCTIONS[name]
    return fn(dataframe, **params)
