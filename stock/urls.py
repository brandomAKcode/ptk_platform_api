from django.urls import path
from . import views

urlpatterns = [
    path('count-products-in-stock/', views.CountProductsInStock.as_view()),
    path('products-in-stock/', views.ProductsInStock.as_view()),
    path('rotation-list/', views.RotationList.as_view()),
    path('rotation-pending/', views.RotationPending.as_view()),
    path('rotation-update/', views.RotationUpdate.as_view()),
    path('rotation-detail/<int:id>/', views.RotationDetail.as_view()),
]
