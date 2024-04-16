import copy

import numpy as np

from mindsdb_sql.parser.ast import (
    Identifier,
)
from mindsdb_sql.planner.steps import (
    JoinStep,
)
from mindsdb_sql.planner.utils import query_traversal
from mindsdb_sql.render.sqlalchemy_render import SqlalchemyRender

from mindsdb.api.executor.sql_query.result_set import ResultSet
from mindsdb.api.executor.utilities.sql import query_df_with_type_infer_fallback
from mindsdb.api.executor.exceptions import NotSupportedYet

from .base import BaseStepCall


class JoinStepCall(BaseStepCall):

    bind = JoinStep

    def call(self, step):
        left_data = self.steps_data[step.left.step_num]
        right_data = self.steps_data[step.right.step_num]
        table_a, names_a = left_data.to_df_cols(prefix='A')
        table_b, names_b = right_data.to_df_cols(prefix='B')

        if right_data.is_prediction or left_data.is_prediction:
            # ignore join condition, use row_id
            a_row_id = left_data.find_columns('__mindsdb_row_id')[0].get_hash_name(prefix='A')
            b_row_id = right_data.find_columns('__mindsdb_row_id')[0].get_hash_name(prefix='B')

            join_condition = f'table_a.{a_row_id} = table_b.{b_row_id}'

            join_type = step.query.join_type.lower()
            if join_type == 'join':
                # join type is not specified. using join to prediction data
                if left_data.is_prediction:
                    join_type = 'left join'
                elif right_data.is_prediction:
                    join_type = 'right join'
        else:
            def adapt_condition(node, **kwargs):
                if not isinstance(node, Identifier) or len(node.parts) != 2:
                    return

                table_alias, alias = node.parts
                cols = left_data.find_columns(alias, table_alias)
                if len(cols) == 1:
                    col_name = cols[0].get_hash_name(prefix='A')
                    return Identifier(parts=['table_a', col_name])

                cols = right_data.find_columns(alias, table_alias)
                if len(cols) == 1:
                    col_name = cols[0].get_hash_name(prefix='B')
                    return Identifier(parts=['table_b', col_name])

            if step.query.condition is None:
                raise NotSupportedYet('Unable to join table without condition')

            condition = copy.deepcopy(step.query.condition)
            query_traversal(condition, adapt_condition)

            join_condition = SqlalchemyRender('postgres').get_string(condition)
            join_type = step.query.join_type

        query = f"""
                       SELECT * FROM table_a {join_type} table_b
                       ON {join_condition}
                   """
        resp_df, _description = query_df_with_type_infer_fallback(query, {
            'table_a': table_a,
            'table_b': table_b
        })

        resp_df = resp_df.replace({np.nan: None})

        names_a.update(names_b)
        data = ResultSet().from_df_cols(resp_df, col_names=names_a)

        for col in data.find_columns('__mindsdb_row_id'):
            data.del_column(col)

        return data
