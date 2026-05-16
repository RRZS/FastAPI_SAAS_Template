# framework imports
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

# application imports
from src.app.utils.db_utils import get_db
from src.auth.models import User
from src.leads import schemas
from src.leads.lead_service import lead_service
from src.organization.pipes import org_dep

# lead router
lead_router = APIRouter(prefix="/api/v1/org/{org_slug}/leads", tags=["Leads"])


@lead_router.post(
    "/capture/",
    status_code=status.HTTP_201_CREATED,
    response_model=schemas.MessageLeadResp,
)
def capture_lead(
    org_slug: str,
    lead_capture: schemas.LeadCapture,
    db: Session = Depends(get_db),
):
    """Public endpoint: capture a lead from a website form. No auth required."""
    return lead_service(db).capture_lead(org_slug, lead_capture)


@lead_router.get(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=schemas.MessageListLeadResp,
)
def get_org_leads(
    org_slug: str,
    current_user: User = Depends(org_dep.member_dep),
    db: Session = Depends(get_db),
):
    """List every lead for an org."""
    return lead_service(db).get_org_leads(org_slug)


@lead_router.get(
    "/missed/",
    status_code=status.HTTP_200_OK,
    response_model=schemas.MessageListLeadResp,
)
def get_missed_leads(
    org_slug: str,
    current_user: User = Depends(org_dep.member_dep),
    db: Session = Depends(get_db),
):
    """List leads that have not been followed up within the configured window."""
    return lead_service(db).get_missed_leads(org_slug)


@lead_router.get(
    "/{lead_id}/",
    status_code=status.HTTP_200_OK,
    response_model=schemas.MessageLeadResp,
)
def get_lead(
    org_slug: str,
    lead_id: int,
    current_user: User = Depends(org_dep.member_dep),
    db: Session = Depends(get_db),
):
    """Fetch a single lead."""
    return lead_service(db).get_lead(org_slug, lead_id)


@lead_router.patch(
    "/{lead_id}/update/",
    status_code=status.HTTP_200_OK,
    response_model=schemas.MessageLeadResp,
)
def update_lead(
    org_slug: str,
    lead_id: int,
    lead_update: schemas.LeadUpdate,
    current_user: User = Depends(org_dep.member_dep),
    db: Session = Depends(get_db),
):
    """Update a lead's details or move it through its status lifecycle."""
    return lead_service(db).update_lead(org_slug, lead_id, lead_update)


@lead_router.delete(
    "/{lead_id}/delete/",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_lead(
    org_slug: str,
    lead_id: int,
    current_user: User = Depends(org_dep.admin_rights_dep),
    db: Session = Depends(get_db),
):
    """Delete a lead. Admin only."""
    lead_service(db).delete_lead(org_slug, lead_id)
    return {"status": status.HTTP_204_NO_CONTENT}
