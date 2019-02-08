from django import forms
from blog.models import Dish, Comment

class PostForm(forms.ModelForm):

    class Meta:
        model = Dish
        fields = ['name', 'portions', 'ingredients', 'description', 'added', 'photo0', 'photo1', 'photo2', 'rating', 'thermomix']

        widgets = {
            'name':forms.TextInput(attrs={'class': 'textinputclass'}),
            # allows to edit text with 'media editor library', 'postcontent' - my class
            'description':forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['author', 'text']

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }