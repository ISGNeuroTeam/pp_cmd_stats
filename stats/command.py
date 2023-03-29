import pandas
import pandas as pd
from otlang.sdk.syntax import Positional, OTLType
from pp_exec_env.base_command import BaseCommand, Syntax
from .functions import generate


class StatsCommand(BaseCommand):
    # define syntax of your command here
    syntax = Syntax(
        [
            Positional("function_name", required=False, otl_type=OTLType.FUNCTION, inf=True),
        ],
    )
    use_timewindow = False  # Does not require time window arguments
    idempotent = True  # Does not invalidate cache

    def transform(self, df: pd.DataFrame) -> pd.DataFrame:
        # self.log_progress('Start stats command')
        # that is how you get arguments
        function_name = self.get_iter('function_name')
        values = [x for x in function_name]

        # Make your logic here
        # df = pd.DataFrame(
        #     [
        #         ["John", "Snow", 10],
        #         ["Alex", "Smith", 7],
        #         ["Anna", "Show", 21],
        #         ["James", "Bond", 3],
        #         ["John", "Dow", 14]
        #     ],
        #     columns=["Name", "Surname", "age"])

        # Add description of what going on for log progress
        # self.log_progress('First part is complete.', stage=1, total_stages=2)
        #
        result_list = []
        for val in values:
            params = dict()
            funcname: object = val.value["funcname"]["value"]
            params['args'] = [x["value"] for x in val.value["funcargs"]]
            params['named_as'] = None if val.value.get("named_as") is None else val.value["named_as"]["value"]
            params['grouped_by'] = [x["value"] for x in val.value["grouped_by"]]
            # print(f'{df}')
            temp = generate(dataframe=df, name=funcname, **params)
            result_list.append(temp)

        if len(result_list) > 1:
            result = pandas.concat(result_list, axis=1)
        else:
            result = result_list[0]

        # self.log_progress('Last transformation is complete', stage=2, total_stages=2)

        return result
