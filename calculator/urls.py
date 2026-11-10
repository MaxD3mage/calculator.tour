from django.urls import path

from .views import calculator_page

urlpatterns = [path("", calculator_page, name="calculator")]
