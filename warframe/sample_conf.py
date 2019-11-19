from warframe.auth import auth


class Config:
    SECRET_KEY = 'ITS A SECRET!'
    SQLALCHEMY_DATABASE_URI = 'mysql://{DB_user}:{DB_user_pass}@localhost/{DB}'
    MAIL_SERVER = 'mail.sample.net'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME, MAIL_PASSWORD = auth
