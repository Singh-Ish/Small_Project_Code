from django import forms
from blog.models import Post,Comment # importing the created models from models.py to forms.py

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('author','title','text')

        widgets = {  # for customized css for the form widgets
            'title' : forms.TextInput(attrs={'class':'textinputclass'}),
            'text' : forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})

        }

class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('author','text')

        widgets = {  # for customized css for the form widgets
            'author' : forms.TextInput(attrs={'class':'textinputclass'}),
            'text' : forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})

            }
