from pydantic import BaseModel
from typing import Optional
from datetime import datetime, date


class CampaignBase(BaseModel):
    title: str
    description: str
    start_date: date
    end_date: date
    image_url: Optional[str] = None
    is_featured: bool = False
    location: Optional[str] = None
    requirements: Optional[str] = None


class CampaignCreate(CampaignBase):
    pass


class CampaignUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None
    image_url: Optional[str] = None
    is_featured: Optional[bool] = None
    location: Optional[str] = None
    requirements: Optional[str] = None


class CampaignResponse(CampaignBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class FeaturedCampaignResponse(BaseModel):
    id: int
    title: str
    description: str
    image_url: Optional[str] = None
    start_date: date

    class Config:
        from_attributes = True


class UpcomingCampaignResponse(BaseModel):
    id: int
    title: str
    description: str
    start_date: date
    image_url: Optional[str] = None

    class Config:
        from_attributes = True
