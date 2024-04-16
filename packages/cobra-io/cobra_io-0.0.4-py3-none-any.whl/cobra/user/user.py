from getpass import getpass
from typing import Optional

from cobra.utils.urls import BASE_URL
from cobra.utils.requests import session


_refresh_token = None


def login(e_mail: str, password: Optional[str] = None) -> str:
    """
    Login to COBRA and return the access token.

    :param e_mail: The e-mail address of the user.
    :param password: The password of the user; alternatively, the user will be prompted to enter the password.
    :return: The access token.
    """
    global _refresh_token
    if _refresh_token is not None:
        r_refresh = session.post(BASE_URL + 'token/refresh/', data={'refresh': _refresh_token})
        if r_refresh.status_code == 200:
            return r_refresh.json()['access']
        # Fall through if refresh token is invalid.
    if password is None:
        password = getpass(f"Please enter the password for {e_mail}: ")
    r_login = session.post(BASE_URL + 'token/', data={'email': e_mail, 'password': password})
    if r_login.status_code != 200:
        raise ValueError("Invalid credentials.")
    _refresh_token = r_login.json()['refresh']
    return r_login.json()['access']


def logout():
    """
    Logout from COBRA.
    """
    global _refresh_token
    _refresh_token = None
