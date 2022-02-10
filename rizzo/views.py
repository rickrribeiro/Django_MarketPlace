# from core.forms import RegisterForm
from rizzo.forms import UserCreateForm
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from .models import Category, User, Sale, Service, Message, Ngo
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.views.generic import FormView
from django.http import JsonResponse
import urllib.parse as urlparse
from urllib.parse import parse_qs
def filterFamousByName(request):
    # parsed = urlparse.urlparse(request)
    # print(parse_qs(parsed.query)['name'])
    name = request.GET.get('name')
    
    
    users = User.objects.famous(True).filterByName(name)[:5]
    print(users)
    data = []
    for user in users:
        
        print("1")
        print(user.image.name)
    
        data.append({'name':user.name, 'last_name':user.last_name,'username':user.username,'image':'/media/'+user.image.name})
    return JsonResponse(data, safe=False)

class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        users = User.objects.famous(True)
        categories_spotlight = Category.objects.spotlight(True)
         
        
        for category in categories_spotlight:
            category.total = User.objects.total_by_category(category.id)
            category.famous = User.objects.famous(True).specific_category(category)#Category.objects.get_by_name(category.name)[0]
            for famous in category.famous:
                famous.price = Service.objects.smallest_price(famous)
            
        # for user in users:
        #     user.total_donate = 
        famous_spotlight = users.spotlight(True)
        for famous in famous_spotlight:
            famous.price = Service.objects.smallest_price(famous)
        
        top_donators = Sale.objects.top_donators()

        context['top_donators'] = top_donators
        context['spotlight'] = famous_spotlight
        context['categories_spotlight'] = categories_spotlight
        
        return context

class FamousPageView(TemplateView):
    template_name = "famous-page.html"

    def get_context_data(self, **kwargs):
        context = super(FamousPageView, self).get_context_data(**kwargs)
        user = get_object_or_404(User.objects.famous(True).filter(username=kwargs['user'])) #criar queryset getbyemail e mudar isso
        top_donators = Sale.objects.top_donators()
        services = Service.objects.getServiceByFamous(user.id)
        videos = Sale.objects.getFamousProfileVideos(user.id)
        context['services'] = services
        context['top_donators'] = top_donators
        context['ranking'] = 1
        context['user'] = user
        context['videos'] = videos
        return context

class CategoryPageView(TemplateView):
    template_name = "category-page.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryPageView, self).get_context_data(**kwargs)
        category = get_object_or_404(Category.objects.get_by_name(kwargs['category']))
        category.total = User.objects.total_by_category(category.id)
        category.famous = User.objects.famous(True).specific_category(category)
        for famous in category.famous:
            famous.price = Service.objects.smallest_price(famous)
        top_donators = Sale.objects.top_donators()

        context['top_donators'] = top_donators
        context['category'] = category
        return context



class RegisterPageView(FormView):
    template_name = "registration/form-register.html"
    form_class = UserCreateForm
    success_url = reverse_lazy('index')
    
    def get_context_data(self, **kwargs):

        context = super(RegisterPageView, self).get_context_data(**kwargs)
       
        top_donators = Sale.objects.top_donators()

        context['top_donators'] = top_donators
        return context
    
    def form_valid(self, form, *args, **kwargs):
        
        user = form.save()
        
        user.save()
        return super(RegisterPageView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        
        messages.error(self.request, 'Erro ao enviar e-mail')
        print(form.errors)
        return super(RegisterPageView, self).form_invalid(form, *args, **kwargs)


    



class FamousRegisterPageView(TemplateView):
    template_name = "registration/form-famous-register.html"

    def get_context_data(self, **kwargs):
        context = super(FamousRegisterPageView, self).get_context_data(**kwargs)
       
        top_donators = Sale.objects.top_donators()

        context['top_donators'] = top_donators
        return context


class ContactFormPageView(TemplateView):
    template_name = "form-contact.html"

    def get_context_data(self, **kwargs):
        context = super(ContactFormPageView, self).get_context_data(**kwargs)
       
        top_donators = Sale.objects.top_donators()

        context['top_donators'] = top_donators
        return context

class CategoryListPageView(TemplateView):
    template_name = "category-list.html"

    def get_context_data(self, **kwargs):
        context = super(CategoryListPageView, self).get_context_data(**kwargs)
        categories = Category.objects.all()
         
        
        for category in categories:
            category.total = User.objects.total_by_category(category.id)
            category.famous = User.objects.famous(True).specific_category(category)
            for famous in category.famous:
                famous.price = Service.objects.smallest_price(famous)
        
        top_donators = Sale.objects.top_donators()
        context['top_donators'] = top_donators
        context['categories'] = categories
        return context


class NGOListPageView(TemplateView):
    template_name = "ngo-list.html"

    def get_context_data(self, **kwargs):
        context = super(NGOListPageView, self).get_context_data(**kwargs)
        ngo_list = Ngo.objects.all()
        top_donators = Sale.objects.top_donators()

        context['top_donators'] = top_donators
        context['ngo_list'] = ngo_list
        return context

class CheckoutPageView(TemplateView):
    template_name = "checkout.html"

    def get_context_data(self, **kwargs):
        context = super(CheckoutPageView, self).get_context_data(**kwargs)
        service = Service.objects.get(id=kwargs['service'])
        top_donators = Sale.objects.top_donators()

        context['top_donators'] = top_donators
        context['service'] = service
        return context



class PaymentPageView(TemplateView):
    template_name = "payment.html"

    def get_context_data(self, **kwargs):
        context = super(PaymentPageView, self).get_context_data(**kwargs)
        top_donators = Sale.objects.top_donators()
        context['top_donators'] = top_donators
        return context