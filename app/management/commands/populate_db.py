from django.core.management.base import BaseCommand
from app.models import Menu, MenuItem

class Command(BaseCommand):
    help = 'Populates the database with test data'

    def handle(self, *args, **kwargs):
        MenuItem.objects.all().delete()
        Menu.objects.all().delete()

        main_menu = Menu.objects.create(name='main_menu')
        footer_menu = Menu.objects.create(name='footer_menu')
        sidebar_menu = Menu.objects.create(name='sidebar_menu')

        home = MenuItem.objects.create(menu=main_menu, name='Home', url='/')
        about = MenuItem.objects.create(menu=main_menu, name='About', url='/about/')
        services = MenuItem.objects.create(menu=main_menu, name='Services', url='/services/')
        contact = MenuItem.objects.create(menu=main_menu, name='Contact', url='/contact/')

        web_development = MenuItem.objects.create(menu=main_menu, name='Web Development', url='/services/web-development/', parent=services)
        mobile_development = MenuItem.objects.create(menu=main_menu, name='Mobile Development', url='/services/mobile-development/', parent=services)
        seo_services = MenuItem.objects.create(menu=main_menu, name='SEO Services', url='/services/seo-services/', parent=services)

        frontend = MenuItem.objects.create(menu=main_menu, name='Frontend Development', url='/services/web-development/frontend/', parent=web_development)
        backend = MenuItem.objects.create(menu=main_menu, name='Backend Development', url='/services/web-development/backend/', parent=web_development)

        privacy_policy = MenuItem.objects.create(menu=footer_menu, name='Privacy Policy', url='/privacy-policy/')
        terms_of_service = MenuItem.objects.create(menu=footer_menu, name='Terms of Service', url='/terms-of-service/')
        contact_footer = MenuItem.objects.create(menu=footer_menu, name='Contact Us', url='/contact-us/')

        email_contact = MenuItem.objects.create(menu=footer_menu, name='Email Us', url='/contact-us/email/', parent=contact_footer)
        phone_contact = MenuItem.objects.create(menu=footer_menu, name='Call Us', url='/contact-us/phone/', parent=contact_footer)

        dashboard = MenuItem.objects.create(menu=sidebar_menu, name='Dashboard', url='/dashboard/')
        profile = MenuItem.objects.create(menu=sidebar_menu, name='Profile', url='/profile/')
        settings = MenuItem.objects.create(menu=sidebar_menu, name='Settings', url='/settings/')

        account_settings = MenuItem.objects.create(menu=sidebar_menu, name='Account Settings', url='/settings/account/', parent=settings)
        privacy_settings = MenuItem.objects.create(menu=sidebar_menu, name='Privacy Settings', url='/settings/privacy/', parent=settings)

        self.stdout.write(self.style.SUCCESS('Database populated with test data.'))
