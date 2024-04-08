from django.urls import path
from . import views
urlpatterns = [
    path("",views.get_routes),
    path("developers/",views.get_developers),
    path("developers/<int:id>/",views.get_developer)
]
