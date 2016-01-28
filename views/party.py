from flask import Blueprint, render_template
from models import Orgy
from database import get_db_session

party = Blueprint('party', __name__)

# If coming in to a subdomain, that's a new party
@party.route('/', subdomain='<party_subdomain>')
def show_party(party_subdomain):
    db_session = get_db_session()
    party = db_session.query(Orgy)\
                      .filter(Orgy.name.ilike(party_subdomain))\
                      .filter(Orgy.is_old == False)\
                      .one_or_none()
    if not party:
        return 'Party not found! Make one <a href="//my.corgiorgy.com">here</a>!', 404
    else:
        return render_template('party.html', party=party)

# If coming to an unrecgnized path on 'my' subdomain,
# that's an old party
@party.route('/<path:old_party_name>', subdomain='my')
def show_old_party(old_party_name):
    db_session = get_db_session()
    party = db_session.query(Orgy)\
                      .filter(Orgy.name == old_party_name)\
                      .filter(Orgy.is_old == True)\
                      .one_or_none()
    if not party:
        return 'Party not found! Make one <a href="//my.corgiorgy.com">here</a>!', 404
    else:
        return render_template('party.html', party=party)
