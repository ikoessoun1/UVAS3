from rest_framework import serializers
from .models import Vendor, Contract, Contact, Document


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'vendor', 'file', 'uploaded_at']
        extra_kwargs = {'vendor': {'write_only': True}}


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id',
            'vendor',
            'name',
            'position',
            'phone_numbers',
            'email',
            'escalation_level',
        ]
        extra_kwargs = {
            'vendor': {'write_only': True},
            'position': {'required': False, 'allow_null': True, 'allow_blank': True},
            'phone_numbers': {'required': False, 'allow_null': True, 'allow_blank': True},
        }




class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'contract_number', 'vendor',
            'contract_start_date', 'contract_expiry_date',
            'contract_currency', 'contract_terms'
        ]
        extra_kwargs = {
            'vendor': {'write_only': False}
        }


class VendorSerializer(serializers.ModelSerializer):
    # Nested relationships (read-only)
    contacts = ContactSerializer(many=True, read_only=True)
    contract = ContractSerializer(read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = [
            'id', 'name', 'description', 'emails',
            'contacts', 'contract', 'documents'
        ]
