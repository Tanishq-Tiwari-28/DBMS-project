# from django.contrib.auth.forms import UserCreationForm, UserChangeForm
# from django import forms
# from django.contrib.auth.models import User

# from .models import Customer


# class CustomerSignupForm(UserCreationForm):
#     email = forms.EmailField(
#         max_length=254, help_text='Required. Enter a valid email address.')
#     contact = forms.CharField(
#         max_length=12, required=False, help_text='Optional. Enter your contact number.')
#     dob = forms.DateField(
#         required=False, help_text='Optional. Enter your date of birth.')

#     class Meta:
#         model = User
#         fields = ('username', 'email', 'password1', 'password2')

#     def save(self, commit=True):
#         user = super().save(commit=False)
#         user.email = self.cleaned_data['email']
#         if commit:
#             user.save()
#             customer = Customer.objects.create(
#                 user=user,
#                 contact=self.cleaned_data['contact'],
#                 dob=self.cleaned_data['dob']
#             )
#             customer.save()
#         return user
