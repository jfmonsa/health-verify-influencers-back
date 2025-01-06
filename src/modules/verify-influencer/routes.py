from fastapi import APIRouter

verify_influencer_router = APIRouter()


@verify_influencer_router.post("/verify")
async def verify_influencer():
    pass
