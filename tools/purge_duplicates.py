from database import db_session
from models import Orgy
from sqlalchemy import func



taken_names = []
list_of_dupes = []

all_orgies = db_session.query(Orgy).filter(Orgy.is_old == False).all()

for orgy in all_orgies:
    if orgy.name not in taken_names:
        taken_names.append(orgy.name)
    else:
        db_session.delete(orgy)

db_session.commit()
