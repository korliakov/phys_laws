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

def add_law(request):
    return render(request, "law_add.html")

def send_law(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_law = request.POST.get("new_law", "")
        new_area = request.POST.get("new_area", "")
        new_formula = request.POST.get("new_formula", "")
        new_definition = request.POST.get("new_definition", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_definition) == 0:
            context["success"] = False
            context["comment"] = "Формулировка должна быть не пустой"
        elif len(new_law) == 0:
            context["success"] = False
            context["comment"] = "Название должно быть не пустым"
        elif len(new_formula) == 0:
            context["success"] = False
            context["comment"] = "Должна быть формула или прочерк"
        elif len(new_area) == 0:
            context["success"] = False
            context["comment"] = "Раздел должен быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Закон принят"
            laws_handler.write_law(new_law, new_definition, new_formula, new_area)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "law_request.html", context)
    else:
        add_law(request)


def add_error(request):
    return render(request, "error_add.html")

def send_error(request):
    if request.method == "POST":
        cache.clear()
        user_mail = request.POST.get("mail")
        new_law = request.POST.get("new_law", "")
        new_description = request.POST.get("new_description", "").replace(";", ",")
        context = {"user": user_mail}
        if len(new_description) == 0:
            context["success"] = False
            context["comment"] = "Описание должно быть не пустым"
        elif len(new_law) == 0:
            context["success"] = False
            context["comment"] = "Название должно быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Закон принят"
            laws_handler.write_error(new_law, new_description, user_mail)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "error_request.html", context)
    else:
        add_error(request)
