from django.urls import path
from .views  import  *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import views as auth_views
app_name="core_app"
urlpatterns = [
    path('login/',auth_views.LoginView.as_view(template_name="core_app/login.html",redirect_authenticated_user=True),name='Login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="core_app/logout.html"),name='Logout'),
    path('',login_required(index),name='Index'),
    path('candidato/add/',login_required(CandidatoCreate.as_view()),name='Add_Candidato'),
    path('candidato/up/<int:pk>/', login_required(CandidatoUpdateView.as_view()), name='Update_Candidato'),
    path('candidato/del/<int:pk>/', login_required(CandidatoDeleteView.as_view()), name='Delete_Candidato'),
]
