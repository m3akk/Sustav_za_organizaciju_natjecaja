from django.test import TestCase, Client
from django.urls import reverse
from .models import *
from .forms import *

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main import views





class TestUrls(SimpleTestCase):
    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.index)

    def test_login_url_resolves(self):
        url = reverse('login')
        self.assertEqual(resolve(url).func, views.login_view)

    def test_register_url_resolves(self):
        url = reverse('register')
        self.assertEqual(resolve(url).func, views.register)

    def test_logout_url_resolves(self):
        url = reverse('logout')
        self.assertEqual(resolve(url).func, views.logout)

    def test_organizator_list_url_resolves(self):
        url = reverse('organizator_list')
        self.assertEqual(resolve(url).func, views.organizator_list)

    def test_organizator_create_url_resolves(self):
        url = reverse('organizator_create')
        self.assertEqual(resolve(url).func, views.organizator_create)

    def test_organizator_detail_url_resolves(self):
        url = reverse('organizator_detail', args=[1])
        self.assertEqual(resolve(url).func, views.organizator_detail)

    def test_organizator_update_url_resolves(self):
        url = reverse('organizator_update', args=[1])
        self.assertEqual(resolve(url).func, views.organizator_update)

    def test_organizator_delete_url_resolves(self):
        url = reverse('organizator_delete', args=[1])
        self.assertEqual(resolve(url).func, views.organizator_delete)

    def test_sudionik_list_url_resolves(self):
        url = reverse('sudionik_list')
        self.assertEqual(resolve(url).func, views.sudionik_list)

    def test_sudionik_create_url_resolves(self):
        url = reverse('sudionik_create')
        self.assertEqual(resolve(url).func, views.sudionik_create)

    def test_sudionik_detail_url_resolves(self):
        url = reverse('sudionik_detail', args=[1])
        self.assertEqual(resolve(url).func, views.sudionik_detail)

    def test_sudionik_update_url_resolves(self):
        url = reverse('sudionik_update', args=[1])
        self.assertEqual(resolve(url).func, views.sudionik_update)

    def test_sudionik_delete_url_resolves(self):
        url = reverse('sudionik_delete', args=[1])
        self.assertEqual(resolve(url).func, views.sudionik_delete)

    def test_natjecaj_list_url_resolves(self):
        url = reverse('natjecaj_list')
        self.assertEqual(resolve(url).func, views.natjecaj_list)

    def test_natjecaj_create_url_resolves(self):
        url = reverse('natjecaj_create')
        self.assertEqual(resolve(url).func, views.natjecaj_create)

    def test_natjecaj_detail_url_resolves(self):
        url = reverse('natjecaj_detail', args=[1])
        self.assertEqual(resolve(url).func, views.natjecaj_detail)

    def test_natjecaj_update_url_resolves(self):
        url = reverse('natjecaj_update', args=[1])
        self.assertEqual(resolve(url).func, views.natjecaj_update)

    def test_natjecaj_delete_url_resolves(self):
        url = reverse('natjecaj_delete', args=[1])
        self.assertEqual(resolve(url).func, views.natjecaj_delete)

    def test_prijava_list_url_resolves(self):
        url = reverse('prijava_list')
        self.assertEqual(resolve(url).func, views.prijava_list)

    def test_prijava_create_url_resolves(self):
        url = reverse('prijava_create')
        self.assertEqual(resolve(url).func, views.prijava_create)

    def test_prijava_detail_url_resolves(self):
        url = reverse('prijava_detail', args=[1])
        self.assertEqual(resolve(url).func, views.prijava_detail)

    def test_prijava_update_url_resolves(self):
        url = reverse('prijava_update', args=[1])
        self.assertEqual(resolve(url).func, views.prijava_update)

    def test_prijava_delete_url_resolves(self):
        url = reverse('prijava_delete', args=[1])
        self.assertEqual(resolve(url).func, views.prijava_delete)

































class TestModels(TestCase):
    def setUp(self):
        self.organizator = Organizator.objects.create(
            organizator_naziv='Test Organizator',
            organizator_email='test@organizator.com'
        )
        self.sudionik = Sudionik.objects.create(
            sudionik_naziv='Test Sudionik',
            sudionik_email='test@sudionik.com'
        )
        self.natjecaj = Natjecaj.objects.create(
            natjecaj_naziv='Test Natjecaj',
            natjecaj_datum='2022-01-01',
            natjecaj_organizator=self.organizator
        )
        self.prijava = Prijava.objects.create(
            prijava_broj=1,
            prijava_natjecaj=self.natjecaj,
            prijava_sudionik=self.sudionik
        )

    def test_organizator_str(self):
        self.assertEqual(str(self.organizator), 'Test Organizator')

    def test_sudionik_str(self):
        self.assertEqual(str(self.sudionik), 'Test Sudionik')

    def test_natjecaj_str(self):
        self.assertEqual(str(self.natjecaj), 'Test Natjecaj')

    def test_prijava_str(self):
        self.assertEqual(str(self.prijava), '1')















































def test_index(self):
    response = self.client.get(self.index_url)
    self.assertEqual(response.status_code, 200)
    self.assertTemplateUsed(response, 'index.html')









class TestViews_Login(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.index_url = reverse('index')
        self.user_data = {
            'username': 'testuser',
            'password1': 'testpass123',
            'password2': 'testpass123'
        }
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

    def test_register_GET(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/register.html')

    # def test_register_POST(self):
    #     response = self.client.post(self.register_url, self.user_data)
    #     self.assertEqual(response.status_code, 302)
    #     self.assertRedirects(response, self.index_url)

    def test_login_GET(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'registration/login.html')

    def test_login_POST(self):
        response = self.client.post(self.login_url, {
            'username': 'testuser',
            'password': 'testpass123'
        })
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.index_url)

    def test_logout(self):
        self.client.login(username='testuser', password='testpass123')
        response = self.client.get(self.logout_url)
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, self.index_url)

















class TestViews_Organizator(TestCase):

    def setUp(self):
        self.client = Client()
        self.organizator_list_url = reverse('organizator_list')
        self.organizator_detail_url = reverse('organizator_detail', args=[1])
        self.organizator_create_url = reverse('organizator_create')
        self.organizator_update_url = reverse('organizator_update', args=[1])
        self.organizator_delete_url = reverse('organizator_delete', args=[1])

        self.organizator = Organizator.objects.create(
            organizator_naziv='Test Organizator',
            organizator_email='test@organizator.com'
        )

    def test_organizator_list_GET(self):
        response = self.client.get(self.organizator_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'organizatori/organizator_list.html')

    def test_organizator_detail_GET(self):
        response = self.client.get(self.organizator_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'organizatori/organizator_detail.html')

    def test_organizator_create_GET(self):
        response = self.client.get(self.organizator_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'organizatori/organizator_create.html')
        self.assertIsInstance(response.context['form'], OrganizatorForm)

    def test_organizator_create_POST(self):
        response = self.client.post(self.organizator_create_url, {
            'organizator_naziv': 'New Organizator',
            'organizator_email': 'new@organizator.com'
        })

        self.assertRedirects(response, self.organizator_list_url)

    def test_organizator_update_GET(self):
        response = self.client.get(self.organizator_update_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'organizatori/organizator_update.html')
        self.assertIsInstance(response.context['form'], OrganizatorForm)

    def test_organizator_update_POST(self):
        response = self.client.post(self.organizator_update_url, {
            'organizator_naziv': 'Updated Organizator',
            'organizator_email': 'updated@organizator.com'
        })

        self.assertRedirects(response, self.organizator_list_url)

    def test_organizator_delete_GET(self):
        response = self.client.get(self.organizator_delete_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'organizatori/organizator_delete.html')
        self.assertIsInstance(response.context['form'], OrganizatorDeleteForm)

    def test_organizator_delete_POST(self):
        response = self.client.post(self.organizator_delete_url)

        self.assertRedirects(response, self.organizator_list_url)





















class TestViews_Sudionik(TestCase):

    def setUp(self):
        self.client = Client()
        self.sudionik_list_url = reverse('sudionik_list')
        self.sudionik_detail_url = reverse('sudionik_detail', args=[1])
        self.sudionik_create_url = reverse('sudionik_create')
        self.sudionik_update_url = reverse('sudionik_update', args=[1])
        self.sudionik_delete_url = reverse('sudionik_delete', args=[1])

        self.sudionik = Sudionik.objects.create(
            sudionik_naziv='Test Sudionik',
            sudionik_email='test@sudionik.com'
        )

    def test_sudionik_list_GET(self):
        response = self.client.get(self.sudionik_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sudionici/sudionik_list.html')

    def test_sudionik_detail_GET(self):
        response = self.client.get(self.sudionik_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sudionici/sudionik_detail.html')

    def test_sudionik_create_GET(self):
        response = self.client.get(self.sudionik_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sudionici/sudionik_create.html')
        self.assertIsInstance(response.context['form'], SudionikForm)

    def test_sudionik_create_POST(self):
        response = self.client.post(self.sudionik_create_url, {
            'sudionik_naziv': 'New Sudionik',
            'sudionik_email': 'new@sudionik.com'
        })

        self.assertRedirects(response, self.sudionik_list_url)

    def test_sudionik_update_GET(self):
        response = self.client.get(self.sudionik_update_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sudionici/sudionik_update.html')
        self.assertIsInstance(response.context['form'], SudionikForm)

    def test_sudionik_update_POST(self):
        response = self.client.post(self.sudionik_update_url, {
            'sudionik_naziv': 'Updated Sudionik',
            'sudionik_email': 'updated@sudionik.com'
        })

        self.assertRedirects(response, self.sudionik_list_url)

    def test_sudionik_delete_GET(self):
        response = self.client.get(self.sudionik_delete_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'sudionici/sudionik_delete.html')
        self.assertIsInstance(response.context['form'], SudionikDeleteForm)

    def test_sudionik_delete_POST(self):
        response = self.client.post(self.sudionik_delete_url)

        self.assertRedirects(response, self.sudionik_list_url)




























class TestViews_Natjecaj(TestCase):

    def setUp(self):
        self.client = Client()
        self.natjecaj_list_url = reverse('natjecaj_list')
        self.natjecaj_detail_url = reverse('natjecaj_detail', args=[1])
        self.natjecaj_create_url = reverse('natjecaj_create')
        self.natjecaj_update_url = reverse('natjecaj_update', args=[1])
        self.natjecaj_delete_url = reverse('natjecaj_delete', args=[1])

        self.organizator = Organizator.objects.create(
            organizator_naziv='Test Organizator',
            organizator_email='test@organizator.com'
        )

        self.sudionik = Sudionik.objects.create(
            sudionik_naziv='Test Sudionik',
            sudionik_email='test@sudionik.com'
        )

        self.natjecaj = Natjecaj.objects.create(
            natjecaj_naziv='Test Natjecaj',
            natjecaj_datum='2022-01-01',
            natjecaj_organizator=self.organizator
        )
        self.natjecaj.natjecaj_sudionici.add(self.sudionik)

    def test_natjecaj_list_GET(self):
        response = self.client.get(self.natjecaj_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'natjecaji/natjecaj_list.html')

    def test_natjecaj_detail_GET(self):
        response = self.client.get(self.natjecaj_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'natjecaji/natjecaj_detail.html')

    def test_natjecaj_create_GET(self):
        response = self.client.get(self.natjecaj_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'natjecaji/natjecaj_create.html')
        self.assertIsInstance(response.context['form'], NatjecajForm)

    def test_natjecaj_create_POST(self):
        response = self.client.post(self.natjecaj_create_url, {
            'natjecaj_naziv': 'New Natjecaj',
            'natjecaj_datum': '2022-01-01',
            'natjecaj_organizator': self.organizator.id,
            'natjecaj_sudionici': [self.sudionik.id]
        })

        self.assertRedirects(response, self.natjecaj_list_url)

    def test_natjecaj_update_GET(self):
        response = self.client.get(self.natjecaj_update_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'natjecaji/natjecaj_update.html')
        self.assertIsInstance(response.context['form'], NatjecajForm)

    def test_natjecaj_update_POST(self):
        response = self.client.post(self.natjecaj_update_url, {
            'natjecaj_naziv': 'Updated Natjecaj',
            'natjecaj_datum': '2022-01-01',
            'natjecaj_organizator': self.organizator.pk,
            'natjecaj_sudionici': [self.sudionik.pk]
        })

        self.assertRedirects(response, self.natjecaj_list_url)

    def test_natjecaj_delete_GET(self):
        response = self.client.get(self.natjecaj_delete_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'natjecaji/natjecaj_delete.html')
        self.assertIsInstance(response.context['form'], NatjecajDeleteForm)

    def test_natjecaj_delete_POST(self):
        response = self.client.post(self.natjecaj_delete_url)

        self.assertRedirects(response, self.natjecaj_list_url)

























class TestViews_Prijava(TestCase):

    def setUp(self):
        self.client = Client()
        self.prijava_list_url = reverse('prijava_list')
        self.prijava_detail_url = reverse('prijava_detail', args=[1])
        self.prijava_create_url = reverse('prijava_create')
        self.prijava_update_url = reverse('prijava_update', args=[1])
        self.prijava_delete_url = reverse('prijava_delete', args=[1])

        self.organizator = Organizator.objects.create(
            organizator_naziv='Test Organizator',
            organizator_email='test@organizator.com'
        )

        self.sudionik = Sudionik.objects.create(
            sudionik_naziv='Test Sudionik',
            sudionik_email='test@sudionik.com'
        )

        self.natjecaj = Natjecaj.objects.create(
            natjecaj_naziv='Test Natjecaj',
            natjecaj_datum='2022-01-01',
            natjecaj_organizator=self.organizator
        )


        self.prijava = Prijava.objects.create(
            prijava_broj=1,
            prijava_natjecaj=self.natjecaj,
            prijava_sudionik=self.sudionik
        )

    def test_prijava_list_GET(self):
        response = self.client.get(self.prijava_list_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'prijave/prijava_list.html')

    def test_prijava_detail_GET(self):
        response = self.client.get(self.prijava_detail_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'prijave/prijava_detail.html')

    def test_prijava_create_GET(self):
        response = self.client.get(self.prijava_create_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'prijave/prijava_create.html')
        self.assertIsInstance(response.context['form'], PrijavaForm)

    # def test_prijava_create_POST(self):
    #     response = self.client.post(self.prijava_create_url, {
    #         'prijava_broj': 2,
    #         'prijava_natjecaj': self.natjecaj.id,
    #         'prijava_sudionik': self.sudionik.id,
    #     })

    #     self.assertRedirects(response, self.prijava_list_url)

    def test_prijava_update_GET(self):
        response = self.client.get(self.prijava_update_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'prijave/prijava_update.html')
        self.assertIsInstance(response.context['form'], PrijavaForm)

    def test_prijava_update_POST(self):
        response = self.client.post(self.prijava_update_url, {
            'prijava_natjecaj': self.natjecaj.pk,
            'prijava_sudionik': self.sudionik.pk,
            'prijava_broj': 3
        })

        self.assertRedirects(response, self.prijava_list_url)

    def test_prijava_delete_GET(self):
        response = self.client.get(self.prijava_delete_url)

        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'prijave/prijava_delete.html')
        self.assertIsInstance(response.context['form'], PrijavaDeleteForm)

    def test_prijava_delete_POST(self):
        response = self.client.post(self.prijava_delete_url)

        self.assertRedirects(response, self.prijava_list_url)

