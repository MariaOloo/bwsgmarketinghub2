# bwsgmarketinghub2/forms.py
from django import forms

class QuoteForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email')
    service = forms.ChoiceField(
        label='Service',
        choices=[
            ('Brand Strategy', 'Brand Strategy'),
            ('Content Creation', 'Content Creation'),
            ('SEO', 'Search Engine Optimization (SEO)'),
            ('Social Media Management', 'Social Media Management'),
            ('Data Analytics', 'Data Analytics'),
        ]
    )
    time_period = forms.ChoiceField(
        label='Time Period',
        choices=[
            ('Short Term', 'Short Term'),
            ('Long Term', 'Long Term'),
        ]
    )
    specify = forms.CharField(label='Specify', widget=forms.Textarea)
