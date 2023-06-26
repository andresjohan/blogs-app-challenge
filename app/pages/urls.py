from django.urls import path
from .views import ArticleListView,ArticleDetailView,AuthorCreate,PageUpdate,PageDelete,UpdateView2


urlpatterns = [
    path('<int:pk>/<slug:slug>/',ArticleDetailView.as_view(), name='page'),
    path('pagina/',ArticleListView.as_view(), name='pages'),
    path('create/',AuthorCreate.as_view(),name='create'),
    path('update/<int:pk>/',PageUpdate.as_view(),name='update'),
    path('update2/<int:pk>/',UpdateView2.as_view(),name='update2'),
    path('delete/<int:pk>/',PageDelete.as_view(),name='delete'),
  

]