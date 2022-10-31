from django.urls import path

from . import views

app_name='diary'
urlpatterns = [
    path('',views.IndexView.as_view(),name="index"),
    path('inquiry/',views.InquiryView.as_view(),name="inquiry"),
    path('diary-list/',views.DiaryListView.as_view(),name="diary_list"),
    path('diary-list/<slug:pk>',views.DiaryListView.as_view(),name="diary_list"),
    path('diary-detail/<int:pk>',views.DiaryDetailView.as_view(),name="diary_detail"),
    path('my-diary-list/',views.MyDiaryListView.as_view(),name="my_diary_list"),
    path('my-diary-detail/<int:pk>/',views.MyDiaryDetailView.as_view(),name="my_diary_detail"),
    path('my-diary-create/',views.MyDiaryCreateView.as_view(),name="my_diary_create"),
    path('my-diary-update/<int:pk>',views.MyDiaryUpdateView.as_view(),name="my_diary_update"),
    path('my-diary-delete/<int:pk>',views.MyDiaryDeleteView.as_view(),name="my_diary_delete"),
]