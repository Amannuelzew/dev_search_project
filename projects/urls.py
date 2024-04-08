from django.urls import path
from projects import views
from django.contrib.auth.decorators import login_required
urlpatterns = [
    path('', views.index,name="index"),
    path('projects', views.index,name="projects"),
   path('profile/', login_required(views.ProfileView.as_view()),name="profile"),

    path('signup/', views.signup_page,name="signup"),
    path('login/', views.login_page,name="login"),
    path('logout/', views.logout_page,name="logout"),
   
]


