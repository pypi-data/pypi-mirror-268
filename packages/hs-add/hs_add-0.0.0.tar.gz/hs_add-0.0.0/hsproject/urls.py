from django.urls import path, include
# from django.views.static import serve
# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('system/', include("system.urls")),
]
