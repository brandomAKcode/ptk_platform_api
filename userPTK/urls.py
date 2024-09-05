from django.urls import path
from . import views

urlpatterns = [
    path('dealer-list/', views.UserDealerList.as_view()),
    path('user-token-access-valid/', views.UserTokenAccessValid.as_view()),
]