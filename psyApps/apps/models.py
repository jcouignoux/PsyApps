from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Patient(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Contact")
    MISTER = 'MR'
    MISS = 'MISS'
    MISSES = 'MRS'
    GENDER = (
        (MISTER, 'Monsieur'),
        (MISS, 'Mademoiselle'),
        (MISSES, 'Madame'),
    )
    gender = models.CharField(
        max_length=4, choices=GENDER, default=MISTER, verbose_name="Civilité")
    last_name = models.CharField(max_length=50, verbose_name="Nom")
    first_name = models.CharField(max_length=50, verbose_name="Prénom")
    phone = models.CharField(max_length=10, verbose_name="Téléphone")

    def __str__(self):
        return self.last_name + " " + self.first_name

    class Meta:
        verbose_name = "Patient"

    @property
    def get_address(self):
        patient_address = Address.objects.filter(patient_id=self.id)
        return patient_address

    @property
    def get_subjects(self):
        patient_subjects = Subject.objects.filter(patient_id=self.id)
        return patient_subjects


class Address(models.Model):
    patient_id = models.ForeignKey(
        Patient, on_delete=models.CASCADE, verbose_name="Patient")
    address = models.CharField(max_length=255, verbose_name="Adresse")
    additional_address = models.CharField(
        max_length=255, blank=True, verbose_name="Complément d'adresse")
    postcode = models.CharField(max_length=5, verbose_name="Code postal")
    city = models.CharField(max_length=50, verbose_name="Ville")

    class Meta:
        verbose_name = 'Adresse'
        verbose_name_plural = 'Adresses'

    def __str__(self):
        return self.patient_id.first_name + " " + self.patient_id.last_name + " (" + self.address + ", " + self.postcode + " " + self.city + ")"


class Subject(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    patient_id = models.ForeignKey(
        Patient, on_delete=models.CASCADE, verbose_name="Patient")
    title = models.CharField(
        max_length=50, blank=True, verbose_name="Titre")
    LOW = 'L'
    MEDIUM = 'M'
    HIGHT = 'H'
    LEVEL = (
        (LOW, 'Bas'),
        (MEDIUM, 'Moyen'),
        (HIGHT, 'Urgent'),
    )
    level = models.CharField(
        max_length=4, choices=LEVEL, default=LOW, verbose_name="Criticité")

    class Meta:
        verbose_name = 'Sujet'

    def __str__(self):
        return self.patient_id.first_name + " " + self.patient_id.last_name + " (" + self.title + ")"

    @property
    def get_messages(self):
        subject_detail = Message.objects.filter(subject_id=self.id)
        return subject_detail


class Message(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    subject_id = models.ForeignKey(
        Subject, on_delete=models.CASCADE, verbose_name="Sujet")
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Auteur", null=True)
    message = models.CharField(max_length=1000, verbose_name="Message")

    class Meta:
        verbose_name = 'Message'

    def __str__(self):
        return self.user.first_name + " " + self.user.last_name + " (" + self.subject_id.title + ")"
