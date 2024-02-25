from django import forms
from django.forms import fields, ModelForm
from arc_app.models import RfidTags

#create a form to add tags
class TagForm(ModelForm):
    class Meta:
        model = RfidTags
        fields = ('tag_no', 'pupil_name')