from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

project_developer = Table(
    'project_developers',
    Base.metadata,
    Column('id', Integer, primary_key=True),
    Column('developer_id', Integer, ForeignKey('developers.id')),
    Column('project_id', Integer, ForeignKey('projects.id')),
    Column('role', String),
    Column('join_date', Date)
)

class Developer(Base):
    __tablename__ = 'developers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    skills = Column(String)
    
    projects = relationship("Project", secondary=project_developer, back_populates="developers")

class Manager(Base):
    __tablename__ = 'managers'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    department = Column(String)
    
    projects = relationship("Project", back_populates="manager")

class Project(Base):
    __tablename__ = 'projects'
    
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    manager_id = Column(Integer, ForeignKey('managers.id'))
    
    manager = relationship("Manager", back_populates="projects")
    developers = relationship("Developer", secondary=project_developer, back_populates="projects")

def create_db():
    engine = create_engine('sqlite:///software_development.db', echo=False)
    Base.metadata.create_all(engine)
    return engine

def create_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()