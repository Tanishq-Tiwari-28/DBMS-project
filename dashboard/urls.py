from django.urls import path
from dashboard.views import *
from . import views
# from django.contrib.auth.decorators import login_required
# from django.contrib.sessions.view import SessionWizardView
# from django.contrib.formtools.wizard.views import SessionWizardView

urlpatterns = [
    path('', home),
    # path('show_session/', SessionWizardView.as_view(), name='show_session'),
    path('customer/', home),
    path('driver/', home),
    # path('tables/', table),
    path('logout/', Logout_view),
    # path('login/<str:count>', login2),
    path('type/', usertype),
    path('passwordchange/', passwordchange),
    path('updateprofile/', updateprofile),
    path('addphone/', addphone),
    path('signup/', signup_view),
    path('signup/vehicle', reg_vehicle),
    path('booking/', booking),
    path('booking/request/', Request),
    path('request/dtracking', driver_tracking),
    path('booking/request/tracking/', tracking),
    path('drequests/', driver_requests),
    path('login/', Login_view),
    path('payment/', payment),
    path('about-us/', aboutus),
    path('contact-us/', contactus),
    path('profile/', profile),
    path('goodbye/', account_delete)
]
