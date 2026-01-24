# bookshelf/forms.py
from django import forms

class ExampleForm(forms.Form):
    """A standard form to demonstrate secure data handling."""
    name = forms.CharField(max_length=100, required=True, help_text="Enter your full name.")
    message = forms.CharField(widget=forms.Textarea, required=True)
    
    # You can add custom clean methods for even deeper security
    def clean_message(self):
        data = self.cleaned_data['message']
        # You could add logic here to block specific keywords or patterns
        return data