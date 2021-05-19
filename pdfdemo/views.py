from django.shortcuts import render
from django.conf import settings
from django_renderpdf.views import PDFView
from django.views.generic import DetailView
# Create your views here.
from .models import Product


def home(request):
    products = Product.objects.all()
    return render(request, 'pdfdemo/index.html', {"products": products})


class TestPDFView(PDFView):
    """Generate labels for some Shipments.

    A PDFView behaves pretty much like a TemplateView, so you can treat it as such.
    """
    template_name = 'pdfdemo/report.html'

    def get_context_data(self, *args, **kwargs):
        """Pass some extra context to the template."""
        context = super().get_context_data(*args, **kwargs)
        comp_info = {
            "company_name": "Patrick's Company",
            "address": "Lusaka, Zambia",
            "items": [
                {"name": "shoe", "price": 200},
                {"name": "trouser", "price": 200},
                {"name": "shirt", "price": 200},
            ]
        }

        context['comp_info'] = comp_info
        return context
