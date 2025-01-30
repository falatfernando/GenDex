from django import forms

class DNAInputForm(forms.Form):
    sequence = forms.CharField(
        label='DNA Sequence',
        widget=forms.Textarea(attrs={'rows': 5}),
        required=True
    )
