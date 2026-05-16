# python imports
from datetime import datetime, timedelta, timezone

# 3rd party imports
from sqlalchemy.orm import Session

# application imports
from src.leads.models import Lead


class LeadRepo:
    def __init__(self, db: Session) -> None:
        self.db = db

    # lead base query
    def base_query(self):
        return self.db.query(Lead)

    # get a single lead scoped to an org
    def get_lead(self, org_id: int, lead_id: int):
        return (
            self.base_query()
            .filter(Lead.org_id == org_id, Lead.id == lead_id)
            .first()
        )

    # all leads for an org, newest first
    def get_org_leads(self, org_id: int):
        return (
            self.base_query()
            .filter(Lead.org_id == org_id)
            .order_by(Lead.date_created.desc())
            .all()
        )

    # leads still in "new" status created more than `minutes` ago
    def get_missed_leads(self, org_id: int, minutes: int):
        cutoff = datetime.now(timezone.utc) - timedelta(minutes=minutes)
        return (
            self.base_query()
            .filter(
                Lead.org_id == org_id,
                Lead.status == "new",
                Lead.date_created < cutoff,
            )
            .order_by(Lead.date_created.desc())
            .all()
        )

    # create lead
    def create_lead(self, lead_create: dict):
        new_lead = Lead(**lead_create)
        self.db.add(new_lead)
        self.db.commit()
        self.db.refresh(new_lead)
        return new_lead

    # update lead
    def update_lead(self, lead: Lead):
        self.db.commit()
        self.db.refresh(lead)
        return lead

    # delete lead
    def delete_lead(self, lead: Lead):
        self.db.delete(lead)
        self.db.commit()


lead_repo = LeadRepo
