# 3rd party imports
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, text
from sqlalchemy.orm import relationship

# application imports
from src.app.utils.models_utils import AbstractModel


# Lead Table.
class Lead(AbstractModel):
    __tablename__ = "lead"
    org_id = Column(
        Integer, ForeignKey("organization.id", ondelete="CASCADE"), nullable=False
    )
    name = Column(String, nullable=False)
    email = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    message = Column(String, nullable=True)
    source = Column(String, nullable=False, server_default=text("'web'"))
    status = Column(String, nullable=False, server_default=text("'new'"))
    contacted_at = Column(TIMESTAMP(timezone=True), nullable=True)
    org = relationship("Organization")
