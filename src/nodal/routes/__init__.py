from fastapi import APIRouter

from nodal.calculations.nodal import calc_nodal
from nodal.models.models import NodalCalcRequest, NodalCalcResponse

main_router = APIRouter(prefix="/nodal", tags=["NodalAnalysis"])


@main_router.post("/calc", response_model=NodalCalcResponse)
async def my_profile(data: NodalCalcRequest):
    result = NodalCalcResponse.parse_obj(calc_nodal(**data.dict()))
    return result