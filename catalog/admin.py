from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Film)
#admin.site.register(Producer)
admin.site.register(Genre)
#admin.site.register(FilmRent)
admin.site.register(Language)

class FilmInline(admin.TabularInline): #Встроенное редактирование связанных записей
    model = Film
    extra = 0 #Удаляет лишние экземпляры книг

# Define the admin class
class ProducerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] #  Кортежи - отображение горизонтально
    inlines = [FilmInline]  #Встроеный список фильмов в представлении Продюсер
                                                                             # (вертикально по умолчанию)

# Register the admin class with the associated model
admin.site.register(Producer, ProducerAdmin)

# Register the Admin classes for Film using the decorator - do the same as admin.site.register(Film,FilmAdmin)

class FilmsRentInline(admin.TabularInline): #Встроенное редактирование связанных записей
    model = FilmRent

    extra = 0 #Удаляет лишние экземпляры книг


@admin.register(Film)
class FilmAdmin(admin.ModelAdmin):
    list_display = ('title', 'producer', 'display_genre') #К сожалению, мы не можем напрямую
    inlines = [FilmsRentInline]                                                # поместить поле genre в list_display, так как оно является
                                                            # ManyToManyField (Django не позволяет это из-за большой "стоимости"
                                                            # доступа к базе данных). Вместо этого мы определим функцию display
                                                            #genre для получения строкового представления информации
                                                             # (вызов этой функции есть в list_display,  ее определение см. ниже).

# Register the Admin classes for FilmRent using the decorator

@admin.register(FilmRent)
class FilmRentAdmin(admin.ModelAdmin):
    list_display = ('id', 'film', 'status', 'due_back') #представление
    list_filter = ('status', 'due_back') #Фильтр
    fieldsets = (
        (None, {                 #Разделение на секции
            'fields': ('film', 'imprint', 'id')
        }),
        ('Availability', #заголовок секции,
        {
            'fields': ('status', 'due_back')
        }),
    )

