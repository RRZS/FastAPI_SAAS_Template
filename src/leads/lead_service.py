# python imports
from datetime import datetime, timezone

# framework imports
from fastapi import HTTPException, status
from fastapi.encoders import jsonable_encoder

# application imports
from src.leads import schemas
from src.leads.lead_repository import lead_repo
from src.leads.models import Lead
from src.organization.org_repository import org_repo

# how long a "new" lead can sit before it counts as a missed follow-up
MISSED_LEAD_MINUTES = 60


class LeadService:
    def __init__(self, db):
        self.db = db
        self.lead_repo = lead_repo(self.db)
        self.org_repo = org_repo(self.db)

    # orm call
    def orm_call(self, lead: Lead) -> dict:
        return jsonable_encoder(lead)

    # resolve an org by slug or raise 404
    def get_org_or_404(self, org_slug: str):
        org = self.org_repo.get_org(org_slug)
        if not org:
            raise HTTPException(
                detail="Org does not exist",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        return org

    # resolve a lead scoped to an org or raise 404
    def get_lead_or_404(self, org_id: int, lead_id: int) -> Lead:
        lead = self.lead_repo.get_lead(org_id, lead_id)
        if not lead:
            raise HTTPException(
                detail="Lead does not exist",
                status_code=status.HTTP_404_NOT_FOUND,
            )
        return lead

    # public: capture a lead from a website form
    def capture_lead(
        self, org_slug: str, lead_capture: schemas.LeadCapture
    ) -> schemas.MessageLeadResp:
        org = self.get_org_or_404(org_slug)
        lead_dict = lead_capture.dict(exclude_unset=True)
        lead_dict["org_id"] = org.id
        if not lead_dict.get("source"):
            lead_dict["source"] = "web"
        lead = self.lead_repo.create_lead(lead_dict)
        return {
            "message": "Lead captured successfully",
            "data": self.orm_call(lead),
            "status": status.HTTP_201_CREATED,
        }

    # list every lead for an org
    def get_org_leads(self, org_slug: str) -> schemas.MessageListLeadResp:
        org = self.get_org_or_404(org_slug)
        leads = self.lead_repo.get_org_leads(org.id)
        return {
            "message": "Leads retrieved successfully",
            "data": [self.orm_call(lead) for lead in leads],
            "status": status.HTTP_200_OK,
        }

    # list leads that have not been followed up in time
    def get_missed_leads(self, org_slug: str) -> schemas.MessageListLeadResp:
        org = self.get_org_or_404(org_slug)
        leads = self.lead_repo.get_missed_leads(org.id, MISSED_LEAD_MINUTES)
        return {
            "message": "Missed leads retrieved successfully",
            "data": [self.orm_call(lead) for lead in leads],
            "status": status.HTTP_200_OK,
        }

    # fetch a single lead
    def get_lead(self, org_slug: str, lead_id: int) -> schemas.MessageLeadResp:
        org = self.get_org_or_404(org_slug)
        lead = self.get_lead_or_404(org.id, lead_id)
        return {
            "message": "Lead retrieved successfully",
            "data": self.orm_call(lead),
            "status": status.HTTP_200_OK,
        }

    # update a lead's details or status
    def update_lead(
        self, org_slug: str, lead_id: int, lead_update: schemas.LeadUpdate
    ) -> schemas.MessageLeadResp:
        org = self.get_org_or_404(org_slug)
        lead = self.get_lead_or_404(org.id, lead_id)
        update_data = lead_update.dict(exclude_unset=True)
        # stamp the follow-up time when a lead moves out of "new"
        if update_data.get("status") and update_data["status"] != "new":
            if lead.contacted_at is None:
                lead.contacted_at = datetime.now(timezone.utc)
        for key, value in update_data.items():
            setattr(lead, key, value)
        lead = self.lead_repo.update_lead(lead)
        return {
            "message": "Lead updated successfully",
            "data": self.orm_call(lead),
            "status": status.HTTP_200_OK,
        }

    # delete a lead
    def delete_lead(self, org_slug: str, lead_id: int):
        org = self.get_org_or_404(org_slug)
        lead = self.get_lead_or_404(org.id, lead_id)
        self.lead_repo.delete_lead(lead)


lead_service = LeadService
