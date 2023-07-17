
from django.views.generic import TemplateView


class HomeGalleryView(TemplateView):
    template_name = 'home.html'


class AboutPageView(TemplateView):  # new
    template_name = 'about.html'
