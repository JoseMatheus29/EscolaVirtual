from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'pages'

urlpatterns = [
    path('', views.HomePageView.as_view(), name = 'home'),
    path('cursos', views.CursoPage.as_view(), name = 'cursos'),
    path('sobre/', views.SobrePage.as_view(), name ='sobre')
]