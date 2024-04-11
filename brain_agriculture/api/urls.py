from django.urls import path
from . import views

urlpatterns = [
    path('produtors/', views.ProdutorListView.as_view(), name='produtor-list'),
    path('dash/', views.get_dashboard_data, name='get-dashboard-data'),
]