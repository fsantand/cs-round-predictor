from django.urls import path
from predictions.views import HomeView, ResultView

app_name = "predictions"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("results", ResultView.as_view(), name="results"),
]