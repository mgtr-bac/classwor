from data import db_session
from data.user import User


db_session.global_init("db/mars_explore.db")
session = db_session.create_session()

captain = User(
    surname="Scott",
    name="Ridley",
    age=21,
    position="captain",
    speciality="research engineer",
    address="module_1",
    email="scott_chief@mars.org"
)
session.add(captain)
colonist1 = User(
    surname="Rain",
    name="Bom",
    age=35,
    position="Engineer",
    speciality="Mechanical Engineer",
    address="module_2",
    email="bom@mars.org"
)
colonist2 = User(
    surname="Petrov",
    name="Petr",
    age=40,
    position="Biologist",
    speciality="Biology",
    address="module_3",
    email="petrov@mars.org"
)

colonist3 = User(
    surname="Anna",
    name="Ivanova",
    age=29,
    position="Medic",
    speciality="Medicine",
    address="module_4",
    email="ivanova@mars.org"
)
session.commit()
