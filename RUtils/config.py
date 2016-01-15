import singleton


class RConfig(singleton.Singleton):
    """Config Class

    This class store some import parameters of the app.
    Such as database username, password, etc.
    """

    def __init__(self):
        if hasattr(self, '_init'):
            return
        self._init = True
        self.password_salt = "hahahssdf"
        self.login_expired_time = 30 * 24 * 3600
        self.db_user = "instrument"
        self.db_passwd = "LsK7F9R5RsCrpjdZ"
        self.db_host = "127.0.0.1"
        self.db_port = 5432
        self.db_db = "instrument"
        self.db_mincached = 5
        self.db_maxcached = 40
        self.db_maxshared = 40
        self.db_maxconnections = 40
        self.session_cache_size = 1000
        self.mail_host = "cn-aliyun-mail.catofes.com"
        self.mail_port = 587
        self.mail_username = "InstrumentRent@catofes.com"
        self.mail_password = "LsK7F9R5RsCrpjdZ-Epg"
        self.mail_timeout = 3
        self.mail_from_address = "noreply@railgun.ac"
        self.mail_thread_numbers = 1
