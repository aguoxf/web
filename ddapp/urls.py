from django.contrib import admin
from django.urls import path
app_name='ddapp'
from ddapp import views
urlpatterns = [
    path('index/',views.index,name='index'),
    path('booklist/',views.booklist,name='booklist'),
    path('login/',views.login,name='login'),
    path('regist/', views.regist, name='regist'),
    path('login_logic/', views.login_logic, name='login_logic'),
    path('regist_logic/', views.regist_logic, name='regist_logic'),
    path('getcaptcha/',views.getcaptcha,name='getcaptcha'),
    path('yzm_logic/', views.yzm_logic, name='yzm_logic'),
    path('regist_l/',views.regist_l,name='regist_l'),
    path('register_ok/',views.register_ok,name='register_ok'),
    path('car/',views.car,name='car'),
    path('add_car/',views.add_car,name='add_car'),
    path('bookde/', views.bookde, name='bookde'),
    path('del_car/', views.del_car, name='del_car'),
    path('change_car/', views.change_car, name='change_car'),
    path('indent/', views.indent, name='indent'),
    path('closing/', views.closing, name='closing'),
    path('indent_add/', views.indent_add, name='indent_add'),
    path('indent_ok/', views.indent_ok, name='indent_ok'),
    path('change/', views.change, name='change'),
    path('book_de2/', views.book_de2, name='book_de2'),


]
