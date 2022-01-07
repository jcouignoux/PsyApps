from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from apps.models import Patient, Subject
from apps.serializers import PatientSerializer, SubjectDetailSerializer


class MultipleSerializerMixin:

    detail_serializer_class = None

    def get_serializer_class(self):
        if self.action == 'retrieve' and self.detail_serializer_class is not None:
            return self.detail_serializer_class
        return super().get_serializer_class()


class PatientViewset(ReadOnlyModelViewSet):

    serializer_class = PatientSerializer
    # detail_serializer_class = PatientDetailSerializer

    def get_queryset(self):
        return Patient.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()


class SubjectViewset(ReadOnlyModelViewSet):

    serializer_class = SubjectDetailSerializer
    # detail_serializer_class = PatientDetailSerializer

    def get_queryset(self):
        return Subject.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return self.detail_serializer_class
        return super().get_serializer_class()
