from database import db_session
from models import Orgy

orgy_to_delete = 'ka400'

party = db_session.query(Orgy)\
                   .filter(Orgy.name.ilike(orgy_to_delete))\
                   .filter(Orgy.is_old == False)\
                   .one_or_none()
db_session.delete(party)
db_session.commit()

print 'done deleting', orgy_to_delete
