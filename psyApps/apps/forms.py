from django import forms
from django.forms import ModelForm, Form
from django.contrib.auth.models import User
from django.forms.widgets import TextInput, PasswordInput, Textarea, Widget
from django.utils.safestring import mark_safe

from apps.models import Subject


class TextareaWidget(Widget):

    def __init__(self, base_widget, data, *args, **kwargs):
        """Initialise widget and get base instance"""
        super(TextareaWidget, self).__init__(*args, **kwargs)
        self.base_widget = base_widget(*args, **kwargs)
        self.data = data

    def render(self, name, value, attrs=None, renderer=None):
        """Render base widget and add bootstrap spans"""
        field = self.base_widget.render(name, value, attrs)
        return mark_safe((
            '<div class="form-floating mb-3">'
            # '  <div class="input-group-prepend">'
            # '    <span class="input-group-text">Message</span>'
            # '  </div>'
            '  <textarea name="message" rows="5" cols="20" class="form-control" placeholder="Votre message" aria-label="Message" required=True></textarea>'
            '  <label for="floatingInput">Votre message</label>'
            '</div>'
        ) % {'field': field, 'data': self.data})


class UserForm(Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Password'}))


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ['id', 'title', 'level']
        extra = 1


class MessageForm(Form):
    message = forms.CharField(
        required=True,
        widget=TextareaWidget(base_widget=Textarea, data='$'),
        label="",
    )
