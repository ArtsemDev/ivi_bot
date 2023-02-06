from sqlalchemy import Column, SMALLINT, VARCHAR, ForeignKey, TIMESTAMP, DECIMAL

from .base import Base


class Category(Base):
    __tablename__ = 'categories'

    id = Column(SMALLINT, primary_key=True)
    name = Column(VARCHAR(64), unique=True, nullable=False)


class Movie(Base):
    __tablename__ = 'movies'

    title = Column(VARCHAR(256), nullable=False)
    descr = Column(VARCHAR(1024), nullable=False)
    category_id = Column(SMALLINT, ForeignKey('categories.id', ondelete='RESTRICT'), nullable=False)
    release_date = Column(TIMESTAMP, nullable=False)
    poster = Column(VARCHAR(512), nullable=False)
    kp_rating = Column(DECIMAL(4, 2), nullable=True)
    imdb_rating = Column(DECIMAL(4, 2), nullable=True)
