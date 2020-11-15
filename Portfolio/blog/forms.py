from django import forms

class CommentForm(forms.Form):
    s_Author    = forms.CharField( max_length=60,
                                widget=forms.TextInput(attrs={
                                    "class":"form-control",
                                    "placeholder": "Your Name"
                                })
    )

    s_Body      = forms.CharField(widget=forms.Textarea(
                    attrs={
                        "class": "form-control",
                        "placeholder": "Leave a comment!"
                    })
    )
