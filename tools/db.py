import sqlalchemy
from sqlalchemy.orm import Session, Mapped, DeclarativeBase, mapped_column

engine = sqlalchemy.create_engine("sqlite:///reagents.db")
insert = sqlalchemy.insert
select = sqlalchemy.select
update = sqlalchemy.update

class Base(DeclarativeBase):
    pass

class Reagent(Base):
    __tablename__ = "reagents"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    formula: Mapped[str] = mapped_column()
    density: Mapped[float] = mapped_column()
    quantity: Mapped[float] = mapped_column()
    state: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"Reagent(id={self.id!r}, name={self.name!r}, formula={self.formula!r}, density={self.density!r}, quantity={self.quantity!r})"
    
Base.metadata.create_all(engine)

def add_reagent(name, formula, density, quantity):
    with Session(engine) as session:
        session.execute(insert(Reagent), {"name": name, "formula": formula, "density": density, "quantity": quantity, "state": "available"})
        session.commit()

def return_reagent(rid, quantity):
    with Session(engine) as session:
        session.execute(update(Reagent).where(Reagent.id == rid).values(quantity=quantity, state="available"))
        session.commit()

def get_reagent(rid):
    with Session(engine) as session:
        session.execute(update(Reagent).where(Reagent.id == rid).values(state="unavailable"))
        session.commit()

get_reagent(1)