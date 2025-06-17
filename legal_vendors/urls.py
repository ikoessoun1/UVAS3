from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    LegalSCMVendorViewSet, LegalSCMContractViewSet, LegalSCMContactViewSet, LegalSCMDocumentViewSet,
    LegalVASVendorViewSet, LegalVASContractViewSet, LegalVASContactViewSet, LegalVASDocumentViewSet,
   
    LegalIDDVendorViewSet, LegalIDDContractViewSet, LegalIDDContactViewSet, LegalIDDDocumentViewSet,
)

router = DefaultRouter()

# SCM Legal Routes
router.register(r'scm/vendors', LegalSCMVendorViewSet, basename='legal-scm-vendors')
router.register(r'scm/contracts', LegalSCMContractViewSet, basename='legal-scm-contracts')
router.register(r'scm/contacts', LegalSCMContactViewSet, basename='legal-scm-contacts')
router.register(r'scm/documents', LegalSCMDocumentViewSet, basename='legal-scm-documents')

# VAS Legal Routes
router.register(r'vas/vendors', LegalVASVendorViewSet, basename='legal-vas-vendors')
router.register(r'vas/contracts', LegalVASContractViewSet, basename='legal-vas-contracts')
router.register(r'vas/contacts', LegalVASContactViewSet, basename='legal-vas-contacts')
router.register(r'vas/documents', LegalVASDocumentViewSet, basename='legal-vas-documents')

# IDD Legal Routes
router.register(r'idd/vendors', LegalIDDVendorViewSet, basename='legal-idd-vendors')
router.register(r'idd/contracts', LegalIDDContractViewSet, basename='legal-idd-contracts')
router.register(r'idd/contacts', LegalIDDContactViewSet, basename='legal-idd-contacts')
router.register(r'idd/documents', LegalIDDDocumentViewSet, basename='legal-idd-documents')

urlpatterns = [
    path('', include(router.urls)),
]
