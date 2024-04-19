from fastapi import APIRouter, Depends

from komodo.server.globals import get_appliance_runtime

router = APIRouter(
    prefix='/api/v1/user',
    tags=['User']
)


@router.get("/profile", response_model=dict, summary="Get user profile.", description="Get user profile.")
async def get_user_profile(runtime=Depends(get_appliance_runtime)):
    if not runtime or not runtime.user:
        return {"error": "User not found."}

    appliance = runtime.appliance
    user = runtime.user
    return appliance.get_user_profile(user)
