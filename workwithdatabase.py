from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.sql.expression import and_



# database+library://username:password@host:port/database_name
engine = create_engine("mysql+mysqlconnector://admin:admin123456654321@localhost:3306/sqlalchemy")
base = declarative_base()
session = sessionmaker(bind=engine)()



#Creating tables
class Student(base):
    __tablename__ = 'student'
    id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    classroom_id = Column('classroom_id',Integer, ForeignKey('classroom.id'))

class ClassRoom(base):
    __tablename__ = 'classroom'
    id = Column('id', Integer, unique=True, primary_key=True)
    name = Column('name', String(50))
    students = relationship('Student', backref='classroom', uselist=False)

base.metadata.create_all(engine)



# #SELECT
# students = session.query(Student).all()
# for student in students:
#     print(student._id, student.name)
#
# students = session.query(Student).first()
# print(students._id, students.name)
#
# students = session.query(Student).filter(Student.name=='Ali').all()
# print(students)
#
# students = session.query(Student).filter(and_(Student.name=='Ali', Student._id == 1)).all()
# print(students)
#
# students = session.query(Student).order_by(Student._id).all()
# for student in students:
#     print(student._id, student.name)



# #INSERT
# student_1 = Student(name='MohammadAli')
# student_2 = Student(name='MohammadReza')
# session.add_all([student_1, student_2])
# session.commit()



# #DELETE
# students = session.query(Student).filter(Student.name == 'MohammadAli').first()
# session.delete(students)
# session.commit()
#
# session.query(Student).filter(Student.name == 'MohammadReza').delete()
# session.commit()



# #UPDATE
# students = session.query(Student).filter(Student.name == 'Ali').first()
# students.name = 'ali2'
# session.commit()
#
# session.query(Student).filter(Student.name == 'Abolfazl').update({'name':'Mohammad'})
# session.commit()



