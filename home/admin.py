from django.contrib import admin
from image_cropping import ImageCroppingMixin

from home.models import Section, File, Article, StaticArticle, News, Invitation, Column, Calendar, Sponzor, Contact, Banner

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
    list_display = ('name', 'date', sekce, 'weight')

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
