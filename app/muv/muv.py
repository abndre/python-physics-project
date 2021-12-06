from fastapi import APIRouter
router = APIRouter()


@router.get("/speed")
async def speed(x: float, time: float):
    speed_value = x / time
    return {
        "speed": speed_value
    }
