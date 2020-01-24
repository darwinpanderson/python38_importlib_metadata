from django.http import HttpResponse, JsonResponse
import re, json, pkgutil, importlib.metadata

def index(request):
    """
    API endpoint that presents all endpoints.
    """
    endpoints = [
        {
            "endpoint":"list/",
            "desc":"Lists valid packages installed via Django",
            "parameters":"none"
        },{
            "endpoint":"list/<package>",
            "desc":"Lists all details of supplied package",
            "parameters":"package"
        }
    ]

    return JsonResponse(endpoints, safe=False)

def listpkg(request,package=None):
    """
    Lists all valid packages installed.
    """
    dist_list = getpackages(package)
    return JsonResponse(dist_list, safe=False)

def getpackages(package=None):
    """
    Helper function, returns a list of packages. 
    """
    dist_list = []
    if package:
        pkgi = getpackageinfo(package)
        dist_list.append(pkgi)
    else:
        pattern="ModuleInfo\(module_finder=FileFinder\([0-9a-zA-Z'\/\-\_\.\/]+\), name='([\w]+)', ispkg=True\)"
        for p in pkgutil.iter_modules():
            result = re.match(pattern, str(p))
            if result:
                try:
                    pkgi = getpackageinfo(result[1])
                    dist_list.append(pkgi)
                except:
                    pass              
    return dist_list

def getpackageinfo(package):
    pkgi = {}
    pkgi['name'] = package
    pkgi['version'] = importlib.metadata.version(package)
    try:
        md_list = []
        md = {}
        for i in importlib.metadata.metadata(package).items():
            md[i[0]] = i[1]
        pkgi['metadata'] = md
    except Exception as e:
        pkgi['metadata'] = str(e)
    return pkgi