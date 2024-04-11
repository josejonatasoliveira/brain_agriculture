from rest_framework.response import Response
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from django.db.models import Sum, Count

from .models import Produtor
from .serializers import ProdutorSerializer, ProdutorRequest

class ProdutorListView(generics.ListCreateAPIView):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class ProdutorDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produtor.objects.all()
    serializer_class = ProdutorSerializer
    permission_classes = [permissions.IsAuthenticated]

@api_view(['GET'])
def get_dashboard_data(request):
    produtores = Produtor.objects.all()
    
    dash_data = {
        'qty_farm': 0,
        'total_area': 0
    }
    
    if not produtores:
        return Response(dash_data)
    
    dash_data['qty_farm'] = produtores.aggregate(qty=Count('farm_name'))["qty"]
    dash_data['total_area'] = produtores.aggregate(total_area=Sum("farm_total_area"))["total_area"]

    return Response(dash_data)
