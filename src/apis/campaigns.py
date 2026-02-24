from fastapi import APIRouter, HTTPException
from typing import List
from src.schemas.campaign import (
    CampaignResponse,
    FeaturedCampaignResponse,
    UpcomingCampaignResponse,
)
from src.services.campaign_service import campaign_service

router = APIRouter(prefix="/campaigns", tags=["Campaigns"])


@router.get("", response_model=List[CampaignResponse])
def get_all_campaigns():
    return campaign_service.get_all_campaigns()


@router.get("/{campaign_id}", response_model=CampaignResponse)
def get_campaign_by_id(campaign_id: int):
    campaign = campaign_service.get_campaign_by_id(campaign_id)
    if not campaign:
        raise HTTPException(status_code=404, detail="Campaña no encontrada")
    return campaign


@router.get("/featured", response_model=List[FeaturedCampaignResponse])
def get_featured_campaigns():
    return campaign_service.get_featured_campaigns()


@router.get("/upcoming", response_model=List[UpcomingCampaignResponse])
def get_upcoming_campaigns():
    return campaign_service.get_upcoming_campaigns()
