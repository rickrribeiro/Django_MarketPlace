from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.fields import CharField
from stdimage.models import StdImageField
from .helpers import get_file_path
from .querysets import CategoryQuerySet, UserQuerySet, SaleQuerySet, ServiceQuerySet
############################################ User Models ############################################
class Base(models.Model):
    created = models.DateField("Criação", auto_now_add=True) #mudar p created e migrar
    modified = models.DateField("Atualização", auto_now=True)
    active = models.BooleanField("Ativo?", default=True)

    class Meta:
        abstract = True


class UsuarioManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError('O e-mail é obrigatório')
        
        email = self.normalize_email(email)
        
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
       
        extra_fields.setdefault('is_superuser', False)
        return self._create_user( email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser precisa ter is_superuser=True')

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser precisa ter is_staff=True')

        return self._create_user(email, password, **extra_fields)
    
    def get_queryset(self):
        return UserQuerySet(self.model)

    def __getattr__(self, attr, *args):
        if(attr.startswith("_")):
            raise AttributeError
        return getattr(self.get_queryset(), attr, *args)

#adicionar foreingkey para serviços(botar preço), lista de videos
class User(AbstractUser): 
    #common
    email = models.EmailField('E-mail', max_length=60, unique=True)
    name = models.CharField('Nome', max_length=30)
    last_name = models.CharField('Sobrenome', max_length=50, blank=True,null=True)
    username = models.CharField('Usuário', max_length=30, unique=True, blank=True,null=True)
    phone = models.CharField('Telefone', max_length=15, blank=True,null=True) #validar e mudar p PHONE
    image = StdImageField('Foto do perfil', upload_to = get_file_path, variations={"thumb": {"width": 480, "height": 480, "crop": True}}, blank=True, null=True, default='default_profile.png') #remover null = true quando resetar
    is_staff = models.BooleanField('Membro da equipe', default=False)
    is_famous = models.BooleanField('Famoso', default=False)
    #Famous
    instagram = models.CharField('Instagram', max_length=15, blank=True,null=True)
    facebook = models.CharField('Facebook', max_length=15,blank=True, null=True)
    twitter = models.CharField('Twitter', max_length=15,blank=True, null=True)
    youtube = models.CharField('Youtube', max_length=15, blank=True,null=True)
    category = models.ForeignKey("rizzo.Category",related_name="user_category",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
    subcategory = models.CharField('subcategory', max_length=70, blank=True,null=True)
    description = models.CharField('Descrição', max_length=600, blank=True,null=True)
    spotlight = models.BooleanField('Destaque', default=False)
    intro_video = models.FileField(upload_to='uploads/intro/', blank=True,null=True)
    to_ngo = models.BooleanField('Para ONGs', default = False)
    ngo =  models.ForeignKey("rizzo.NGO",related_name="ngo",
        blank=True,
        null=True,
        on_delete=models.SET_NULL)
    ngo_percentage = models.IntegerField('Porcentagem da ONG', blank=True,null=True, default=0,validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ])
    #customer
    cpf =  models.CharField('CPF', max_length=14, blank=True,null=True)

    #------------------------------------------------
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username'] #ver oq é isso

    objects = UsuarioManager()
    
    def __str__(self):
        if(self.username):
            return self.username
        else:
            return self.name


############################################ END User Models ############################################

class CategoryManager(models.Manager):
    def get_queryset(self):
        return CategoryQuerySet(self.model)

    def __getattr__(self, attr, *args):
        if(attr.startswith("_")):
            raise AttributeError
        return getattr(self.get_queryset(), attr, *args)


class Category(Base):
    name = models.CharField('Nome', max_length=30)
    image = StdImageField('Imagem', upload_to = get_file_path, variations={"thumb": {"width": 480, "height": 480, "crop": True}})
    spotlight = models.BooleanField('Destaque', default=False)
    icon =  StdImageField('Icone', upload_to = get_file_path, variations={"thumb": {"width": 40, "height": 40, "crop": True}}, null=True)#remover o null = true quando resetar

    objects = CategoryManager()

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"

    def __str__(self):
        return self.name

class Ngo(Base):
    name = models.CharField('Nome', max_length=60)
    adress = models.CharField('Endereço', max_length=80)
    phone = models.CharField('Telefone', max_length=15)
    email =  models.CharField('Email', max_length=40)
    description = models.CharField('Descrição', max_length=500)
    image = StdImageField('Foto do perfil', upload_to = get_file_path, variations={"thumb": {"width": 480, "height": 480, "crop": True}}, blank=True, null=True) #remover null = true quando resetar
    class Meta:
        verbose_name = "Ong"
        verbose_name_plural = "ONGs"

    def __str__(self):
        return self.name

class ServiceType(Base):
    name = models.CharField('Nome', max_length=40)
    description = models.CharField('Description', max_length=180)
    class Meta:
        verbose_name = "Tipo de Serviço"
        verbose_name_plural = "Tipo de Serviços"

    def __str__(self):
        return self.name

class ServiceManager(models.Manager):
    def get_queryset(self):
        return ServiceQuerySet(self.model)

    def __getattr__(self, attr, *args):
        if(attr.startswith("_")):
            raise AttributeError
        return getattr(self.get_queryset(), attr, *args)

class Service(Base):
    famous =  models.ForeignKey("rizzo.User",related_name="service_user",
        on_delete=models.CASCADE)

    service =  models.ForeignKey("rizzo.ServiceType",related_name="servicetype",
        on_delete=models.CASCADE)
    
    price = models.IntegerField('Preço')
    
    deliver_time =  models.IntegerField('Tempo de entrega (Dias)')

    objects = ServiceManager()

    class Meta:
        verbose_name = "Serviço"
        verbose_name_plural = "Serviços"

    def __str__(self):
        return self.famous.username+" - "+self.service.name

class SaleManager(models.Manager):
    def get_queryset(self):
        return SaleQuerySet(self.model)

    def __getattr__(self, attr, *args):
        if(attr.startswith("_")):
            raise AttributeError
        return getattr(self.get_queryset(), attr, *args)

class Sale(Base):
    customer =  models.ForeignKey("rizzo.User",related_name="sale_customer",
        on_delete=models.SET_NULL, blank=True, null=True)
    service =  models.ForeignKey("rizzo.service", related_name="sale_service",
        on_delete=models.SET_NULL, blank=True, null=True)
    done = models.BooleanField('Done', default=False) #set true when done by the famous and the customer can set false if has some problem
    payed = models.BooleanField('Payed', default=False)
    rating = models.IntegerField('Avaliação', blank=True, null=True)
    customerMessage = models.CharField('Mensagem do Cliente', max_length=300, blank=True, null=True)
    famousMessage = models.CharField('Mensagem do Famoso', max_length=300, blank=True, null=True)
    toProfile = models.BooleanField('Aparece no Perfil', default=False)
    ##for earch service
    video = models.FileField(upload_to='uploads/%Y/%m/%d/', null = True, blank=True)
    link = models.CharField('Link', max_length=200, blank=True, null=True) #zoom ou game
    saleCode = models.CharField('Código da venda', max_length=30,  blank=True, null=True, unique=True)
    objects = SaleManager()
    class Meta:
        verbose_name = "Venda"
        verbose_name_plural = "Vendas"

    def __str__(self):
        return 'Venda'

class Message(Base):
    title = models.CharField('Titulo', max_length=40 )
    email = models.EmailField('E-mail')
    phone = models.CharField('Telefone', max_length=15, blank=True,null=True) #validar
    description = models.CharField('Descrição', max_length=600)
    image = StdImageField('Foto do problema', upload_to = get_file_path, blank=True, null=True)
    
    read = models.BooleanField('Done', default=False)

class Search(Base):
    user =  models.ForeignKey("rizzo.User",related_name="search_user",
        on_delete=models.CASCADE, blank = True, null = True) # Null p anonimo
    famous =  models.ForeignKey("rizzo.User",related_name="searched_famous",
        on_delete=models.CASCADE, blank = True, null = True)
    text = CharField('Texto Pesquisado', max_length=100, blank=True, null=True)


# class Cart(Base):
#     user =  models.ForeignKey("core.User",related_name="cart_user",
#         on_delete=models.CASCADE)