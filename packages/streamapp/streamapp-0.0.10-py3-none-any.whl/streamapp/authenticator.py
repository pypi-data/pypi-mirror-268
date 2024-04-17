"""Custom handler for streamlit Authenticator.

Login class to handle the login and logout from
streamlit authenticator, checking for password and
setting up the roles to acces specifict pages.
Streamlit Authenticator: https://blog.streamlit.io/streamlit-\
    authenticator-part-1-adding-an-authentication-component-to-your-app/

Usage:
    from streamapp_utils import logn
    `in the begining of your app file after set_page_config`
    login(['admin', 'role1', 'role2'])
"""

from streamlit_authenticator import Authenticate
from streamlit import (
    session_state, secrets, sidebar, stop, caption, warning, error
)
from typing import Optional, Callable
from .roles import Roles


class Auth:
    """Custom Login handler for streamlit authenticator.

    type: class callable

    This custom login handler checks for hashed password and
    sets up the roles to acces specifict pages.

    toml file:
        [credentials.usernames]
        Pepe.name = 'pepe@gmail.com'
        Pepe.roles = ['admin']
        Pepe.password = '$2b$12$6E4nrCcqA...'

    """
    @classmethod
    def login(cls, roles: Optional[list] = None,
              side_bar_widget: Callable = lambda: None) -> None:
        """Login callable to set up session user variables.

        This callable use the .secrets/toml file to get the user
        variables and check for the login and set up roles.

        Args:
            roles: list with the user granted roles

        Return:
            None
        """
        if session_state.get('authentication_status') is None:
            try:
                session_state.authenticator = Authenticate(
                    dict(secrets.credentials),
                    'cookie_name',
                    'key',
                    cookie_expiry_days=1
                )
                *_, username = session_state.authenticator.login(
                    'Login',
                    'main'
                )
                print('Login ', session_state.name)
                try:
                    session_state['roles'] = session_state.authenticator\
                        .credentials['usernames']\
                        .get(username)\
                        .get('roles', [])
                except AttributeError:
                    session_state['roles'] = []
            except KeyError:
                session_state.authentication_status = None
                warning('Try again something went wrong')
                stop()
            except AttributeError:
                error('There is no credentials setted up')
                stop()
        try:
            if session_state.authentication_status:
                cls.logout(side_bar_widget)
                Roles.allow_acces(roles)
            elif session_state.authentication_status is False:
                session_state.authentication_status = None
                error('Username/password is incorrect')
                stop()
            elif session_state.authentication_status is None:
                session_state.authentication_status = None
                warning('Please enter your username and password')
                stop()
        except AttributeError:
            session_state.authentication_status = None
        return

    @classmethod
    def logout(cls, side_bar_widget: Callable) -> None:
        """Logout and delete the session variable for user auth.

        Args:
            None

        Returns:
            None
        """
        session_state.authenticator.logout('Logout', 'sidebar')
        with sidebar:
            if side_bar_widget:
                side_bar_widget()
            caption(f'Welcome **{session_state.name}**')
        return
