#CONFIGURATION BASE CONFIGURATION
class Config():
    DEBUG: True
    TESTING: True
    
    # SQLALCHEMY DATABASE CONFIGURATION
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:123qweAs*@localhost:3306/database_name"
    
#PRODUCTION SERVER CONFIGURATION
class ProductionConfig(Config):
    DEBUG: False
    

#DEVELOPMENT SERVER CONFIGURATION    
class DevelopmentConfig(Config):
    SECRET_KEY = "hardsecretkey"
    DEBUG = True
    TESTING = True
    
    
    