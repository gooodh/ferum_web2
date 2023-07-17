
from django.urls import path
from .views import HomeGalleryView, AboutPageView


urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),  # new
    path('', HomeGalleryView.as_view(), name='home'),
]
