from django.contrib import admin
from .models import Condition
from .forms import ConditionForm

class ConditionAdmin(admin.ModelAdmin):
  form = ConditionForm

admin.site.register(Condition, ConditionAdmin)



