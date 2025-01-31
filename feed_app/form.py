from django import forms
from feed_app.models import Tweet

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['content']
        
    def clean_content(self):
        content = self.cleaned_data.get("content")
        if len(content) > 300:
            raise forms.ValidationError("El tweet no puede superar los 300 caracteres.")
        return content