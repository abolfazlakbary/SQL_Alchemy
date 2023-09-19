from sqlalchemy import Column, create_engine, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship



class DB:
    
    _engine = create_engine("mysql+mysqlconnector://admin:admin123456654321@localhost:3306/university")
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

    class ReshteHa(SubClass, _base):
        __tablename__ = 'reshte_ha'
        esm = Column('esm', String(50))
        daneshjo_ha_reshte = relationship('DaneshjoHa', backref='reshte')
        kelas_reshte = relationship('KelasHa', backref='reshte_kelas')
            
    class Asatid(SubClass, _base):
        __tablename__ = 'asatid'
        esm = Column('esm', String(50))
        family = Column('family', String(50))
        kelas_ha = relationship('KelasHa', backref='ostad')

    class DaneshjoHa(SubClass, _base):
        __tablename__ = 'daneshjo_ha'
        esm = Column('esm', String(50))
        family = Column('family', String(50))
        id_reshte = Column('id_reshte',Integer, ForeignKey('reshte_ha.id'))
        kelas_ha = relationship('KelasHa', secondary='DaneshjoKelas', back_populates='daneshjo_ha')

    class KelasHa(SubClass, _base):
        __tablename__ = 'kelas_ha'
        esm = Column('esm', String(50))
        id_ostad = Column('id_ostad', Integer, ForeignKey('asatid.id'))
        id_reshte = Column('id_reshte', Integer, ForeignKey('reshte_ha.id'))
        daneshjo_ha = relationship('DaneshjoHa', secondary='DaneshjoKelas', back_populates='kelas_ha')
    
    class DaneshjoKelas(SubClass, _base):
        __tablename__ = 'daneshjo_kelas'
        id_daneshjo = Column('id_daneshjo', Integer, ForeignKey('daneshjo_ha.id'))
        id_kelas = Column('id_kelas', Integer, ForeignKey('kelas_ha.id'))


if __name__ == '__main__':
    db = DB()
    db.create_all_table()
    db.create_session()
    
    # #Creating a new reshte :)
    # reshte = db.ReshteHa(esm='riazi')
    # db.session.add(reshte)
    # db.session.commit()
    
    # #Creating a new daneshjo :)
    # daneshjo = db.DaneshjoHa(esm='ali', family='alizade', reshte=reshte)
    # db.session.add(daneshjo)
    # db.session.commit()
    # print(daneshjo.id_reshte)
    
    # # #Creating a new ostad :)
    # ostad = db.Asatid(esm='ostad1', family='ostad_1_family')
    # db.session.add(ostad)
    # db.session.commit()
    
    # #Creating a new kelas :)
    # reshte = db.session.query(db.ReshteHa).one()
    # kelas = db.KelasHa(esm='kelas_A', reshte_kelas= reshte, ostad=ostad)
    # db.session.add(kelas)
    # db.session.commit()
