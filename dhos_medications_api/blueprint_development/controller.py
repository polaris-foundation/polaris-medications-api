from flask_batteries_included.sqldb import db


def reset_database() -> None:
    session = db.session
    session.execute("TRUNCATE TABLE tag cascade")
    session.execute("TRUNCATE TABLE relationship_table cascade")
    session.execute("TRUNCATE TABLE medication cascade")
    session.commit()
    session.close()
