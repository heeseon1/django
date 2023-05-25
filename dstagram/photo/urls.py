from django.urls import path
from .views import *
from .models import Photo


app_name = 'photo' # 네임 스페이스 지정 (앱 이름)

urlpatterns = [
    path('', PhotoViews.as_view(), name='photo_list'),
    path('detail/<int:pk>/', PhotoDetailView.as_view(), name='photo_detail'),
    path('upload/', PhotoUploadView.as_view(), name='photo_upload'),
    path('delete/<int:pk>/', PhotoDeleteView.as_view(), name='photo_delete'),
    path('update/<int:pk>/', PhotoUpdateView.as_view(), name='photo_update'),
]
