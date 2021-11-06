import datetime
import os
from flask_security import LoginForm

# Directories Path -----------------------------------------------------------------------------------------------------
basedir = os.path.dirname(os.path.abspath(__file__))
templates_path = os.path.join(basedir, "templates")
static_path = os.path.join(basedir, "static")
UPLOAD_FOLDER = os.path.join(basedir, "uploads")

# Site Settings --------------------------------------------------------------------------------------------------------
per_page = 12
last_posts_limit = 10

# Security -------------------------------------------------------------------------------------------------------------
    # Security Configs
SECRET_KEY = os.environ.get("SECRET_KEY", 'pf9Wkove4IKEAXvy-cQkeDPhv9Cb3Ag-wyJILbq_dFw')
SECURITY_PASSWORD_SALT = os.environ.get("SECURITY_PASSWORD_SALT", '146585145368132386173505678016728509634')
ALLOWED_FILES = ('jpg', 'png')

    # Security Options
SECURITY_REGISTERABLE = True
SECURITY_SEND_REGISTER_EMAIL = True
SECURITY_USERNAME_ENABLE = True
SECURITY_CONFIRMABLE = True
SECURITY_USERNAME_REQUIRED = True
SECURITY_URL_PREFIX = '/users/'
SECURITY_I18N_DOMAIN = "Minecraft"
SECURITY_POST_REGISTER_VIEW = 'security.login'
SECURITY_POST_CONFIRM_VIEW = 'security.login'

    # Security Messages Translation To Persian
SECURITY_EMAIL_SUBJECT_REGISTER = "FlaskFa - Welcome"
SECURITY_EMAIL_SUBJECT_CONFIRM = "FlaskFa - لطفا ایمیل خود را تایید کنید"
# SECURITY_MSG_LOGIN = ('برای دسترسی به این صفحه باید وارد حساب کاربری خود شوید', 'error')
# SECURITY_MSG_INVALID_PASSWORD = ('رمز عبور اشتباه است', 'error')
# SECURITY_MSG_INVALID_EMAIL_ADDRESS = ('ایمیل وارد شده نا معتبر است', 'error')
# SECURITY_MSG_USER_DOES_NOT_EXIST = ('کاربری با این ایمیل وجود ندارد', 'error')

# Mail Configuration ---------------------------------------------------------------------------------------------------
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_USERNAME = 'xsamansafaeix@gmail.com'
MAIL_PASSWORD = 'mrlmajhwergpjsxh'

# Database Configs -----------------------------------------------------------------------------------------------------
    # Database Path
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, "database", "data.sqlite")
    # disable Database Track Modifications massages
SQLALCHEMY_TRACK_MODIFICATIONS = False

DEBUG = True
