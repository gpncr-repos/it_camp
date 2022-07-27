from test_app.models.models import (PVT, IprCalcRequest, NodalCalcRequest,
                                    VlpCalcRequest)


def form_vlp_request(well_model_request):
    pvt = well_model_request.pvt.dict()
    pvt.pop("pb")
    request = VlpCalcRequest(inclinometry=well_model_request.inclinometry,
                             casing=well_model_request.casing,
                             tubing=well_model_request.tubing,
                             pvt=PVT(**pvt),
                             p_wh=well_model_request.p_wh,
                             geo_grad=well_model_request.geo_grad,
                             h_res=well_model_request.h_res).dict()
    return request


def form_ipr_request(well_model_request):
    request = IprCalcRequest(p_res=well_model_request.p_res,
                             wct=well_model_request.pvt.wct,
                             pi=well_model_request.pi,
                             pb=well_model_request.pvt.pb).dict()
    return request


def form_nodal_request(vlp_result, ipr_result):
    request = NodalCalcRequest(vlp=vlp_result, ipr=ipr_result).dict()

    return request
