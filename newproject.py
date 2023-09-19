from sqlalchemy import Column, create_engine, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship



class DB:
    
    _engine = create_engine("mysql+mysqlconnector://admin:admin123456654321@localhost:3306/mydatabase")
    _base = declarative_base()
    
    
    def __init__(self):
        self.session_maker = sessionmaker(bind=self._engine)
        self.session = None

    def create_session(self):
        self.session = self.session_maker()
        
    def create_all_table(self):
        self._base.metadata.create_all(self._engine)


    class SubClass:
        id = Column('id', Integer, primary_key=True, unique=True, autoincrement=True)

    class Afrad(SubClass, _base):
        __tablename__ = 'afrad'
        esm = Column('esm', String(50))
        family = Column('family', String(50))
        jaygah_id = Column('jaygah_id', Integer, ForeignKey('jaygah.id'))

    class Jaygah(SubClass, _base):
        __tablename__ = 'jaygah'
        esm = Column('esm', String(50))
        afrad = relationship('Afrad', backref='jaygah')
