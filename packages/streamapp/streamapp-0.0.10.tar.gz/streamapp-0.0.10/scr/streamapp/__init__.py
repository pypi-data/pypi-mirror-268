from streamlit import connection
from .snow_class import SnowConnection
from .authenticator import Auth
from .enviroment_selector import EnvironmentSelector
from .report_generator import ReportGenerator, InMemoryZip
from .roles import Roles
from .cards import Card
from .validators import BaseValidator
from .requests import BaseRequest
from .subpages import SubPages


class Conn:

    @property
    def connection(cls):
        return connection('snow', type=SnowConnection)

    @property
    def query(cls):
        return connection('snow', type=SnowConnection).query

    @property
    def query_async(cls):
        return connection('snow', type=SnowConnection).query_async

    @property
    def get_async_results(cls):
        return connection('snow', type=SnowConnection).get_async_results


conn = Conn()
login = Auth.login
setattr(BaseValidator, 'conn', conn)

__all__ = [
    'EnvironmentSelector',
    'ReportGenerator',
    'Roles',
    'Card',
    'BaseRequest',
    'utils',
    'BaseValidator',
    'InMemoryZip',
    'SubPages'
]
