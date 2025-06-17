from rest_framework import serializers
from .models import Vendor, Contract, Service, Contact, Document

def get_diff_fields(obj):
    if obj.prev_record:
        return {
            field.name: {
                'from': getattr(obj.prev_record, field.name, None),
                'to': getattr(obj, field.name, None)
            }
            for field in obj._meta.fields
            if getattr(obj.prev_record, field.name, None) != getattr(obj, field.name, None)
        }
    return {}


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


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ['id', 'vendor', 'name', 'shortcode', 'revenue_share']
        extra_kwargs = {'vendor': {'write_only': True}}


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
    services = ServiceSerializer(many=True, read_only=True)
    contract = ContractSerializer(read_only=True)
    documents = DocumentSerializer(many=True, read_only=True)

    class Meta:
        model = Vendor
        fields = [
            'id', 'name', 'description', 'emails',
            'contacts', 'services', 'contract', 'documents'
        ]


from rest_framework import serializers
from simple_history.utils import get_history_model_for_model
from .models import Vendor, Contract, Service, Contact, Document

HistoricalVendor = get_history_model_for_model(Vendor)

class VendorHistorySerializer(serializers.ModelSerializer):
    changed_fields = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = HistoricalVendor
        fields = [
            'id', 'history_id', 'history_date', 'history_user', 'history_type',
            'user', 'changed_fields',
            'name', 'description', 'emails',
        ]

    def get_user(self, obj):
        return getattr(obj.history_user, 'username', None)

    def get_changed_fields(self, obj):
        if obj.prev_record:
            return {
                field.name: {'from': getattr(obj.prev_record, field.name), 'to': getattr(obj, field.name)}
                for field in obj._meta.fields
                if getattr(obj.prev_record, field.name) != getattr(obj, field.name)
            }
        return {}

HistoricalContract = get_history_model_for_model(Contract)

class ContractHistorySerializer(serializers.ModelSerializer):
    changed_fields = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = HistoricalContract
        fields = [
            'contract_number', 'history_id', 'history_date', 'history_user', 'history_type',
            'user', 'changed_fields',
            'vendor', 'contract_start_date', 'contract_expiry_date',
            'contract_currency', 'contract_terms',
        ]

    def get_user(self, obj):
        return getattr(obj.history_user, 'username', None)

    def get_changed_fields(self, obj):
        if obj.prev_record:
            return {
                field.name: {'from': getattr(obj.prev_record, field.name), 'to': getattr(obj, field.name)}
                for field in obj._meta.fields
                if getattr(obj.prev_record, field.name) != getattr(obj, field.name)
            }
        return {}


HistoricalService = get_history_model_for_model(Service)

class ServiceHistorySerializer(serializers.ModelSerializer):
    changed_fields = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = HistoricalService
        fields = [
            'id', 'history_id', 'history_date', 'history_user', 'history_type',
            'user', 'changed_fields',
            'vendor', 'name', 'shortcode', 'revenue_share',
        ]

    def get_user(self, obj):
        return getattr(obj.history_user, 'username', None)

    def get_changed_fields(self, obj):
        if obj.prev_record:
            return {
                field.name: {'from': getattr(obj.prev_record, field.name), 'to': getattr(obj, field.name)}
                for field in obj._meta.fields
                if getattr(obj.prev_record, field.name) != getattr(obj, field.name)
            }
        return {}


HistoricalContact = get_history_model_for_model(Contact)

class ContactHistorySerializer(serializers.ModelSerializer):
    changed_fields = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = HistoricalContact
        fields = [
            'id', 'history_id', 'history_date', 'history_user', 'history_type',
            'user', 'changed_fields',
            'vendor', 'name', 'position', 'phone_numbers', 'email', 'escalation_level',
        ]

    def get_user(self, obj):
        return getattr(obj.history_user, 'username', None)

    def get_changed_fields(self, obj):
        if obj.prev_record:
            return {
                field.name: {'from': getattr(obj.prev_record, field.name), 'to': getattr(obj, field.name)}
                for field in obj._meta.fields
                if getattr(obj.prev_record, field.name) != getattr(obj, field.name)
            }
        return {}


HistoricalDocument = get_history_model_for_model(Document)

class DocumentHistorySerializer(serializers.ModelSerializer):
    changed_fields = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:
        model = HistoricalDocument
        fields = [
            'id', 'history_id', 'history_date', 'history_user', 'history_type',
            'user', 'changed_fields',
            'vendor', 'file', 'uploaded_at',
        ]

    def get_user(self, obj):
        return getattr(obj.history_user, 'username', None)

    def get_changed_fields(self, obj):
        if obj.prev_record:
            return {
                field.name: {'from': getattr(obj.prev_record, field.name), 'to': getattr(obj, field.name)}
                for field in obj._meta.fields
                if getattr(obj.prev_record, field.name) != getattr(obj, field.name)
            }
        return {}


