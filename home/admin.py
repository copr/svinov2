from django.contrib import admin
from image_cropping import ImageCroppingMixin

from home.models import *



class InvitationAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

class CalendarAdmin(admin.StackedInline):
    model = Calendar

class SectionAdmin(admin.ModelAdmin):
    pass

def sekce(obj):
    news_concat = ""
    for new in obj.news.all():
        news_concat = news_concat + new.name + ", "
    return news_concat

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', sekce, 'weight', 'user')
    
    def save_model(self, request, obj, form, change):
        if obj.user == None:
            obj.user = request.user
        obj.save()

    # def save_formset(self, request, form, formset, change): 
    #     if formset.model == Comment:
    #         instances = formset.save(commit=False)
    #         for instance in instances:
    #             instance.user = request.user
    #             instance.save()
    #     else:
    #         formset.save()

class StaticArticleAdmin(admin.ModelAdmin):
    list_display = ('name', 'section', 'column')



admin.site.register(Section, SectionAdmin)
admin.site.register(File)
admin.site.register(Article, ArticleAdmin)
admin.site.register(StaticArticle, StaticArticleAdmin)
admin.site.register(News)
admin.site.register(Invitation, InvitationAdmin)
admin.site.register(Sponzor)
admin.site.register(Contact)
admin.site.register(Column)
admin.site.register(Calendar)
admin.site.register(Banner)

#admin.site.register(EventField, EventFieldAdmin)
