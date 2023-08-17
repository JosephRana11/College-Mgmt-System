from django.urls import path 
from .views import home_view , login_view , logout_view , select_account_type , student_registration , professor_registration

urlpatterns = [
    path('' , home_view , name= 'home'),
    path('home' , home_view , name= 'home'),
    path('login' , login_view , name='login'),
    path('logout' , logout_view , name='logout'),
    path('select-account-type' , select_account_type , name = 'select-account-type'),
    path('student-register' , student_registration , name= 'student-registration'),
    path('professor-register' , professor_registration , name = 'professor-registration'),
]
