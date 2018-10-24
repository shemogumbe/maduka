from .database import db_session


class Utility(object):
    def save(self):
        db_session.add(self)
        db_session.commit()

