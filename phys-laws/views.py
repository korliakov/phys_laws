from django.shortcuts import render
from django.core.cache import cache
from . import laws_handler
from django.template.defaulttags import register

@register.filter
def div(value, arg):
    try:
        return float(value) / float(arg)
    except (ValueError, ZeroDivisionError):
        return None

@register.filter
def multiply(value, arg):
    try:
        return float(value) * float(arg)
    except (ValueError, ZeroDivisionError):
        return None

def index(request):
    return render(request, "index.html")

def laws_list(request):
    laws = laws_handler.get_laws()
    return render(request, "laws_list.html", context={"laws": laws})

def statistics(request):
    stats = laws_handler.get_stats()
    return render(request, "stats.html", stats)