import sqlalchemy as sql
import datetime
from sqlalchemy.orm import Session, Mapped, DeclarativeBase, mapped_column, relationship
from werkzeug.security import check_password_hash, generate_password_hash
from typing import List

engine = sql.create_engine("sqlite:///reagents.db")
insert = sql.insert
select = sql.select
update = sql.update

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
    registers: Mapped[List["Register"]] = relationship()

    def __repr__(self) -> str:
        return f"Reagent(id={self.id!r}, name={self.name!r}, formula={self.formula!r}, density={self.density!r}, quantity={self.quantity!r}, state={self.state!r}, last={self.last!r})"

class Admin(Base):
    __tablename__ = "admins"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, username={self.username!r}, password={self.password!r})"
    
class Register(Base):
    __tablename__ = "registers"

    id: Mapped[int] = mapped_column(primary_key=True)
    reagent_id: Mapped[int] = mapped_column(sql.ForeignKey("reagents.id"))
    date: Mapped[datetime.datetime] = mapped_column(sql.types.DateTime(timezone=True), server_default=sql.sql.func.now())
    description: Mapped[str] = mapped_column()
    spend: Mapped[float] = mapped_column()

Base.metadata.create_all(engine)

def add_reagent(name, formula, density, quantity):
    try:
        with Session(engine) as session:
            session.execute(insert(Reagent), {"name": name, "formula": formula, "density": density, "quantity": quantity, "state": "available", "last": 0})
            session.commit()
        return 0
    except:
        raise Exception("Couldn't add reagent")

def get_quantity(rid):
    try:
        with Session(engine) as session:
            session.execute(select(Reagent.quantity).where(Reagent.id == rid))
            session.commit()
        return 0
    except:
        raise Exception("Couldn't define the quantity")

def is_available(rid):
    try:
        with Session(engine) as session:
            stmt = select(Reagent.state).where(Reagent.id == rid)
            state = session.scalar(stmt)
            if state == "available":
                return True
            else:
                return False
    except:
        raise Exception("We couldn't find out wether the reagent is available or not")

def return_reagent(rid, quantity):
    try:
        with Session(engine) as session:
            session.execute(update(Reagent).where(Reagent.id == rid).values(quantity=quantity, state="available"))
            session.execute()
            session.commit()
        return 0
    except:
        raise Exception("Couldn't return reagent")
    
def create_user(username, password):
    try:
        with Session(engine) as session:
            session.execute(insert(Admin).values(username=username, password=generate_password_hash(password)))
            session.commit()
        return 0
    except:
        raise Exception("Error while creating a new user")

def login(username, password):
    authenticate = False
    try: 
        with Session(engine) as session:
            truepass = session.execute(select(Admin.password).where(Admin.username == username)).first()
            if truepass:
                truepass = truepass[0]
                if check_password_hash(truepass, password):
                    authenticate = True
                    session.commit()
        return authenticate
    except:
        raise Exception("Error while logging in")

def get_reagent(rid):
    try:
        with Session(engine) as session:
            session.execute(update(Reagent).where(Reagent.id == rid).values(state="unavailable"))
            session.execute(insert(Register), {"reagent_id": rid})
            session.commit()
        return 0
    except:
        raise Exception("Error while gettint reagent")
    
def list_reagents():
    try:
        with Session(engine) as session:
            reagents = session.execute(select(Reagent)).all()
            for i in reagents:
                yield i[0]
    except:
        raise Exception("A critical error has ocurred while selecting reagents")

# create_user("Teste", "123456")