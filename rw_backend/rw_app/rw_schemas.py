from typing import List
from pydantic import BaseModel, Field


class RWGenerateRequest(BaseModel):
    topic: str = Field(..., description="Content topic or niche, e.g. 'toy shop'")
    description: str | None = None
    platform: str = Field(..., description="tiktok / instagram")
    tone: str = Field(..., description="funny / motivational / dramatic")
    media_filename: str | None = Field(
        None, description="Optional uploaded media filename (image/video)"
    )


class RWCaptionItem(BaseModel):
    text: str
    index: int


class RWGenerateResponse(BaseModel):
    captions: List[RWCaptionItem]
    hashtags: List[str]
