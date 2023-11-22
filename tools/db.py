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
    try:
        with Session(engine) as session:
            session.execute(insert(Reagent), {"name": name, "formula": formula, "density": density, "quantity": quantity, "state": "available"})
            session.commit()
        return 0
    except:
        return 1

def get_quantity(rid):
    try:
        with Session(engine) as session:
            session.execute(select(Reagent.quantity).where(Reagent.id == rid))
            session.commit()
        return 0
    except:
        return 1

def return_reagent(rid, quantity):
    try:
        with Session(engine) as session:
            session.execute(update(Reagent).where(Reagent.id == rid).values(quantity=quantity, state="available"))
            session.commit()
        return 0
    except:
        return 1

def get_reagent(rid):
    try:
        with Session(engine) as session:
            session.execute(update(Reagent).where(Reagent.id == rid).values(state="unavailable"))
            session.commit()
        return 0
    except:
        return 1
    
def list_reagents():
    try:
        with Session(engine) as session:
            reagents = session.execute(select(Reagent)).all()
            for i in reagents:
                yield i[0]
    except:
        raise Exception("A critical error has ocurred while selecting reagents")

# add_reagent("Ácido Sulfúrico", "H2SO4", 1.83, 2)