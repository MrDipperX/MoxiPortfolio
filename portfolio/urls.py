from django.urls import path, include

from portfolio.views import *

urlpatterns = [
    path('', PortfolioHome.as_view(), name="home"),
    path('details/<slug:theme_slug>/', PortfolioDetail.as_view(), name="details")
]


