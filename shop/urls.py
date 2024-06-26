from django.urls import path
from . import views

urlpatterns=[
    path("register/",views.RegisterAPI.as_view()),
    path('login/', views.LoginView.as_view()),
    path('product/', views.ProductView.as_view()),
      path('product/<int:pk>/', views.ProductDetailView.as_view()),
]
