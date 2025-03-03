from django.urls import path, include
from . import views
from .ClassViews import FirstPageView, SecondPageView

urlpatterns = [
    path('test', views.index, name="main"),
    path('', FirstPageView.as_view(), name="firstpage"),
    # path('<str:name>', views.shorts, name="shorturl"),
    path('<str:name>', SecondPageView.as_view(), name="shorturl"),
]