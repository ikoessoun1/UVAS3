from rest_framework import serializers
from .models import Vendor, Contact, Contract, Document, Department


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = [
            'id', 'vendor', 'name', 'position',
            'phone_numbers', 'email', 'escalation_level'
        ]
        extra_kwargs = {'vendor': {'write_only': True}}


class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = [
            'contract_number', 'vendor', 'contract_start_date',
            'contract_expiry_date', 'contract_currency',
            'contract_terms', 'contract_value', 'novation_status'
        ]
        extra_kwargs = {'vendor': {'write_only': True}}


class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'vendor', 'file', 'uploaded_at']
        extra_kwargs = {'vendor': {'write_only': True}}

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = ['id', 'name']
        
# --- Vendor Serializer (includes department) ---
class VendorSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(
        queryset=Department.objects.all(),
        source='department',
        write_only=True,
        required=False
    )

    contacts = ContactSerializer(many=True, read_only=True)
    contract = ContractSerializer(read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = [
            'id', 'name', 'description', 'payment_terms',
            'department', 'department_id', 'emails',
            'contacts', 'contract', 'documents'
        ]


