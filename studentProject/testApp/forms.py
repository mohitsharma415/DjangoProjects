from django import forms
from testApp.models import Students
class studentForm(forms.ModelForm):
    class Meta:
        model=Students
        fields='__all__'
