from django.shortcuts import render
from django.views import generic
from .models import Film, Producer, FilmRent, Genre
# Create your views here.

def index(request):
    #Генерация количества главных объектов
    num_films = Film.objects.all().count()
    num_rents = FilmRent.objects.all().count()
    #Доступные фильмы (фильтрация по статусу "а")
    num_rents_available = FilmRent.objects.filter(status__exact = 'a').count()
    num_producers = Producer.objects.count() #Метод 'all()' по умолчанию
    num_genres = Genre.objects.count()
    name_film = Film.objects.filter(title__icontains = 'dark').count()
    return render(request, "index.html",
           context=
                {'num_films': num_films,'num_rents': num_rents, 'num_rents_available': num_rents_available,
                  'num_producers': num_producers, 'num_genres': num_genres, 'name_film': name_film
                }
           )

class FilmListView(generic.ListView):  #oтображение выполнит запрос к базе данных, получит все записи заданной модели (Film),
                                        # затем отрендерит (отрисует) соответствующий шаблон, расположенный
    model = Film
    paginate_by = 3
    #context_object_name = 'my_film_list'   # ваше собственное имя переменной контекста в шаблоне
    #queryset = Film.objects.filter(title__icontains='dark')[:5] # Получение 5 фильмов, содержащих слово 'dark' в заголовке
    #template_name = 'books/my_arbitrary_template_name_list.html'  # Определение имени вашего шаблона и его расположения
    # def get_queryset(self):
    #     return Film.objects.filter(title__icontains='dark')[:5]  # Получить 5 фильмов, содержащих 'dark' в заголовке

    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(FilmListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['some_data'] = 'This is just some data'
        return context

class FilmDetailView(generic.DetailView):
    model = Film

class ProducerListView(generic.ListView):
    model = Producer
    paginate_by = 3
    def get_context_data(self, **kwargs):
        # В первую очередь получаем базовую реализацию контекста
        context = super(ProducerListView, self).get_context_data(**kwargs)
        # Добавляем новую переменную к контексту и иниуиализируем ее некоторым значением
        context['some_data'] = 'This is just some data'
        return context

class ProducerDetailView(generic.DetailView):
    model = Producer