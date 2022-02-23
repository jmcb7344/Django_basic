from dataclasses import fields
from django.forms import forms, ModelForm
from app_RRHH import models


class Contact(forms.Form):
    pass


class EditarF(ModelForm):
    class Meta:
        model = models.Empleado
        fields = '__all__'