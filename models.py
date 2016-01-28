from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import INTEGER, BOOLEAN, VARCHAR, CIDR
from database import Base

class Orgy(Base):
    __tablename__ = 'orgy'
    id               = Column(INTEGER, primary_key=True)
    name             = Column(VARCHAR(length=200), nullable=False)
    is_old           = Column(BOOLEAN, nullable=False)
    foreground_url   = Column(VARCHAR(length=100), nullable=False)
    background_url   = Column(VARCHAR(length=100), nullable=False)
    is_left_to_right = Column(BOOLEAN, nullable=False)
    youtube_id       = Column(VARCHAR(length=100))
    creator_ip       = Column(CIDR)

    def __repr__(self):
        return '<Orgy %s by %s>' % (self.name, self.creator_ip)
