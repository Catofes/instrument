import RUtils
import hashlib
import user


def hash_password(password):
    return hashlib.sha512(password + RUtils.RConfig().password_salt).hexdigest()[0:64]


def require_login(func):
    def check_login(*args, **kwargs):
        if 'token' not in args[1].params.keys():
            raise RUtils.RError(2)
        data = user.User(db=args[1].context['sql'], token=args[1].params['token'])
        data.login_by_token()
        if not data.info.ifLogin:
            raise RUtils.RError(3)
        func(*args, user=user, **kwargs)

    return check_login
