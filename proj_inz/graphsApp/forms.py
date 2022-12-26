from django import forms

CURRENCY_TAPES = (
    (0, 'To PLN'),
    (1, 'To USD'),
    (2, 'To EUR'),
)
 
class calculatorForm(forms.Form):
    currency_in = forms.ChoiceField(label='Choose Currency', choices=CURRENCY_TAPES, widget=forms.Select)
    value = forms.IntegerField(label = 'Input amount of currency', widget=forms.NumberInput)
    