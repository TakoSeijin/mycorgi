import psycopg2
import pickle

from database import db_session
from models import Orgy

def delete_test_parties():
    # Connect to new database and get all test parties
    test_orgies = db_session.query(Orgy).all()
    # Delete all test parties
    for test_orgy in test_orgies:
        db_session.delete(test_orgy)
    db_session.commit()
    db_session.expunge_all()
    print 'done deleting test parties'

def migrate_old_orgies():
    old_orgies = pickle.load(open('/home/seth/imgur_migration/migrated_orgies.p', 'rb'))
    for orgy_name, orgy_data in old_orgies.iteritems():
        if orgy_data['youtube'] == 'none':
            youtube_id = None
        else:
            youtube_id = orgy_data['youtube']
        if orgy_data['direction'] == 'right':
            is_left_to_right = True
        else:
            is_left_to_right = False

        new_orgy = Orgy(name=orgy_name, is_old=True, foreground_url=orgy_data['foreground'],
                        background_url=orgy_data['background'], is_left_to_right=is_left_to_right,
                        youtube_id=youtube_id)
        db_session.add(new_orgy)
    db_session.commit() 

def migrate_subdomain_orgies():
    # Connect to old database
    old_db = psycopg2.connect("dbname=corgi user=seth2")
    old_cursor = old_db.cursor()
    # Get all old orgies
    query = "select * from orgies"
    old_cursor.execute(query)
    old_subdomain_orgies = old_cursor.fetchall()

    i = 0
    total = len(old_subdomain_orgies)
    for orgy in old_subdomain_orgies:
        if orgy[4] == 'right':
            is_left_to_right = True
        else:
            is_left_to_right = False

        if orgy[5] == 'none':
            youtube_id = None
        else:
            youtube_id = orgy[5]

        new_orgy = Orgy(name=orgy[0], is_old=False, foreground_url=orgy[3],
                        background_url=orgy[2], is_left_to_right=is_left_to_right,
                        youtube_id=youtube_id)
        db_session.add(new_orgy)
        if i % 20000 == 0:
            print i, '/', total
        i += 1
    
    db_session.commit()
    print 'done adding subdomain parties'

delete_test_parties()
migrate_old_orgies()
migrate_subdomain_orgies()
