import pandas
import pandas as pd
from pandas.core.dtypes.common import is_numeric_dtype


def _avg(df: pd.DataFrame, args, grouped_by, named_as=None):
    # error checks
    if len(args) > 1:
        raise ValueError(f'avg function may have only 1 argument, we have got {len(args)}: {args}.')
    if len(grouped_by) > 0:
        raise ValueError(f'avg function does not support using [grouped_by] option.')
    column_name = args[0]
    if not is_numeric_dtype(df[column_name]):
        raise ValueError(f'avg function support only numeric values in columns.')
    # calculation
    named_as = column_name if named_as is None else named_as
    result = df[column_name].mean()
    # done
    return pd.DataFrame([[result]], columns=[named_as])


def _count(df: pd.DataFrame, args, grouped_by, named_as=None):
    # error checks
    if len(args) > 1:
        raise ValueError(f'avg function may have only 1 argument, we have got {len(args)}: {args}.')
    if len(grouped_by) > 1:
        raise ValueError(f'avg function may be grouped only by 1 name, got {len(grouped_by)}: {grouped_by}')
    # calculation
    named_as = "count" if named_as is None else named_as
    column_name = args[0]
    if len(grouped_by) == 0:
        result = df[column_name].count()
        result = pd.DataFrame([[result]], columns=[named_as])
    else:
        group_by_name = grouped_by[0]
        result = df.value_counts(df[group_by_name]).to_frame(name=named_as)
    # done
    return result


FUNCTIONS = {
    'avg': _avg,
    'count': _count
}


def generate(dataframe, name, **params):
    fn = FUNCTIONS[name]
    return fn(dataframe, **params)
