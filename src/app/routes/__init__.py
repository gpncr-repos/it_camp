import requests
from fastapi import APIRouter

from src.app.models.models import (NodalCalcResponse, VlpIprCalcResponse,
                                   WellModelCalcRequest, WellModelCalcResponse)
from src.app.routes.request_formers import (form_ipr_request,
                                            form_nodal_request,
                                            form_vlp_request)

main_router = APIRouter(prefix="/well_model", tags=["WellModel"])


@main_router.put("/calc", response_model=WellModelCalcResponse)
async def my_profile(data: WellModelCalcRequest):
    well_model_request = WellModelCalcRequest.parse_obj(data.dict())

    vlp_request = form_vlp_request(well_model_request)
    ipr_request = form_ipr_request(well_model_request)

    vlp_response = VlpIprCalcResponse.parse_obj(
        requests.post("http://localhost:8001/vlp/calc",
                      json=vlp_request).json())
    ipr_response = VlpIprCalcResponse.parse_obj(
        requests.post("http://localhost:8002/ipr/calc",
                      json=ipr_request).json())

    nodal_request = form_nodal_request(vlp_response, ipr_response)

    nodal_response = NodalCalcResponse.parse_obj(
        requests.post("http://localhost:8003/nodal/calc",
                      json=nodal_request).json())

    result = WellModelCalcResponse(vlp=vlp_response,
                                   ipr=ipr_response,
                                   nodal=nodal_response)

    return result
