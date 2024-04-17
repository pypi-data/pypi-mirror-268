"""Snowflake query tool to pass quick queries

Class definition to use in other validator classes that runs
a Snoflake query, intended to be use as a quick approach to
pass tables, columns, conditions and groupers.

The idea is use this validators as parent clases in other
that need make checks about recurrent issues or queries.

Usage
    from streamapp_utils import BaseValidator

    class TestValidator(BaseValidator):
        def test_exists(self, id: int):
            result = self.query(
                table='MY_SCHEMA.USERS',
                columns=['USER', 'NAME'],
                WHERE=[f'id = "{id}"']
            )
            return not result.empty

        def test_second(self, id: int):
            ...
"""
from typing import Optional
from .snow_class import SnowConnection
from pandas import DataFrame


class BaseValidator:
    """Class definition to use in other validator classes that runs
    a Snoflake query, intended to be use as a quick approach to
    pass tables, columns, conditions and groupers.
    """
    conn: SnowConnection
    query_base = """
        SELECT
            {% for column in columns %}
                 {{'' if loop. first else ', '}}{{column}}
            {% endfor %}
        FROM {{table}}
        {% if where %}
            where
            {% for condition in where %}
                 {{'' if loop. first else 'AND '}}{{condition}}
            {% endfor %}
        {% endif %}
        {% if group_by %}
            group by
            {% for condition in group_by %}
                 {{'' if loop. first else ', '}}{{condition}}
            {% endfor %}
        {% endif %}
    """

    @classmethod
    def query(cls, table: str, columns: list[str] = ['*'],
              where: Optional[list[str]] = None,
              group_by: Optional[list[int | str]] = None,
              succes_confirmation: bool = False) -> DataFrame:
        """Parse and perform query

        Args:
            table: table name to query
            colums: list wiht columsn to check
            where: conditions list to query
            group_by: list of columns to group
            succes_confirmation: bool to call a success toast

        Returns:
            a DataFrame object to perform validations
        """
        result = cls.conn.query(
            query=cls.query_base,
            params={
                'columns': columns,
                'table': table,
                'where': where,
                'group_by': group_by
            },
            template=False,
            succes_confirmation=succes_confirmation
        )
        return result
