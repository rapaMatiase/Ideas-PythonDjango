from django.forms import fields
from .models import MyExcelFiles
from django.forms import ModelForm

class MyExcelFilesForm(ModelForm):
    class Meta:
        model = MyExcelFiles
        fields = '__all__'