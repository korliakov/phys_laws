from django.shortcuts import render
from django.core.cache import cache
from . import laws_handler


def index(request):
    return render(request, "index.html")

def laws_list(request):
    laws = laws_handler.get_laws()
    return render(request, "laws_list.html", context={"laws": laws})
    # return render(request, "laws_list.html")