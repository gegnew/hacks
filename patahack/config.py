import os

class Config(object):
    """ 
    Config settings are defined as class variables inside the Config class.
    Feel free to add more configs as you go.
    """
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
