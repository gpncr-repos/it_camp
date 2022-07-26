from calculations.vlp import calc_vlp
from fastapi import APIRouter
from models.models import VlpCalcRequest, VlpCalcResponse

main_router = APIRouter(prefix="/vlp", tags=["VLP"])


@main_router.post("/calc", response_model=VlpCalcResponse)
async def my_profile(vlp_in: VlpCalcRequest):
    result = VlpCalcResponse.parse_obj(calc_vlp(**vlp_in.dict()))
    return result
