from rest_framework import viewsets
from .models import Vendor, Contact, Contract, Document
from .serializers import VendorSerializer, ContactSerializer, ContractSerializer, DocumentSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework import filters

class VendorViewSet(viewsets.ModelViewSet):
    queryset = Vendor.objects.prefetch_related('contacts', 'contract', 'documents')
    serializer_class = VendorSerializer


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['escalation_level', 'name']
    ordering = ['escalation_level']  # Default: Level 1 to Level 4


class ContractViewSet(viewsets.ModelViewSet):
    queryset = Contract.objects.all()
    serializer_class = ContractSerializer
    lookup_field = 'contract_number'
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['vendor__name', 'contract_number']
    ordering_fields = ['contract_start_date', 'contract_expiry_date']


class DocumentViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer

class VendorDetailView(RetrieveAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer