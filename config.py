# -*- coding: utf-8 -*-
#==============================================================================
#  coding by ShimchY shimchy@gmail.com and ... 2017
#==============================================================================
import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'ERER$%34834-dfsff-oji4e'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    FLASKY_MAIL_SUBJECT_PREFIX    = '[FLASKY]'
    FLASK_MAIL_SENDER             = 'Flasky Admin <ShimchY@gmail.com>'
    FLASK_ADMIN                   = os.environ.get('FLASKY_ADMIN')

    @staticmethod    
    def init_app(app):
        pass
    
class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USRENAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    SQLCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
        
class TestingConfig(Config):
    TESTING =True
    SQLALCHEMY_DATABASE_URI = os.environ.get('TESTING_DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data-test.sqlite')

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing'    : TestingConfig,
    'production' : ProductionConfig,
    
    'default'    : DevelopmentConfig
}