from django.forms import ModelForm
from .models import New


class NewsForm(ModelForm):
    class Meta:
        model = New
        fields = ["title", "content"]
