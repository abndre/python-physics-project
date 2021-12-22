from fastapi import APIRouter
from funcoes import calc_speed_mean
router = APIRouter()


@router.get("/speed")
async def speed(x2: float,
                x1: float,
                t2: float,
                t1: float):
    speed_value = calc_speed_mean(x2, x1, t2, t1)
    return {
        "speed mean": speed_value
    }
