from django.urls import path
from . import views

urlpatterns = [
    path('', views.PeakListAPIView.as_view(), name='peak_list'),
    path('create/', views.PeakCreateAPIView.as_view(), name='peak_create'),
    path('update/<int:id>/', views.PeakRetrieveUpdateAPIView.as_view(), name='peak_update'),
    path('delete/<int:id>/', views.PeakDestroyAPIView.as_view(), name='peak_delete'),
    path('delete/all/', views.destroy, name='peak_delete_all'),
    path('<int:id>/', views.map, name='map'),
    path('ingest', views.ingest, name='ingest'),
]