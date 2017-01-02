from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

from ckeditor.fields import RichTextField
from image_cropping import ImageRatioField
from unidecode import unidecode

HELP_TEXT = (
    "Jméno sekce, ve které bude prvek součástí menu",
    "Nechcete-li specifikovat url, nechte prázdné",
    "Vyjíždecí sloupec, ve kterém se objeví link na tuto sekci",
    "Sekce s vyšší vahou se zobrazí dříve než sekce s nižší vahou",
)

class Column(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Název")
    parent_section = models.ForeignKey('Section', null = False, verbose_name="Název rodičovské sekce", help_text = HELP_TEXT[0])
    weight = models.IntegerField(default=0, verbose_name="Váha", help_text=HELP_TEXT[3])

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sloupec"
        verbose_name_plural = "Sloupce"

class Calendar(models.Model):
    name = models.CharField(max_length = 255, verbose_name = "Název")
    googleId = models.CharField(max_length = 1000)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kalendář"
        verbose_name_plural = "Kalendáře"

class Section(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Název sekce")
    url = models.CharField(max_length = 100, help_text=HELP_TEXT[1], blank=True, unique=True)
    parent_section = models.ForeignKey('self', null = True, blank = True, verbose_name="Název rodičovské sekce", help_text = HELP_TEXT[0])
    #picaty nazev, vymyslet lepsi
    roll_column = models.ForeignKey(Column, null = True, blank = True, verbose_name="Sloupec", help_text = HELP_TEXT[2])
    weight = models.IntegerField(default=0, verbose_name="Váha", help_text=HELP_TEXT[3])
    calendars = models.ManyToManyField(Calendar, verbose_name="Kalendáře", blank = True)

    def __str__(self):
        return self.name

    def clean(self):
        if self.roll_column != None and self.parent_section != None :
            raise ValidationError("Sloupec a rodicovska sekce nemuzou byt obe nenulove")
        if exists_url(self.url, 0):
            raise ValidationError("Zadané url už existuje, zvolte prosím jiné")
        if self.roll_column == None and self.parent_section == None and self.name != 'index':
            raise ValidationError("Sekce musí mít definovanou nadsekci nebo sloupec")
        if self.name == 'index' and len(Section.objects.filter(name = 'index')) > 0:
            raise ValidationError("Nemuzou byt dva indexy")
                

    def save(self, *args, **kwargs):
        self.url = self.create_unique_url(self.url)
        super(Section, self).save(*args, **kwargs)

    def create_unique_url(self, url):
        if url == '' or Section.objects.filter(url=url).exclude(id=self.id).exists() or Article.objects.filter(url=url).exists():
            return self.create_unique_url(url+'1')
        return url

    class Meta:
        verbose_name = "Sekce"
        verbose_name_plural = "Sekce"


class News(models.Model):
    name = models.CharField(max_length = 100)
    section = models.ForeignKey(Section, verbose_name="Název rodičovské sekce", default=1)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Aktuality"
        verbose_name_plural = "Aktuality"

class StaticArticle(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Název statického článku")
    url = models.CharField(max_length = 100, help_text=HELP_TEXT[1], blank=True, unique=True)
    text = RichTextField()
    section = models.ForeignKey(Section, null = True, blank = True, verbose_name="Název rodičovské sekce")
    column = models.ForeignKey(Column, null = True, blank = True, verbose_name="Sloupec", help_text = HELP_TEXT[2])
    weight = models.IntegerField(default=0, verbose_name="Váha", help_text=HELP_TEXT[3])

    def clean(self):
        if self.column != None and self.section != None :
            raise ValidationError("Sloupec a rodicovska sekce nemuzou byt obe nenulove")
        if self.column == None and self.section == None:
            raise ValidationError("Sloupec a rodicovska sekce nemuzou byt obe nulove") 
        if exists_url(self.url, 2):
            raise ValidationError("Zadané url už existuje, zvolte prosím jiné")

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if self.url == '':
            self.url = create_unique_url(unidecode(self.name).replace(' ', '_'))
        super(StaticArticle, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "Statický článek"
        verbose_name_plural = "Statické články"

class Article(models.Model):
    name = models.CharField(max_length = 100, verbose_name="Jméno článku")
    text = RichTextField()
    news = models.ManyToManyField(News, verbose_name="Aktuality", related_name="Aktualitys")
    date = models.DateTimeField(auto_now_add=True)
    weight = models.IntegerField(default=0, verbose_name="Váha", help_text=HELP_TEXT[3])
    user = models.ForeignKey(User, null=True, editable=False)
    url = models.CharField(max_length = 255, help_text=HELP_TEXT[1], blank=True)

    # no uz je to pekne nechutne napsane :D
    def save(self, *args, **kwargs):
        if self.url == '':
            url = unidecode(self.name[:100]).replace(' ', '_')
        else:
            url = self.url.replace(' ', '_')
        self.url = url
        if Article.objects.filter(url=url).exclude(id=self.id).exists() or Section.objects.filter(name=url).exists():
            self.url = create_unique_article_url(url)
        super(Article, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Článek"
        verbose_name_plural = "Články"

class File(models.Model):
    name = models.CharField(max_length = 255, verbose_name="Název souboru")
    soubor = models.FileField(upload_to="user_uploads")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Soubor"
        verbose_name_plural = "Soubory"

class Invitation(models.Model):
    name = models.CharField(max_length = 255, verbose_name="Název")
    image = models.ImageField(upload_to="user_uploads", verbose_name="Obrázek pozvánky")
    cropping = ImageRatioField('image', '430x200', verbose_name="Oříznutí")
    article = models.ForeignKey(Article, verbose_name="Článek spojený s pozváním", null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Pozvánka"
        verbose_name_plural = "Pozvánky"

class Sponzor(models.Model):
    name = models.CharField(max_length = 255, verbose_name = "Název")
    text = RichTextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Sponzor"
        verbose_name_plural = "Sponzoři"

class Contact(models.Model):
    name = models.CharField(max_length = 255, verbose_name = "Název")
    text = RichTextField()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Kontakt"
        verbose_name_plural = "Kontakty"

class Banner(models.Model):
    name = models.CharField(max_length = 255, verbose_name = "Název")
    parent_section = models.ForeignKey('Section', null = False, verbose_name="Název rodičovské sekce") 
    html = models.CharField(max_length = 500, verbose_name = "HTML Kod", null=True, blank=True)
    img = models.ImageField(upload_to="user_uploads", verbose_name="Obrázek", null=True, blank=True)
#    cropping = ImageRatioField('image', '430x200', verbose_name="Oříznutí")

    def __str__(self):
        return self.name

    def clean(self):
        if self.html == None and self.img == None:
            raise ValidationError("Html kod a obrazek nemuzou byt prazdne")
        # if self.html != None and self.img != None:
        #     raise ValidationError("Html kod a obrazek nemuzou byt obe neprazdne")
    
    class Meta:
        verbose_name = "Baner"
        verbose_name_plural = "Banery"


# tyhle jsou pro StaticArticle
def exists_url(url, model):
    if model == 0:
        return Section.objects.exclude(url=url).filter(url=url).exists() or StaticArticle.objects.filter(url=url).exists() 
    elif model == 1:
        raise Exception('tohle uz by se nemlo zavolat')
        return Section.objects.filter(url=url).exists() or StaticArticle.objects.filter(url=url).exists()
    elif model == 2:
        return Section.objects.filter(url=url).exists() or StaticArticle.objects.exclude(url=url).filter(url=url).exists() 
    elif model == 3:
        return Section.objects.filter(url=url).exists() or StaticArticle.objects.filter(url=url).exists() 
    else:
        raise Exception('Chyba v programovani')

    
def create_unique_url(url):
    if exists_url(url, 3):
        return create_unique_url(url + '1')
    return url

#pro Article
def create_unique_article_url(url):
    if Article.objects.filter(url=url).exists() or Section.objects.filter(name=url).exists():
        return create_unique_article_url(url + '1')
    return url
