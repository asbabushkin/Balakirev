from django.urls import path, register_converter

from . import converters, views

register_converter(converters.FourDigitYearConverter, "year4")

urlpatterns = [
    path("", views.index, name="home"),
    path("about/", views.about, name="about"),
    path("post/<slug:post_slug>", views.show_post, name="post"),
    path("addpage/", views.addpage, name="add_page"),
    path("contact/", views.contact, name="contact"),
    path("login/", views.login, name="login"),
    path("category/<slug:cat_slug>", views.show_category, name="category"),
]
