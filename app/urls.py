from django.urls import path
from . import views

urlpatterns = [     # to hover through the webpages
    path("", views.page_home, name="home-page-api-auth"),
    path("page1/", views.page_1, name="page-1"),
    path("page2/", views.page_2, name="page-2")
]
