from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = 'index'),

    path('films/', views.FilmListView.as_view(), name = 'films'),
    path('film/<int:pk>/', views.FilmDetailView.as_view(), name = 'film-detail' ), #Обобщенный класс отображения подробной
                                                                               # информации ожидает получить параметр с именем pk, можно использовать id
    path('producers/', views.ProducerListView.as_view(), name = 'producers'),
    path('producer/<int:pk>', views.ProducerDetailView.as_view(), name = 'producer-detail'),

]