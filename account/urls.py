from django.urls import path

from account.views import signIn, signup, logoutAccount

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', signIn, name='signin'),
    path('logout/', logoutAccount, name='logout'),
]
