from django.contrib import admin
from django.urls import path, include  # ✅ don't forget include!

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("helloapp.urls")),  # ✅ routes everything to helloapp
]
