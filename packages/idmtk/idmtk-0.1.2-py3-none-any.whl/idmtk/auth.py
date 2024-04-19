from .models import AuthLogin, ReturnAuthLogin
import requests
from requests import Response

def login(username: str, password: str):
    params = AuthLogin(username=username, password=password)
    return _login(params=params)


def _login(params: AuthLogin) -> ReturnAuthLogin:
    """
    登录函数底层
    """

    url: str = "http://10.64.198.12:8008/admin/login"
    json_data: dict = {"loginName": params.username, "password": params.password}
    headers: dict = {"Content-Type": "application/json"}
    response: Response = requests.post(url=url, json=json_data, headers=headers)

    if response.status_code == 200:
        token = response.json()["token"]
        return ReturnAuthLogin(is_login_success=True, token=token)
    else:
        return ReturnAuthLogin(is_login_success=False)
