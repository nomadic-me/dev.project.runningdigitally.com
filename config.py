import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql://dev_prj_rnigdigi:ePC-Xq9MePC-Xq9M@mysql.dev.runningdigitally.com/dev_project_runningdigitally'
    SQLALCHEMY_TRACK_MODIFICATIONS = False