# <project>/<app>/management/commands/seed.py
from django.core.management.base import BaseCommand
import random
from rizzo.models import Category, ServiceType, User, Service
# python manage.py seed --mode=refresh

""" Clear all data and creates addresses """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create any object """
MODE_CLEAR = 'clear'

class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    print("Delete Address instances")
    # Address.objects.all().delete()


def create_categories():
    
    print("Creating categories")
    
    category = Category(
        name="Category-1",
        icon=None,
        spotlight=True,
        image=None
    )
    category.save()
    category = Category(
        name="Category-2",
        icon=None,
        spotlight=True,
        image=None
    )
    category.save()
    category = Category(
        name="Category-3",
        icon=None,
        spotlight=True,
        image=None
    )
    category.save()
    category = Category(
        name="Category-4",
        icon=None,
        spotlight=True,
        image=None
    )
    category.save()
    category = Category(
        name="Category-5",
        icon=None,
        spotlight=True,
        image=None
    )
    category.save()
    category = Category(
        name="Category-6",
        icon=None,
        spotlight=True,
        image=None
    )
    category.save()
    print("Categorias criadas!")
    return category

def create_serviceType():
    
    print("Creating service type")
    
    servicetype = ServiceType(
        name="service_type-1",
        description="Send a video"
    )
    servicetype.save()
    servicetype = ServiceType(
        name="service_type-1",
        description="Send a video"
    )
    servicetype.save()
    print("Tipos de serviço criadas!")
    return servicetype

def create_user(category):
    
    print("Creating User")
    
    user = User(
        email="name1@gmail.com",
        name="name1",
        last_name="lastname1",
        username="username1",
        phone="+5571999999999",
        is_staff=False,
        is_famous=True,
        instagram="rickrribeiro",
        category = category,
        subcategory="subcategory1",
        description="Hello, world!",
        spotlight=True,
        to_ngo = False,
        password="123456"
    )
    user.save()
    user = User(
        email="name2@gmail.com",
        name="name2",
        last_name="lastname2",
        username="username2",
        phone="+5572999999999",
        is_staff=False,
        is_famous=True,
        instagram="rickrribeiro",
        category = category,
        subcategory="subcategory2",
        description="Hello, world!",
        spotlight=True,
        to_ngo = False,
        password="123456"
    )
    user.save()
    user = User(
        email="name3@gmail.com",
        name="name3",
        last_name="lastname3",
        username="username3",
        phone="+5573999999999",
        is_staff=False,
        is_famous=True,
        instagram="rickrribeiro",
        category = category,
        subcategory="subcategory3",
        description="Hello, world!",
        spotlight=True,
        to_ngo = False,
        password="123456"
    )
    user.save()
    user = User(
        email="name4@gmail.com",
        name="name4",
        last_name="lastname4",
        username="username4",
        phone="+5574999999999",
        is_staff=False,
        is_famous=True,
        instagram="rickrribeiro",
        category = category,
        subcategory="subcategory4",
        description="Hello, world!",
        spotlight=True,
        to_ngo = False,
        password="123456"
    )
    user.save()
    user = User(
        email="name5@gmail.com",
        name="name5",
        last_name="lastname5",
        username="username5",
        phone="+5575999999999",
        is_staff=False,
        is_famous=True,
        instagram="rickrribeiro",
        category = category,
        subcategory="subcategory5",
        description="Hello, world!",
        spotlight=True,
        to_ngo = False,
        password="123456"
    )
    user.save()
    user = User(
        email="name16@gmail.com",
        name="name6",
        last_name="lastname6",
        username="username6",
        phone="+5576999999999",
        is_staff=False,
        is_famous=True,
        instagram="rickrribeiro",
        category = category,
        subcategory="subcategory6",
        description="Hello, world!",
        spotlight=True,
        to_ngo = False,
        password="123456"
    )
    user.save()
    user = User(
        email="name7@gmail.com",
        name="name7",
        last_name="lastname7",
        username="username7",
        phone="+5577999999999",
        is_staff=False,
        is_famous=True,
        instagram="rickrribeiro",
        category = category,
        subcategory="subcategory7",
        description="Hello, world!",
        spotlight=True,
        to_ngo = False,
        password="123456"
    )
    user.save()
    print("Usuários criadas!")
    return user

def create_service(sType, famous):
    
    print("Creating service type")
    
    service = Service(
        famous = famous,
        service= sType,
        price= 100,
        deliver_time = 6
    )
    service.save()
    
    print("Tipos de serviço criadas!")
    return service

def run_seed(self, mode):
    """ Seed database based on mode

    :param mode: refresh / clear 
    :return:
    """
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    
    category = create_categories()
    sType = create_serviceType()
    user = create_user(category)
    create_service(sType, user)