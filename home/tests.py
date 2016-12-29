from django.test import TestCase
import tempfile
from home.models import *

class ModelTestCase(TestCase):
    def setUp(self):
        self.index = Section.objects.create(
            name="index", parent_section = None, roll_column = None)
        self.roll = Column.objects.create(
            name="col", parent_section = self.index, weight = 1)
        self.news = News.objects.create(
            name="n", section=self.index)
        # self.index = Section.get(name="index")
        # self.roll = Column.get(name="col")
    
    def test_section_both_null(self):
        instance = Section.objects.create(
            name="Not important", url="ahoj", parent_section = None,
            roll_column = None, weight = 1)
        self.assertRaises(ValidationError, instance.clean)

    def test_section_both_notnull(self):
        instance = Section.objects.create(
            name="Not important", url="ahoj", parent_section = self.index,
            roll_column = self.roll, weight = 1)
        self.assertRaises(ValidationError, instance.clean)

    def test_two_indexes(self):
        #First one is in the setup
        index2 = Section.objects.create(name="index", parent_section = None,
                                        roll_column = None)
        self.assertRaises(ValidationError, index2.clean)

    def test_banner(self):
        banner1 = Banner.objects.create(name="banner1", parent_section = self.index,
                                        html = None, img = None)
        self.assertRaises(ValidationError, banner1.clean)

    def test_create_change_Column(self):
        c = Column.objects.create(
            name="Column", parent_section = self.index, weight=0
        )
        c.save()

    def test_create_change_Calendar(self):
        c = Calendar.objects.create(
            name="C", googleId="ahoj"
        )
        c.save()

    def test_create_change_Section(self):
        s = Section.objects.create(
            name="s", url="url", parent_section=self.index,
            weight = 0
        )
        s.save()

    def test_create_change_News(self):
        n = News.objects.create(
            name="n", section=self.index)
        n.save()

    def test_create_change_StaticArticle(self):
        sa = StaticArticle.objects.create(
            name="sa", url="url", text="ahoj", section=self.index,
            weight = 1)
        sa.save()

    def test_create_change_Article(self):
        a = Article.objects.create(
            name="a", text="ahoj")
        a.news.add(self.news)
        a.save()

    def test_create_change_Inviatation(self):
        image = tempfile.NamedTemporaryFile(suffix=".jpg").name
        i = Invitation.objects.create(name="i", image=image, cropping=image)
        i.save()
            
    def test_create_change_Sponzor(self):
        s = Sponzor.objects.create(
            name="s", text="ahoj")
        s.save()

    def test_create_change_Contact(self):
        c = Contact.objects.create(
            name="c", text="cest")
        c.save()

    def test_create_change_Banner(self):
        b = Banner.objects.create(
            name="b", parent_section=self.index)
        b.save()
