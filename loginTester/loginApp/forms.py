from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, ButtonHolder, Submit

class TestForm(forms.Form):
    name = forms.CharField(required=False)
    email = forms.EmailField(required=True)
    # url = forms.URLField(required=False)
    # comment = forms.CharField(required=True, widget=forms.Textarea)

    @property
    def helper(self):
        helper = FormHelper()
        helper.form_tag = False # don't render form DOM element
        helper.layout = Layout(
            Field('email'),
            ButtonHolder(
                Submit('submit', 'Enregistrer', css_class='button white')
            )
        )
        helper.render_unmentioned_fields = False # render all fields
        helper.label_class = 'col-md-2'
        helper.field_class = 'col-md-10'
        return helper