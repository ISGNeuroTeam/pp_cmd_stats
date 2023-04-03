# pp_cmd_stats
Postprocessing command "stats"

Usage examples:
for `avg` function: `... | stats avg(age) as AvgAge, avg(cars) as AvgCars`
Grouping `by` is not available for using with this function.

for `count` function: `... | stats count(Surname) as CountSurname by Name, count(Surname) by age`

for `min` function: `... | stats min(age) as MinAge, min(age)`
Grouping `by` is not available for using with this function.

for `max` function: `... | stats max(age) as MaxAge, max(age)`
Grouping `by` is not available for using with this function.

for `stddev` function: `... | stats stddev(age) as StdAge, stddev(age)`
Grouping `by` is not available for using with this function.

for `sum` function: `... | stats sum(age) as SumAge, sum(age)`
Grouping `by` is not available for using with this function.

for `var` function: `... | stats var(age) as VarAge, var(age)`
Grouping `by` is not available for using with this function.

for `first` function: `... | stats first(age) as FirstAge, first(age)`
Grouping `by` is not available for using with this function.

for `last` function: `... | stats last(age) as LastAge, last(age)`
Grouping `by` is not available for using with this function.

for `distinct_count` function: `... | stats distinct_count(Surname) by Name as DistinctCountSurname`

for `list` function: `... | stats list(Surname) as listSurname`
Grouping `by` is not available for using with this function.

for `values` function: `... | stats values(age) as ValuesAge`
Grouping `by` is not available for using with this function.

for `earliest` function: `... | stats earliest(age) as EarliestAge`
Grouping `by` is not available for using with this function.
It works only when dataframe has `_time` column with datetime data.

for `latest` function: `... | stats latest(age) as LatestAge`
Grouping `by` is not available for using with this function.
It works only when dataframe has `_time` column with datetime data.


## Getting started
###  Prerequisites
1. [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

### Installing
1. Create virtual environment with post-processing sdk 
```bash
make dev
```
That command  
- creates python virtual environment with [postprocessing_sdk](https://github.com/ISGNeuroTeam/postprocessing_sdk)
- creates `pp_cmd` directory with links to available post-processing commands
- creates `otl_v1_config.ini` with otl platform address configuration

2. Configure connection to platform in `otl_v1_config.ini`

### Test stats
Use `pp` to test stats command:  
```bash
pp
Storage directory is /tmp/pp_cmd_test/storage
Commmands directory is /tmp/pp_cmd_test/pp_cmd
query: | otl_v1 <# makeresults count=100 #> |  stats 
```
# pp_cmd_stats
