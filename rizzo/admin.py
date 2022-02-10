from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserCreateForm, UserChangeForm
from .models import User, Category, ServiceType, Ngo, Service, Sale, Message,  Search




@admin.register(User)
class UserAdmin(UserAdmin):
    add_form = UserCreateForm
    form = UserChangeForm
    model = User
    list_display = ( 'username','name', 'last_name', 'email','is_famous', 'is_staff', 'spotlight')
    fieldsets = (
        ('Dados Login', {'fields': ('email', 'password')}),
        ('Informações Pessoais', {'fields': ('name',  'last_name','username', 'phone', 'cpf', 'description','facebook','instagram','youtube','twitter', 'image')}),
        ('Doação', {'fields': ('to_ngo', 'ngo_percentage',  'ngo')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser','is_famous', 'category','subcategory','spotlight', 'user_permissions')}),
        
    )

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    list_display = ('id',"name", "spotlight")

@admin.register(ServiceType)
class ServiceTypeAdmin(admin.ModelAdmin):
    model = ServiceType
    list_display = ("name",)

@admin.register(Ngo)
class NgoAdmin(admin.ModelAdmin):
    model = Ngo
    list_display = ("name",)

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    model = Service
    list_display = ("famous", 'service')

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    model = Sale
    list_display = ("customer", 'service', 'done')

@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    model = Message
    list_display = ("title", 'email', 'read')


@admin.register(Search)
class SearchAdmin(admin.ModelAdmin):
    model = Search
    list_display = ("user", 'famous', 'text')

# @admin.register(Cart)
# class CartAdmin(admin.ModelAdmin):
#     model = Cart
#     list_display = ("user", 'famous', 'text')