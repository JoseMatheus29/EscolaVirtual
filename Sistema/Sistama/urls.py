from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    #url admin
    path('admin/', admin.site.urls),
    #url accounts
    path('accounts/', include("allauth.urls")),
    #local
    path("", include("pages.urls", namespace="pages")),
]
