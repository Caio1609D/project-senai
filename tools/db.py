import sqlalchemy
from sqlalchemy.orm import Session, Mapped, DeclarativeBase, mapped_column

engine = sqlalchemy.create_engine("sqlite:///reagents.db")

class Base(DeclarativeBase):
    pass

class Reagent(Base):
    __tablename__ = "reagents"

    id: Mappend[int] = mapped_column(primary_key=True)
    name: Mappend[str] = mapped_column()
