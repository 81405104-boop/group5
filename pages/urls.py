from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("card/<int:n>/", views.card, name="card"),  # 新增：第 n 個卡片內頁
]
