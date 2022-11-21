from django.urls import path
# Импортируем созданное нами представление
from .views import (PostList, PostDetail, PostListFiltered, NewsCreate, ArticleCreate, NewsUpdate,
                    ArticleUpdate, NewsDelete, ArticleDelete, IndexView, upgrade_me)



urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем товарам у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('news/', PostList.as_view(), name='List'),
   path('news/<int:pk>', PostDetail.as_view(), name='Detail'),
   path('news/search', PostListFiltered.as_view(), name='Filter'),
   path('news/create', NewsCreate.as_view(), name='NewsCreate'),
   path('news/<int:pk>/update', NewsUpdate.as_view(), name='NewsUpdate'),
   path('news/<int:pk>/delete', NewsDelete.as_view(), name='NewsDelete'),
   path('articles/create', ArticleCreate.as_view(), name='ArticleCreate'),
   path('articles/<int:pk>/update', ArticleUpdate.as_view(), name='ArticleUpdate'),
   path('articles/<int:pk>/delete', ArticleDelete.as_view(), name='ArticleDelete'),
   path('user/', IndexView.as_view(), name='UserPage'),
   path('user/upgrade', upgrade_me, name='Upgrade'),
   ]