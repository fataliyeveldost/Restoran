from django.forms import ModelForm
from.models import Menyu
class MenyuForm(ModelForm):
    class Meta:
        model=Menyu
        fields='__all__'