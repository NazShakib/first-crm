from django.urls import path
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [

    path('register/',views.register,name='register'),
    path('login/',views.logedin,name='login'),
    path('logout/',views.logedout, name='logout'),

    path('', views.home, name= 'home'),
    path('products/', views.products, name='product'),
    path('user/',views.user,name='user'),
    path('settings/',views.settings,name='setting'),
    path('customer/<str:customer_id>/', views.customers, name ='customer'),
    path('create_order/<str:pk>/',views.createOrder, name='create_order'),
    path('update_order/<str:pk>/',views.updateOrder, name='update_order'),
    path('delete_order/<str:pk_del>/',views.deleteOrder, name='delete_order'),

# password reset 
    path('reset_password/',auth_view.PasswordResetView.as_view(template_name='accounts/password_reset.html'),name='reset_password'),
    path('reset_password_sent/',auth_view.PasswordResetDoneView.as_view(template_name='accounts/password_reset_sent.html'),name='password_reset_done'),
    path('reset/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_form.html'),name='password_reset_confirm'),
    path('reset_password_complete/',auth_view.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_done.html'),name='password_reset_complete'),
    
    # path()

]



'''
1 - Submit email form                         //PasswordResetView.as_view()
2 - Email sent success message                //PasswordResetDoneView.as_view()
3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
4 - Password successfully changed message     //PasswordResetCompleteView.as_view()
'''