import os

class Config:

    NEWS_API_BASE_URL ='https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    NEWS_API_KEY = '096d6a4804634f82a51e692f6b03aabb'
    ARTS_API_BASE_URL ='https://newsapi.org/v2/everything?q=bitcoin={}&apiKey={}'
   


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}   