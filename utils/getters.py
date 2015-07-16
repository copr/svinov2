from django.shortcuts import get_object_or_404

from home.models import Section, Article, News, StaticArticle, Invitation, Column, Calendar, Sponzor, Contact

def get_article(article_id):
    return Article.objects.get(id = article_id)

def get_posts(section):
    main_section = Section.objects.get(url = section)
    if News.objects.all().filter(section = main_section).exists():
        news = News.objects.get(section = main_section)
        posts = Article.objects.all().filter(news = news).order_by('-weight', '-date')
    else:
        posts = []
    for post in posts:
        post.section = section
    return posts

def get_current_section(section):
    return Section.objects.get(url = section)

def get_all_posts():
    return Article.objects.all().order_by('-weight', '-date')

def get_sections(section):
    #main_section je objekt ktery reprezentuje sekci identifikovanou stringem section
    main_section = get_object_or_404(Section, url = section)
#    main_section = Section.objects.get(url=section)
    other_sections = []
    for s in Section.objects.all().filter(parent_section = main_section):
        other_sections.append({'name': s.name, 'url': s.url})
    sections = get_news(main_section) + other_sections + get_columns(section) + get_statics(section)
    return sections

# Tady to chce poradne promyslet a predelat
def get_columns(section):
    columns = []
    main_section = get_object_or_404(Section, url = section)
#    main_section = Section.objects.get(url=section)
    for column in Column.objects.all().filter(parent_section = main_section):
        sections = Section.objects.all().filter(roll_column = column)
        statics = []
        for s in  StaticArticle.objects.all().filter(column = column):
            statics.append({'name': s.name, 'url': main_section.url + '/' + s.url})
        subsections = list(sections) + list(statics)
        columns.append({'name': column.name, 'url': '#', 'subsections': subsections})
    return columns

def get_statics(section):
    main_section = get_object_or_404(Section, url = section)
#    main_section = Section.objects.get(url=section)
    statics = []
    for s in StaticArticle.objects.all().filter(section = main_section):
        statics.append({'name': s.name, 'url': main_section.url + '/' + s.url})
    return statics

def get_static(static):
#    return StaticArticle.objects.get(url=static)
    return get_object_or_404(StaticArticle, url = static)

def get_invitations():
    return Invitation.objects.all()

def get_news(main_section):
    if News.objects.filter(section = main_section).exists():
        news = [{'name': 'Aktuality', 'url': main_section.url + '/aktuality'}]
    else:
        news = [] 
    return news

def get_calendars(section):
    main_section = get_object_or_404(Section, url = section)
    return Calendar.objects.all().filter(section = main_section)

def get_sponsors():
    return Sponzor.objects.all()

def get_contacts():
    return Contact.objects.all()

