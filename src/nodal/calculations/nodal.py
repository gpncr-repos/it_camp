import numpy as np
from shapely.geometry import LineString


def calc_nodal(vlp: dict, ipr: dict):
    first_line = LineString(np.column_stack((ipr["q_liq"], ipr["p_wf"])))
    second_line = LineString(np.column_stack((vlp["q_liq"], vlp["p_wf"])))
    try:
        intersection = first_line.intersection(second_line)
    except:  # noqa
        first_line = first_line.buffer(0)
        intersection = first_line.intersection(second_line)
    if intersection.type == "MultiPoint":
        results = [{"q_liq": p.x, "p_wf": p.y} for p in intersection]
        return results[-1]
    try:
        x, y = intersection.xy
        return [{"q_liq": x[0], "p_wf": y[0]}]
    except (NotImplementedError, AttributeError):
        return None, None


if __name__ == '__main__':
    import json

    with open("../../../contracts/nodal_in.json") as f:
        data = json.load(f)
    results = calc_nodal(**data)
    print(results)
