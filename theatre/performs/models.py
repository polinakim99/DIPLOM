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
    category = models.ForeignKey(Category, verbose_name="Категория", on_delete=models.SET_NULL, null=True)
    url = models.SlugField(max_length=160, unique=True)
    date1 = models.DateTimeField("Выступление_1", default=timezone.now)
    date2 = models.DateTimeField("Выступление_2", default=timezone.now)
    date3 = models.DateTimeField("Выступление_3", default=timezone.now)
    draft = models.BooleanField("Черновик", default=False)
    pushkin = models.BooleanField("Пушкинская карта", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("perform_detail", kwargs={"slug": self.url})

    class Meta:
        verbose_name = "Спектакль"
        verbose_name_plural = "Спектакли"


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


class RatingStar(models.Model):

    value = models.PositiveSmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):

    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    perform = models.ForeignKey(Perform, on_delete=models.CASCADE, verbose_name="спектакль")

    def __str__(self):
        return f"{self.star} - {self.perform}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Reviews(models.Model):

    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey('self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True)
    perform = models.ForeignKey(Perform, verbose_name="спектакль", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} - {self.perform}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


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
