from django.shortcuts import render

from pricing import calculate_tour
from .forms import TourForm


def calculator_page(request):
    form = TourForm(request.POST or None)
    result = None

    if request.method == "POST" and form.is_valid():
        result = calculate_tour(form.cleaned_data)

    return render(request, "calculator/index.html", {"form": form, "result": result})
