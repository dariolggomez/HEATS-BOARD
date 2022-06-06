from models.user_model import Base
from sqlalchemy.orm import  sessionmaker
from sqlalchemy import  create_engine
#BASE_DIR = os.path.dirname(os.path.realpath(__file__))

connection_string = "postgresql://postgres:simplepass321@localhost/boardDB"#+os.path.join(BASE_DIR,'site.db')

engine = create_engine(connection_string,echo = True)

Session = sessionmaker()

Base.metadata.create_all(engine)