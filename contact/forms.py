from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(min_length=2, max_length=300, label="Your name")
    email = forms.EmailField(min_length=3, max_length=320, label="Email address")
    subject = forms.CharField(min_length=3, max_length=600, label="Subject")
    message = forms.CharField(min_length=5, max_length=2000, label="Your message", widget=forms.Textarea())

    class Meta:
        model = Contact
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                "class": "form-control"
            })

    def clean(self):
        name = self.cleaned_data.get('name')

        if name:
            if not name.replace(" ", "").replace(",", "").replace(".", "").isalpha():
                self.add_error("name", "Adınızı doğru daxil edin")