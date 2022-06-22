from typing import Any, Dict
from django.http import HttpResponse
from django.views.generic import TemplateView

from predictions.ml_model import predict_if_will_win


class HomeView(TemplateView):
    template_name = "predictions/home.html"

class ResultView(TemplateView):
    template_name = "predictions/result.html"
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context_data = super().get_context_data(**kwargs)
        context_data["will_win"] = predict_if_will_win(request_data=self.request.GET)
        return context_data
