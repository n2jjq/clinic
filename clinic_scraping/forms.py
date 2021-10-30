from django import forms
from .models import Condition

class ConditionForm(forms.ModelForm):
  class Meta:
    model = Condition
    fields = ('name', 'address', 'department', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday','saturday', 'sunday', 'holiday')