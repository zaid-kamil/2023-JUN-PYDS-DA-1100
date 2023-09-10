# pip install sqlalchemy
from sqlalchemy.orm import declarative_base
from sqlalchemy.engine import create_engine
from sqlalchemy import Column, String, Integer

Base = declarative_base()

class Article(Base):
    __tablename__ = 'articles'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    pub_date = Column(String)
    summary = Column(String)

    def __str__(self):
        return self.title
    
if __name__ == "__main__":
    engine = create_engine('sqlite:///articles.db', echo=True)
    Base.metadata.create_all(engine)