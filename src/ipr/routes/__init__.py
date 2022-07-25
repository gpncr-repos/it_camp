from fastapi import APIRouter

from ipr.calculations.vogel_ipr import calc_ipr
from ipr.models.models import IprCalcRequest, IprCalcResponse

main_router = APIRouter(prefix="/ipr", tags=["IPR"])


@main_router.post("/calc", response_model=IprCalcResponse)
async def my_profile(ipr_in: IprCalcRequest):
    result = IprCalcResponse.parse_obj(calc_ipr(**ipr_in.dict()))
    return result
