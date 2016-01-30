from database import db_session
from models import Orgy

party_to_delete = 'INSERT ORGY NAME HERE'

party = db_session.query(Orgy)\
                   .filter(Orgy.name.ilike(party_to_delete))\
                   .filter(Orgy.is_old == False)\
                   .one_or_none()
db_session.delete(party)
db_session.commit()

print 'done deleting', orgy_to_delete
