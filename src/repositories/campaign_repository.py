from datetime import date
from typing import Optional, List
from src.schemas.campaign import (
    CampaignCreate,
    CampaignUpdate,
    CampaignResponse,
    FeaturedCampaignResponse,
    UpcomingCampaignResponse,
)


class CampaignRepository:
    def __init__(self):
        self._campaigns: List[dict] = []
        self._next_id = 1
        self._seed_data()

    def _seed_data(self):
        campaigns = [
            {
                "title": "Vacunación Infantil",
                "description": "Campaña de vacunación para niños de 0-5 años",
                "start_date": date(2026, 3, 1),
                "end_date": date(2026, 3, 31),
                "is_featured": True,
                "location": "Centro de Salud",
            },
            {
                "title": "Detección de Diabetes",
                "description": "Campaña gratuita de detección de diabetes",
                "start_date": date(2026, 2, 15),
                "end_date": date(2026, 2, 28),
                "is_featured": False,
                "location": "Laboratorio Central",
            },
            {
                "title": "Chequeo Cardiovascular",
                "description": "Chequeos cardíacos gratuitos para mayores de 40 años",
                "start_date": date(2026, 4, 1),
                "end_date": date(2026, 4, 15),
                "is_featured": True,
                "location": "Área de Cardiología",
            },
        ]
        for camp in campaigns:
            self._campaigns.append(
                {
                    "id": self._next_id,
                    **camp,
                    "image_url": None,
                    "requirements": None,
                    "created_at": date.today(),
                }
            )
            self._next_id += 1

    def get_all(self) -> List[CampaignResponse]:
        return [CampaignResponse(**c) for c in self._campaigns]

    def get_by_id(self, campaign_id: int) -> Optional[CampaignResponse]:
        for camp in self._campaigns:
            if camp["id"] == campaign_id:
                return CampaignResponse(**camp)
        return None

    def get_featured(self) -> List[FeaturedCampaignResponse]:
        featured = [c for c in self._campaigns if c["is_featured"]]
        return [
            FeaturedCampaignResponse(
                **{
                    k: v
                    for k, v in c.items()
                    if k != "is_featured"
                    and k != "end_date"
                    and k != "requirements"
                    and k != "location"
                }
            )
            for c in featured
        ]

    def get_upcoming(self) -> List[UpcomingCampaignResponse]:
        today = date.today()
        upcoming = [c for c in self._campaigns if c["start_date"] > today]
        return [
            UpcomingCampaignResponse(
                **{
                    k: v
                    for k, v in c.items()
                    if k in ["id", "title", "description", "start_date", "image_url"]
                }
            )
            for c in upcoming
        ]


campaign_repo = CampaignRepository()
