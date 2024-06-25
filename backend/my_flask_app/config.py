import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'fd60388eb3e229e206ff18da6268ffd3'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///app.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY') or '36547c22e2badcb53b77993b7e079dbd'
