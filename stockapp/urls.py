from django.urls import path
from . import views
app_name = 'stockapp'

urlpatterns = [
    path('', views.all_orders, name="all_orders"),
    path('all', views.ff),
    path('<int:id>', views.karton_datail, name="fatora"),
    path('prodect/<int:id>', views.prodect_datial, name="prodects"),
    path('new/<int:id>', views.fatora, name="fatoras")
]