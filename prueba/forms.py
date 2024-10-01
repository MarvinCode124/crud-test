from django import forms
from .models import Article

class FormArticle(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'pub_date': forms.DateInput(attrs={'class': 'form-control mb-3', 'type': 'date'}),
            'headline': forms.TextInput(attrs={'class': 'form-control mb-3', 'placeholder': 'Agrega el headline'}),
            'content': forms.Textarea(attrs={'class':'form-control mb-3'}),
            'reporter': forms.Select(attrs={'class':'form-select'})
        }
        labels = {
            'pub_date': 'Fecha de publicación',
            'headline': 'Titulo de articulo',
            'reporter': 'Reporte'
        }
