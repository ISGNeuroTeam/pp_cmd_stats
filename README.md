# pp_cmd_stats
Postprocessing command "stats"

Usage examples:
for `avg` function: `... | stats avg(age) as AvgAge, avg(cars) as AvgCars`
Grouping `by` is not available for using with this function.

for `count` function: `... | stats count(Surname) as CountSurname by Name, count(Surname) by age`

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
# pp_cms_stats
