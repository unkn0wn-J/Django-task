from django.contrib import admin
from django.urls import path, include
from todo.views import todo_list, todo_info
from users import views as user_views
from django.shortcuts import redirect # 👈 1. redirect 임포트 확인!

urlpatterns = [
    # 2. 메인 주소('')로 들어오면 바로 'login'으로 던져버리기
    path('', lambda r: redirect('login'), name='index'),

    path('todo/', todo_list, name='todo_list'),
    path('todo/<int:todo_id>/', todo_info, name='todo_info'),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/', user_views.login, name='login'),
    path('signup/', user_views.sign_up, name='signup')
]