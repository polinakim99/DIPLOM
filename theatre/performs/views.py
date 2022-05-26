from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.base import View
from .models import Perform, People, News, Category
from .forms import UserRegistrationForm, LoginForm


class Cat:

    def get_category(self):
        return Category.objects.all()


class FilterPerformsView(Cat, ListView):
    model = Perform
    template_name = 'performs/affiche_search.html'

    def get_queryset(self):
        queryset = Perform.objects.filter(category__in=self.request.GET.getlist("category")).distinct()
        return queryset

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context["category"] = ''.join([f"category={x}&" for x in self.request.GET.getlist("category")])
        return context


class Search(ListView):
    model = Perform
    template_name = 'performs/affiche_search.html'

    def get_queryset(self):  # новый
        q = self.request.GET.get('q')
        a = "".join(q[0].upper()) + q[1:]
        object_list = Perform.objects.filter(
            Q(title__icontains=a)
        )
        return object_list


class NewsView(View):
    model = News
    template_name = 'performs/news_detail.html'
    slug_field = "url"


class NewsDetailView(DetailView):
    model = News
    slug_field = "url"


class PerformanceView(Cat, ListView):
    model = Perform
    queryset = Perform.objects.filter(draft=False)
    template_name = 'performs/perform_detail.html'
    slug_field = "url"


class PerformanceDetailView(Cat, DetailView):
    """Полное описание фильма"""
    model = Perform
    queryset = Perform.objects.filter(draft=False)
    slug_field = "url"


class ActorView(Cat, DetailView):
    """Вывод информации о актере"""
    model = People
    template_name = 'performs/people_detail.html'
    slug_field = "url"


def index(request):
    performs = Perform.objects.all()
    return render(request, 'performs/index.html', {'perform': performs})


def about(request):
    return render(request, 'performs/about.html')


def news(request):
    news = News.objects.all()
    return render(request, 'performs/news.html', {'news': news})


def contact(request):
    return render(request, 'performs/contact.html')


def affiche(request):
    performs = Perform.objects.all()
    return render(request, 'performs/affiche.html', {'perform': performs})


def people(request):
    people = People.objects.all()
    return render(request, 'performs/people.html', {'people': people})


class LoginView(View):
    def get(self, request):
        form = LoginForm(request.POST or None)
        context = {'form': form}
        return render(request, 'performs/login.html', context)

    def post(self, request):
        form = LoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('/')
        return render(request, 'performs/login.html', {'form': form})


def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # Create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # Save the User object
            new_user.save()
            return render(request, 'performs/register_done_.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'performs/register.html', {'user_form': user_form})


def logout_user(request):
    logout(request)
    return redirect('login')
