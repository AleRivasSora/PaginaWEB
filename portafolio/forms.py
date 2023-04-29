from django import forms
from portafolio.models import Contacto
from django.utils import timezone

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Contacto
        fields = ['nombre', 'email', 'telefono', 'asunto', 'mensaje']
        '''widgets = {
            'fecha_envio': forms.HiddenInput(),
        }'''

    def save(self, commit=True):
        contacto = super(ContactoForm, self).save(commit=False)
        if commit:
            contacto.save()
        return contacto