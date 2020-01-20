from django.http import HttpResponse, JsonResponse
from pkg_resources import working_set
import re, json

def index(request):
    """
    API endpoint that presents all installed .
    """
    dists = [d for d in working_set]
    dist_list = []
    pattern = "(\w+)(\s)(...+)"
    for d in dists:
        mod = {
            "name":"",
            "version":"",
        }
        result = re.match(pattern, str(d))
        mod['name'] = result[1]
        mod['version'] = result[3]
        dist_list.append(mod)

    return JsonResponse(dist_list, safe=False)
