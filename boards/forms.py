from django import forms
from .models import Topic, Post

class NewTopicForm(forms.ModelForm):
    message = forms.CharField(widget=forms.Textarea(attrs={'rows':5 ,'placeholder':'what\'s on your mind?'}),
                              max_length=3000)
    class Meta:
        model = Topic
        fields = ['subject', 'message']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']
