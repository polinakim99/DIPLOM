import datetime

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils import timezone


class Category(models.Model):

    name = models.CharField("Категория", max_length=150)
    description = models.TextField("Описание")
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class People(models.Model):

    name = models.CharField("Имя", max_length=150)
    surname = models.CharField("Фамилия", max_length=150)
    position = models.CharField("Должность", max_length=150, default="")
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="people/")
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.surname

    def get_absolute_url(self):
        return reverse('person_detail', kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class Seat(models.Model):

    seat_no = models.IntegerField("Номер сидения")
    row_no = models.IntegerField("Номер ряда")

    def __str__(self) -> str:
        return f"Ряд {self.row_no}, Место {self.seat_no}"

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"


class Perform(models.Model):

    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    poster = models.ImageField("Изображение", upload_to="perform/")
    preview = models.ImageField("Превью", upload_to="perform/", default="sdsd")
    directors = models.ManyToManyField(People, verbose_name="режиссер", related_name="perform_director")
    actors = models.ManyToManyField(People, verbose_name="актер", related_name="perform_actor")
    composer = models.ManyToManyField(People, verbose_name="композитор", related_name="perform_composer",
                                      default="Голланд")
    choreographer = models.ManyToManyField(People, verbose_name="хореограф", related_name="perform_choreographer")
    artist = models.ManyToManyField(People, verbose_name="художник", related_name="perform_artist")
    categories = models.ManyToManyField(Category, verbose_name="категории", default="жбр")
    url = models.SlugField(max_length=160, unique=True)
    price = models.IntegerField("Цена билета", default=500)
    date1 = models.DateTimeField("Выступление_1", default=timezone.now)
    date2 = models.DateTimeField("Выступление_2", default=timezone.now)
    date3 = models.DateTimeField("Выступление_3", default=timezone.now)
    draft = models.BooleanField("Черновик", default=False)
    pushkin = models.BooleanField("Пушкинская карта", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("perform_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Спектакль"
        verbose_name_plural = "Спектакли"


class Session(models.Model):
    perform = models.ForeignKey(Perform, verbose_name="Спектакль", on_delete=models.CASCADE)
    date_time = models.DateTimeField("Выступление_1", default=timezone.now)

    def __str__(self) -> str:
        return f"{self.perform}: {self.date_time}"

    class Meta:
        verbose_name = "Сеанс"
        verbose_name_plural = "Сеансы"


class SessionSeat(models.Model):
    seat = models.ForeignKey(Seat, verbose_name="Место", on_delete=models.CASCADE)
    session = models.ForeignKey(Session, verbose_name="Сеанс", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.seat}: {self.session}"

    class Meta:
        verbose_name = "Распределение мест"
        verbose_name_plural = "Распределения мест"


class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    session_seat = models.ManyToManyField(SessionSeat, verbose_name="сеанс-место", related_name="session_seat")


class PerformShots(models.Model):

    title = models.CharField("Название", max_length=100)
    perform = models.ForeignKey(Perform, verbose_name="Спектакль", on_delete=models.CASCADE)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="perform_shorts/")
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фотография"
        verbose_name_plural = "Фотографии"


class Reviews(models.Model):
    username = models.ForeignKey(User, verbose_name="Пользователь", on_delete=models.CASCADE, default=0)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    perform = models.ForeignKey(Perform, verbose_name="спектакль", on_delete=models.CASCADE)
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерация", default=True)

    def __str__(self):
        return f"{self.username} - {self.perform}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Comments(models.Model):
    """Класс комментариев
    """
    username = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE)
    perform = models.ForeignKey(
         Perform,
         verbose_name="Спектакль",
         on_delete=models.CASCADE)
    text = models.TextField("")
    created = models.DateTimeField("Дата добавления", auto_now_add=True, null=True)
    moderation = models.BooleanField("Модерация", default=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

    def __str__(self):
        return "{}".format(self.username)


class News(models.Model):

    title = models.CharField("Заголовок", max_length=150)
    description = models.TextField("Описание")
    preview = models.TextField("Краткое описание", default="Новость")
    date = models.DateField("Дата")
    url = models.SlugField(max_length=100)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("news_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"
