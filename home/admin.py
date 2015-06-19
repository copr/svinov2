from django.contrib import admin
from image_cropping import ImageCroppingMixin

from home.models import Section, File, Article, StaticArticle, News, Invitation

class InvitationAdmin(ImageCroppingMixin, admin.ModelAdmin):
    pass

admin.site.register(Section)
admin.site.register(File)
admin.site.register(Article)
admin.site.register(StaticArticle)
admin.site.register(News)
admin.site.register(Invitation, InvitationAdmin)
