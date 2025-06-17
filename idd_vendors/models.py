from django.db import models
import uuid
from django.utils.text import slugify
import os
from django.utils.timezone import now
from simple_history.models import HistoricalRecords


class Vendor(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    emails = models.TextField(help_text="Comma-separated list of emails")

    history = HistoricalRecords()

    def __str__(self):
        return self.name



class Contract(models.Model):
    CURRENCY_CHOICES = [
        ('GHS', 'Ghana Cedis'),
        ('USD', 'US Dollars'),
    ]

    contract_number = models.CharField(
        max_length=100,
        primary_key=True,
        editable=False,
        unique=True
    )
    vendor = models.OneToOneField(
        Vendor,
        related_name='contract',
        on_delete=models.CASCADE
    )
    contract_start_date = models.DateField(null=True, blank=True)
    contract_expiry_date = models.DateField()
    contract_currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    contract_terms = models.TextField()

    history = HistoricalRecords()

    def save(self, *args, **kwargs):
        if not self.contract_number:
            vendor_slug = slugify(self.vendor.name).upper()
            self.contract_number = f"CTR-{vendor_slug}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Contract {self.contract_number} - {self.vendor.name}"

class Contact(models.Model):
    LEVEL_CHOICES = [
        (1, 'Level 1 Escalation'),
        (2, 'Level 2 Escalation'),
        (3, 'Level 3 Escalation'),
        (4, 'Level 4 Escalation'),
    ]

    vendor = models.ForeignKey(Vendor, related_name='contacts', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255, null=True, blank=True)
    phone_numbers = models.TextField(help_text="Comma-separated list of phone numbers", null=True, blank=True)
    email = models.EmailField(blank=True)
    escalation_level = models.PositiveSmallIntegerField(choices=LEVEL_CHOICES)

    history = HistoricalRecords()

    def __str__(self):
        return f"{self.name} ({self.position}) - {self.vendor.name}" if self.position else f"{self.name} - {self.vendor.name}"


def rename_uploaded_file(instance, filename):
    ext = filename.split('.')[-1]

    vendor_name = instance.vendor.name.replace(' ', '_').lower()
    vendor_id = instance.vendor.id
    date_str = now().strftime('%Y%m%d')  # Format: YYYYMMDD

    new_filename = f"{vendor_name}_id{vendor_id}_{date_str}.{ext}"
    return os.path.join('vendor_documents', vendor_name, new_filename)

class Document(models.Model):
    vendor = models.ForeignKey(Vendor, related_name='documents', on_delete=models.CASCADE)
    file = models.FileField(upload_to=rename_uploaded_file)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    history = HistoricalRecords()

    def __str__(self):
        return f"Document for {self.vendor.name}"

