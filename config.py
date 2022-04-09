import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or b'_5#Gy2L"\nF4sdQ8z\x8e2c]/'