from django.urls import path

from family.views import family



urlpatterns = [
    path('', family, name = 'family')

]