from pydantic import BaseModel

class AuthLogin(BaseModel):
    """
    :username: 用户名
    :password: 密码
    """

    username: str
    password: str


class ReturnAuthLogin(BaseModel):
    """
    :is_login_success: 登录是否成功
    :token: token
    """

    is_login_success: bool
    token: str = ""
