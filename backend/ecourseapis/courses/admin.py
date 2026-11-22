
from django.contrib import admin
from django.utils.safestring import mark_safe
from django.templatetags.static import static
from django import forms

from courses.models import Category, Course, Lesson, Tag

from ckeditor_uploader.widgets import CKEditorUploadingWidget


class LessonForm(forms.ModelForm):
    content = forms.CharField(
        widget=CKEditorUploadingWidget()
    )

    class Meta:
        model = Lesson
        fields = '__all__'


class LessonAdmin(admin.ModelAdmin):
    list_display = ['id', 'subject', 'created_date']
    search_fields = ['subject', 'content']
    list_filter = ['id', 'subject', 'created_date']
    readonly_fields = ['image_view']
    form = LessonForm

    def image_view(self, lesson):
        if lesson.image:
            return mark_safe(
                f'<img src="{lesson.image.url}" width="200" />'
            )
        return "Chưa có ảnh"

    image_view.short_description = "Preview Image"

    class Media:
        css = {
            'all': ('css/styles.css',)
        }


admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Tag)
