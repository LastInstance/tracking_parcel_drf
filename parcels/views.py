from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Address, Parcel
from .serializers import AddressSerializer, ParcelSerializer

class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer

class ParcelViewSet(viewsets.ModelViewSet):
    queryset = Parcel.objects.all()
    serializer_class = ParcelSerializer

    @action(detail=False, methods=['post'])
    def check_address(self, request):
        recipient_address = request.data.get('recipient_address')
        address_exists = Address.objects.filter(address=recipient_address).exists()
        if address_exists:
            return Response({'status': 'Address exists'})
        else:
            return Response({'status': 'Address does not exists'})

    @action(detail=True, methods=['put'])
    def change_status(self, request, pk=None):
        parcel = self.get_object()
        new_status = request.data.get('status')

        if new_status:
            parcel_status = new_status
            parcel.save()
            return Response({'status': 'Parcel status updated'})
        else:
            return Responce({'error': 'Invalid status'})

    @action(detail=True, methods=['get'])
    def check_status(self, request, pk=None):
        parcel = self.get_object()
        return Responce({'status': parcel.status})







