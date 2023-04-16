from django.urls import path
from dashboard.views import *
from . import views
# from django.contrib.auth.decorators import login_required
# from django.contrib.sessions.view import SessionWizardView
# from django.contrib.formtools.wizard.views import SessionWizardView

urlpatterns = [
    path('', home),
    # path('show_session/', SessionWizardView.as_view(), name='show_session'),
    path('<int:count>/', home),
    # path('tables/', table),
    path('logout/', Logout_view),
    # path('login/<str:count>', login2),
    path('type/', usertype),
    path('signup/', signup_view),
    path('signup/vehicle', reg_vehicle),
    path('booking/', booking),
    path('booking/request/', Request),
    path('booking/request/tracking/', tracking),
    path('drequests/', driver_requests),
    path('login/', Login_view),
    path('payment/', payment),
    path('about-us/', aboutus),
    path('contact-us/', contactus),
    path('profile/', profile),


]
