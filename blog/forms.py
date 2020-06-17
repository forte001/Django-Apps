from django import forms
"""
This forms holds the author of the post
"""

class CommentForm(forms.Form):
    author = forms.CharField(
        max_length=60,
        widget=forms.TextInput(attrs={
            'class' : 'form-control',
            'placeholder': 'Your name'
        })
    )
    body = forms.CharField(widget=forms.Textarea(
        attrs={'class' : 'form-control',
        'placeholder' : 'Leave a comment!'
        })
    )