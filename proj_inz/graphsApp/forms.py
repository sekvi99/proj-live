from django import forms

CURRENCY_TAPES = (
    ('PLN', 'To PLN'),
    ('USD', 'To USD'),
    ('EUR', 'To EUR'),
    ('GBP', 'To GBP'),
)
 
class calculatorForm(forms.Form):
    currency_in = forms.ChoiceField(label='Choose Currency', choices=CURRENCY_TAPES, widget=forms.Select)
    value = forms.FloatField(label = 'Input amount of currency', widget=forms.NumberInput)
    