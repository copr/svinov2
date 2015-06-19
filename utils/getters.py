from home.models import Section, Article, News, StaticArticle, Invitation

def get_article(article_id):
    return Article.objects.get(id = article_id)

def get_posts(section):
    main_section = Section.objects.get(name=section)
    if News.objects.all().filter(section=main_section).exists():
        news = News.objects.get(section=main_section)
        posts = Article.objects.all().filter(news=news)
    else:
        posts = []
    return posts

def get_all_posts():
    return Article.objects.all()

def get_all_posts():
    return Article.objects.all()

def get_sections(section):
    #main_section je objekt ktery reprezentuje sekci identifikovanou stringem section
    main_section = Section.objects.get(name=section)
    other_sections = []
    for s in Section.objects.all().filter(parent_section=main_section):
        other_sections.append({'name': s.name, 'url': s.name})
    sections = get_news(main_section) + other_sections + get_statics(section)
    return sections

def get_statics(section):
    main_section = Section.objects.get(name=section)
    statics = []
    for s in StaticArticle.objects.all().filter(section=main_section):
        statics.append({'name': s.name, 'url': section + '/' + s.name})
    return statics

def get_static(static):
    return StaticArticle.objects.get(name=static)

def get_invitations():
    return Invitation.objects.all()

def get_news(main_section):
    if News.objects.filter(section=main_section).exists():
        news = [{'name': 'Aktuality', 'url': main_section.name + '/aktuality'}]
    else:
        news = [] 
    return news
