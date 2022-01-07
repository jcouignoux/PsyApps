from django.forms.models import ModelForm
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth import login, logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.db import transaction

from apps.forms import UserForm, SubjectForm, MessageForm
from apps.models import Patient, Subject, Message


def index(request):

    return render(request, 'apps/index.html')


class PatientView(TemplateView):
    template_name = 'apps/patient.html'
    # form_class = SubjectForm
    # success_url = reverse_lazy('apps')
    # success_message = "Way to go!"

    def get(self, request):
        MForm = MessageForm()
        patient = Patient.objects.filter(user_id=request.user.id).first()
        context = {
            'patient': patient,
            'MForm': MForm,
        }

        return render(request, 'apps/patient.html', context)

    def post(self, request):
        MForm = MessageForm(request.POST)
        subject_id = request.POST.get('subject_id')
        subject = get_object_or_404(Subject, id=subject_id)
        if MForm.is_valid():
            with transaction.atomic():
                message = Message()
                message.subject_id = subject
                message.message = MForm.cleaned_data.get('message')
                message.user = request.user
                # message.save()
        else:
            error = "une erreur est survenue"

        patient = Patient.objects.filter(user_id=request.user.id).first()
        context = {
            'patient': patient,
            'MForm': MForm,
            'subject_id': int(subject_id),
        }

        return render(request, 'apps/patient.html', context)


class LoginView(TemplateView):

    template_name = 'apps/login.html'
    context = {}

    def post(self, request, **kwargs):
        UForm = UserForm(data=request.POST)
        if UForm.is_valid():
            username = UForm.cleaned_data['username']
            password = UForm.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return render(request, 'apps/index.html')
            else:
                error_message = "Identifiant ou mot de passe incorrect."
                messages.error(request, error_message)

        context = {'UForm': UForm}

        return render(request, self.template_name, context)

    def get(self, request):
        UForm = UserForm()
        context = {'UForm': UForm}

        return render(request, self.template_name, context)


# @login_required
class LogoutView(TemplateView):

    template_name = 'apps/index.html'

    def get(self, request):

        logout(request)

        return render(request, self.template_name)
