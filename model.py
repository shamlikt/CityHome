from sqlalchemy import Column, Integer, String, create_engin
from sqlalchemy.ext.declarative import declarative_base

class User(Base):
    __tablename__ = 'user'

     id = Column(Integer, primary_key=True)
     name = Column(String)
     fullname = Column(String)

     def __repr__(self):
        return "<User(name='%s', fullname='%s', password='%s')>" % (
            self.name, self.fullname, self.password)

class City(Base):
    __tablename__ = 'city'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    pincode= Column(String)

    def __repr__(self):
        return "<City(name='%s', pincode='%s')>" % (
            self.name, self.pincode)

class House(Base):
    __tablename__ = 'house'
    id = Column(Integer, primary_key=True)
    hose_number = Column(String)
    user = Column(Integer, ForeignKey('user.id'))
    city = Column(Integer, ForeignKey('city.id'))
    def __repr__(self):
        return "<House(number='%s'')>" % (
            self.name)


DB_FILE = "test.db"
engine = create_engine('sqlite:///{}'.format(DB_FILE))
Base.metadata.create_all(engine)
