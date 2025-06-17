from django.shortcuts import render

# Create your views here.
# legal/views.py
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from scm_vendors.models import Vendor as SCMVendor, Contract as SCMContract, Contact as SCMContact, Document as SCMDocument
from vas_vendors.models import Vendor as VASVendor, Contract as VASContract, Contact as VASContact, Document as VASDocument
from idd_vendors.models import Vendor as IDDVendor, Contract as IDDContract, Contact as IDDContact, Document as IDDDocument

from scm_vendors.serializers import VendorSerializer as SCMVendorSerializer, ContractSerializer as SCMContractSerializer, ContactSerializer as SCMContactSerializer, DocumentSerializer as SCMDocumentSerializer
from vas_vendors.serializers import VendorSerializer as VASVendorSerializer, ContractSerializer as VASContractSerializer, ContactSerializer as VASContactSerializer, DocumentSerializer as VASDocumentSerializer
from idd_vendors.serializers import VendorSerializer as IDDVendorSerializer, ContractSerializer as IDDContractSerializer, ContactSerializer as IDDContactSerializer, DocumentSerializer as IDDDocumentSerializer

class LegalSCMVendorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SCMVendor.objects.all()
    serializer_class = SCMVendorSerializer

class LegalSCMContractViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SCMContract.objects.all()
    serializer_class = SCMContractSerializer
    # permission_classes = [IsAuthenticated]
    # permission_classes = [IsAuthenticated]

class LegalSCMContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SCMContact.objects.all()
    serializer_class = SCMContactSerializer
    # permission_classes = [IsAuthenticated]

class LegalSCMDocumentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = SCMDocument.objects.all()
    serializer_class = SCMDocumentSerializer
    # permission_classes = [IsAuthenticated]

class LegalVASVendorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VASVendor.objects.all()
    serializer_class = VASVendorSerializer
    # permission_classes = [IsAuthenticated]

class LegalVASContractViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VASContract.objects.all()
    serializer_class = VASContractSerializer
    # permission_classes = [IsAuthenticated]

class LegalVASContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VASContact.objects.all()
    serializer_class = VASContactSerializer
    # permission_classes = [IsAuthenticated]

class LegalVASDocumentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = VASDocument.objects.all()
    serializer_class = VASDocumentSerializer
    # permission_classes = [IsAuthenticated]

class LegalIDDVendorViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = IDDVendor.objects.all()
    serializer_class = IDDVendorSerializer
    # permission_classes = [IsAuthenticated]

class LegalIDDContractViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = IDDContract.objects.all()
    serializer_class = IDDContractSerializer
    # permission_classes = [IsAuthenticated]

class LegalIDDContactViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = IDDContact.objects.all()
    serializer_class = IDDContactSerializer
    # permission_classes = [IsAuthenticated]

class LegalIDDDocumentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = IDDDocument.objects.all()
    serializer_class = IDDDocumentSerializer
    # permission_classes = [IsAuthenticated]


