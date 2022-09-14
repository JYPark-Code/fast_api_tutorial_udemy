from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# sqlite connection
# SQLALCHEMY_DATABASE_URL = "sqlite:///./todos.db"

# postgresql
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:elql0814@localhost/TodoApplicationDatabase"

# mysql
SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:elql0814@127.0.0.1:3306/todoapp"

# sqlite connection
# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )

# postgresql and mysql
engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

# session local class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# make base - import clear base
Base = declarative_base()


