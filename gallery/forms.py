from django import forms

class GalleryForm(forms.Form):
    image = forms.ImageField(upload_to="media")