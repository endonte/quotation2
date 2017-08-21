from django import forms
from .models import Product
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout



class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = (
                'product_name',
                'category',
                'uom',
        )

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        #self.helper.form_action = ''
        self.helper.help_text_inline = False
        self.helper.form_error_title = 'Form Errors'

        self.helper.add_input(Submit('submit', 'Submit'))
        super(ProductForm, self).__init__(*args, **kwargs)
