import json

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.csrf import csrf_exempt
from .forms import NewUserForm, ReviewForm
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import DetailView, ListView
from django.views.generic.base import View
from .models import Perform, People, News, Category, SessionSeat


class Cat:

    def get_categories(self):
        return Category.objects.all()

    def get_pushkin(self):
        return Perform.objects.filter(pushkin=True)


class FilterPerformsView(Cat, ListView):
    model = Perform
    template_name = 'performs/affiche_search.html'

    def get_queryset(self):
        queryset = Perform.objects.filter(
            Q(pushkin__in=self.request.GET.getlist("pushkin")) |
            Q(categories__in=self.request.GET.getlist("category"))
        ).distinct()
        return queryset


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


class AddReview(View):
    """Отзывы"""
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        perform = Perform.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            if request.POST.get("parent", None):
                form.parent_id = int(request.POST.get("parent"))
            form.username = request.user
            form.perform = perform
            form.save()
        return redirect(perform.get_absolute_url())


class PerformanceDetailView(Cat, DetailView):
    """Полное описание фильма"""
    model = Perform
    queryset = Perform.objects.filter(draft=False)
    slug_field = "url"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = ReviewForm()
        return context


class ActorView(Cat, DetailView):
    """Вывод информации о актере"""
    model = People
    template_name = 'performs/people_detail.html'
    slug_field = "url"


class BookingView(Cat, DetailView):
    """Вывод информации о актере"""
    model = Perform
    template_name = 'performs/booking.html'
    slug_field = "url"


def index(request):
    performs = Perform.objects.all()
    return render(request, 'performs/index.html', {'perform': performs})


@csrf_exempt
def occupiedSeats(request):

    data = json.loads(request.body)
    perform = Perform.objects.get(title=data["perform_title"])
    occupied = perform.booked_seats.all()
    occupied_seat = list(map(lambda seat: seat.seat_no - 1, occupied))

    return JsonResponse({
        "occupied_seats": occupied_seat,
        "perform": str(perform)
    })


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


def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.success(request, "Registration successful.")
            return redirect('/')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render(request=request, template_name="performs/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect('/')
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="performs/login.html", context={"login_form": form})


def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect('/')
