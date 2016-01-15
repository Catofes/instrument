import RUtils
import time
import user_utils


class UserInfo:
    def __init__(self):
        self.uuid = None
        self.ifLogin = False
        self.token = None
        self.login_expired_date = time.time()
        self.username = None
        self.email = None
        self.admin = False
        self.status = 0

    def reload(self):
        result = RUtils.RDateBasePool().execute(
                'select * from users where uuid = %s;', (self.uuid,)
        )
        if not result:
            raise RUtils.RError(0)
        result = result[0]
        self.admin = result['admin']
        self.status = result['status']
        self.username = result['username']
        self.email = result['email']


class User:
    def __init__(self, db=RUtils.RDateBasePool().begin(), token=None):
        self.config = RUtils.RConfig()
        self.info = UserInfo()
        self.db = db
        self.session = RUtils.RMemorySessionStore()
        if token:
            self.info.token = token
            self.login_by_token()

    def login_by_token(self):
        if self.info.ifLogin:
            self.info.reload()
            return True

        if not self.info.token:
            self.info.ifLogin = False
            return False

        if self.session.contains(self.info.token):
            self.info = self.session.get(self.info.token)
            if time.time() < self.info.login_expired_date and self.info.ifLogin:
                self.info.reload()
                return True

        self.info.ifLogin = False
        self.session.remove(self.info.token)
        return False

    def login_by_password(self, username=None, password=None):
        if not username or not password:
            return False

        password = user_utils.hash_password(password)
        result = self.db.execute(
                'select * from users where username=%s and password=%s and status > 0;',
                (username, password)
        )
        if not result:
            return False
        result = result[0]
        self.info.uuid = result['uuid']
        self.info.token = RUtils.generate_code(64)
        self.info.ifLogin = True
        self.info.login_expired_date = time.time() + self.config.login_expired_time
        self.info.reload()
        self.session.push(self.info.token, self.info)
        return True

    def logout(self):
        if not self.info.ifLogin:
            return False
        self.info.ifLogin = False
        self.session.remove(self.info.token)
        return

    def update_password(self, new_password):
        if not new_password:
            return False
        self.db.execute(
                'update users set password = %s where uuid = %s',
                (self.info.username, user_utils.hash_password(new_password))
        )
        return True

