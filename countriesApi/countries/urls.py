from django.urls import path
from countries import views

urlpatterns = [
        path('api/countries/', views.countries_list, name="countries_list"),
        path('api/countries/<int:pk>/', views.countries_detail, name="countries_detail"),

]
        
