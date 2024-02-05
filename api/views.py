from django.shortcuts import render
from .models import BankState
from .serializers import BankStateSerializer
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import permission_classes

# Create your views here.
@permission_classes([permissions.IsAuthenticated, permissions.DjangoModelPermissions])
class BankStateViewSet(viewsets.ModelViewSet):
    queryset = BankState.objects.all()
    serializer_class = BankStateSerializer
    template_name = None  # Ensure no template is used
    permission_classes = [permissions.IsAuthenticated]
    
    def list(self, request, *args, **kwargs):
        if request.user.groups.filter(name = 'account').exists() and request.user.user_permissions.filter(codename='view_bankstate').exists():
            data = list(BankState.objects.all().values())
            return Response(data)
        else:
            return Response('You are not allowed to view this datas')
 

    def retrieve(self, request, *args, **kwargs):
        if request.user.groups.filter(name = 'account').exists() and request.user.user_permissions.filter(codename='view_bankstate').exists():
            data = list(BankState.objects.filter(id=kwargs['pk']).values())
            return Response(data)
        else:
            return Response('You are not allowed to get datas')
    

    def create(self, request, *args, **kwargs):
        if request.user.groups.filter(name = 'account').exists() and request.user.user_permissions.filter(codename='add_bankstate').exists():
            product_serializer_data = BankStateSerializer(data=request.data)
            if product_serializer_data.is_valid():
                product_serializer_data.save()
                status_code = status.HTTP_201_CREATED
                return Response({"message": "Product Added Sucessfully", "status": status_code})
            else:
                status_code = status.HTTP_400_BAD_REQUEST
                return Response({"message": "please fill the datails", "status": status_code})
        else:
            return Response({"message": "please fill the datails", "status": status_code})
    
    def destroy(self, request, *args, **kwargs):
        product_data = BankState.objects.filter(id=kwargs['pk'])
        if product_data:
            product_data.delete()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product delete Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data not found", "status": status_code})
    
    def update(self, request, *args, **kwargs):
        product_details = BankState.objects.get(id=kwargs['pk'])
        product_serializer_data = BankStateSerializer(
            product_details, data=request.data, partial=True)
        if product_serializer_data.is_valid():
            product_serializer_data.save()
            status_code = status.HTTP_201_CREATED
            return Response({"message": "Product Update Sucessfully", "status": status_code})
        else:
            status_code = status.HTTP_400_BAD_REQUEST
            return Response({"message": "Product data Not found", "status": status_code})
