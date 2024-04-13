import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@localhost/dbname'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CELERY_BROKER_URL = 'amqp://guest:guest@localhost//'
    CELERY_RESULT_BACKEND = 'amqp://guest:guest@localhost//'

