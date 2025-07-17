from django import forms
from .models import Idea, DevTool, Tag

class IdeaForm(forms.ModelForm):
    tag_names = forms.CharField(required=False, help_text="쉼표로 구분된 태그 입력")

    class Meta:
        model = Idea
        fields = ['title', 'image', 'content', 'interest', 'devtool']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance.pk:
            self.fields['tag_names'].initial = ', '.join(tag.name for tag in self.instance.tags.all())
    
    def save(self, commit=True):
        instance = super().save(commit=False)
        if commit:
            instance.save()
        
        instance.tags.clear()
        tag_names = self.cleaned_data.get('tag_names', '').split(',')
        for name in tag_names:
            cleaned = name.strip()
            if cleaned:
                tag, _ = Tag.objects.get_or_create(name=name.strip())
                instance.tags.add(tag)
        return instance

class DevToolForm(forms.ModelForm):
    class Meta:
        model = DevTool
        fields = ['name', 'kind', 'content']