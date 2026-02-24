from typing import List, Optional
from src.schemas.campaign import (
    CampaignResponse,
    FeaturedCampaignResponse,
    UpcomingCampaignResponse,
)
from src.repositories.campaign_repository import campaign_repo


class CampaignService:
    def get_all_campaigns(self) -> list[CampaignResponse]:
        return campaign_repo.get_all()

    def get_campaign_by_id(self, campaign_id: int) -> Optional[CampaignResponse]:
        return campaign_repo.get_by_id(campaign_id)

    def get_featured_campaigns(self) -> list[FeaturedCampaignResponse]:
        return campaign_repo.get_featured()

    def get_upcoming_campaigns(self) -> list[UpcomingCampaignResponse]:
        return campaign_repo.get_upcoming()


campaign_service = CampaignService()
