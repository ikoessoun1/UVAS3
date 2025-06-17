from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import VendorViewSet, ContactViewSet, ContractViewSet, DocumentViewSet, DepartmentViewSet

router = DefaultRouter()
router.register(r'vendors', VendorViewSet, basename='vendor')
router.register(r'contacts', ContactViewSet, basename='contact')
router.register(r'contracts', ContractViewSet, basename='contract')
router.register(r'documents', DocumentViewSet, basename='document')
router.register(r'departments', DepartmentViewSet, basename='department')

urlpatterns = [
    path('', include(router.urls)),
]
