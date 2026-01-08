from fastapi import APIRouter, File, Form, UploadFile, HTTPException
from openai import OpenAI
import json

from .rw_schemas import RWGenerateRequest, RWGenerateResponse, RWCaptionItem
from .rw_config import settings

router = APIRouter(prefix="/generate", tags=["generate"])

# OpenAI client
client = OpenAI(api_key=settings.openai_api_key) if settings.openai_api_key else None

SYSTEM_PROMPT = """
You are ReelWriter AI, a caption generator for short-form videos.
Always respond ONLY with valid JSON in the following format:

{
  "captions": [
    {"text": "main caption text", "index": 1},
    {"text": "alternative caption text", "index": 2},
    {"text": "third caption text", "index": 3}
  ],
  "hashtags": ["#tag1", "#tag2", "#tag3"]
}

Do NOT include explanations, prose, or markdown.
Only return pure JSON.
"""


@router.post("", response_model=RWGenerateResponse)
async def generate_captions(
    topic: str = Form(...),
    description: str | None = Form(None),
    platform: str = Form(...),
    tone: str = Form(...),
    media: UploadFile | None = File(None),
) -> RWGenerateResponse:

        

    payload = RWGenerateRequest(
        topic=topic,
        description=description,
        platform=platform,
        tone=tone,
        media_filename=media.filename if media else None,
    )

    # Debug ლოგი — payload
    print("RW DEBUG payload:", payload.model_dump())

    user_prompt = f"""
Generate social-media caption suggestions and hashtags.

Topic: {payload.topic}
Platform: {payload.platform}
Tone: {payload.tone}
Description: {payload.description or "—"}
Media filename: {payload.media_filename or "no media"}

Return ONLY JSON.
"""

    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": user_prompt},
            ],
            response_format={"type": "json_object"},
            temperature=0.9,
        )

        content = completion.choices[0].message.content
        if not content:
            raise ValueError("Empty response from OpenAI")

        # Debug ლოგი — خام JSON
        print("RW DEBUG raw OpenAI content:", content)

        data = json.loads(content)

        captions_list = [
            RWCaptionItem(text=item["text"], index=item.get("index", i + 1))
            for i, item in enumerate(data.get("captions", []))
        ]

        return RWGenerateResponse(
            captions=captions_list,
            hashtags=data.get("hashtags", []),
        )

    except Exception as e:
        print("OpenAI error:", repr(e))
        raise HTTPException(
            status_code=500,
            detail="Failed to generate captions with OpenAI.",
        )
