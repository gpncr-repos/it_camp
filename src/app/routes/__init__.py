from fastapi import APIRouter

from src.app.models.models import WellModelCalcRequest, WellModelCalcResponse

main_router = APIRouter(prefix="/well_model", tags=["WellModel"])


@main_router.put("/calc", response_model=WellModelCalcResponse)
async def my_profile(data: WellModelCalcRequest):
    result = WellModelCalcResponse.parse_obj({
        "vlp": {
            "q_liq": [0, 30, 60, 90, 120, 150],
            "p_wf": [200, 190, 180, 175, 185, 200]
        },
        "ipr": {
            "q_liq": [0, 30, 60, 90, 120, 150],
            "p_wf": [200, 180, 160, 140, 120, 100]
        },
        "nodal": [{
            "p_wf": 150,
            "q_liq": 100
        }, {
            "p_wf": 160,
            "q_liq": 90
        }]
    })
    return result
