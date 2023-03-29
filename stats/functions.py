import pandas as pd
from pandas.core.dtypes.common import is_numeric_dtype


def _avg(df: pd.DataFrame, args, grouped_by, named_as=None) -> pd.DataFrame:
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


def _count(df: pd.DataFrame, args, grouped_by, named_as=None) -> pd.DataFrame:
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


def _distinct_count(df: pd.DataFrame, args, grouped_by, named_as=None) -> pd.DataFrame:
    ...


def _min(df: pd.DataFrame, args, grouped_by, named_as=None) -> pd.DataFrame:
    # error checks
    if len(args) > 1:
        raise ValueError(f'min function may have only 1 argument, we have got {len(args)}: {args}.')
    if len(grouped_by) > 0:
        raise ValueError(f'min function can not be grouped, got {len(grouped_by)}: {grouped_by}')
    # calculation
    named_as = "min" if named_as is None else named_as
    result = df[args[0]].min()
    result = pd.DataFrame([[result]], columns=[named_as])
    # done
    return result


def _max(df: pd.DataFrame, args, grouped_by, named_as=None) -> pd.DataFrame:
    # error checks
    if len(args) > 1:
        raise ValueError(f'max function may have only 1 argument, we have got {len(args)}: {args}.')
    if len(grouped_by) > 0:
        raise ValueError(f'max function can not be grouped, got {len(grouped_by)}: {grouped_by}')
    # calculation
    named_as = "max" if named_as is None else named_as
    result = df[args[0]].max()
    result = pd.DataFrame([[result]], columns=[named_as])
    # done
    return result


def _stddev(df: pd.DataFrame, args, grouped_by, named_as=None) -> pd.DataFrame:
    # error checks
    if len(args) > 1:
        raise ValueError(f'stddev function may have only 1 argument, we have got {len(args)}: {args}.')
    if len(grouped_by) > 0:
        raise ValueError(f'stddev function can not be grouped, got {len(grouped_by)}: {grouped_by}')
    # calculation
    named_as = "stddev" if named_as is None else named_as
    result = df[args[0]].std()
    result = pd.DataFrame([[result]], columns=[named_as])
    # done
    return result


def _sum(df: pd.DataFrame, args, grouped_by, named_as=None) -> pd.DataFrame:
    # error checks
    if len(args) > 1:
        raise ValueError(f'sum function may have only 1 argument, we have got {len(args)}: {args}.')
    if len(grouped_by) > 0:
        raise ValueError(f'sum function can not be grouped, got {len(grouped_by)}: {grouped_by}')
    # calculation
    named_as = "sum" if named_as is None else named_as
    result = df[args[0]].sum()
    result = pd.DataFrame([[result]], columns=[named_as])
    # done
    return result


def _var(df: pd.DataFrame, args, grouped_by, named_as=None) -> pd.DataFrame:
    # error checks
    if len(args) > 1:
        raise ValueError(f'var function may have only 1 argument, we have got {len(args)}: {args}.')
    if len(grouped_by) > 0:
        raise ValueError(f'var function can not be grouped, got {len(grouped_by)}: {grouped_by}')
    # calculation
    named_as = "var" if named_as is None else named_as
    result = df[args[0]].var()
    result = pd.DataFrame([[result]], columns=[named_as])
    # done
    return result


def _first(df: pd.DataFrame, args, grouped_by, named_as=None) -> pd.DataFrame:
    # error checks
    if len(args) > 1:
        raise ValueError(f'first function may have only 1 argument, we have got {len(args)}: {args}.')
    if len(grouped_by) > 0:
        raise ValueError(f'first function can not be grouped, got {len(grouped_by)}: {grouped_by}')
    # calculation
    named_as = "first" if named_as is None else named_as
    result = df[args[0]][0]
    result = pd.DataFrame([[result]], columns=[named_as])
    # done
    return result


def _last(df: pd.DataFrame, args, grouped_by, named_as=None) -> pd.DataFrame:
    # error checks
    if len(args) > 1:
        raise ValueError(f'last function may have only 1 argument, we have got {len(args)}: {args}.')
    if len(grouped_by) > 0:
        raise ValueError(f'last function can not be grouped, got {len(grouped_by)}: {grouped_by}')
    # calculation
    named_as = "last" if named_as is None else named_as
    result = df[args[0]][df[args[0]].count() - 1]
    result = pd.DataFrame([[result]], columns=[named_as])
    # done
    return result


def _earliest(df: pd.DataFrame, args, grouped_by, named_as=None) -> pd.DataFrame:
    ...


def _latest(df: pd.DataFrame, args, grouped_by, named_as=None) -> pd.DataFrame:
    ...


FUNCTIONS = {
    'avg': _avg,
    'count': _count,
    'distinct_count': _distinct_count,
    'min': _min,
    'max': _max,
    'stddev': _stddev,
    'sum': _sum,
    'var': _var,
    'first': _first,
    'last': _last,
    'earliest': _earliest,
    'latest': _latest
}


def generate(dataframe, name, **params):
    fn = FUNCTIONS[name]
    return fn(dataframe, **params)
