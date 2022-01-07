from django.contrib import admin
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse

from apps.models import Patient, Address, Subject, Message

# Register your models here.


class AdminURLMixin(object):
    def get_admin_url(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return reverse("admin:store_%s_change" % (
            content_type.model),
            args=(obj.id,))


class AddressInline(admin.StackedInline):
    model = Address
    extra = 0


class MessageInline(admin.StackedInline):
    model = Message
    extra = 0


# class SubjectInline(admin.StackedInline):
#     model = Subject
#     extra = 0
class SubjectInline(admin.StackedInline):
    model = Subject
    extra = 0
    inlines = [
        MessageInline,
    ]


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    search_fields = ['user', 'gender', 'last_name', 'first_name', 'phone']
    inlines = [
        AddressInline,
        SubjectInline,
        # MessageInline
    ]


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    search_fields = ['patient_id', 'address',
                     'additional_address', 'postcode', 'city']


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    search_fields = ['created_at', 'modified_at',
                     'patient_id', 'title', 'level']


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    search_fields = ['created_at', 'subject_id', 'user', 'message']
