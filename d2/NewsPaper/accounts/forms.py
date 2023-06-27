from allauth.account.forms import SignupForm
from django.contrib.auth.models import Group
from django.core.mail import send_mail


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)

        send_mail(
            subject='Поздравляем с регистрацией на нашем новостном портале!',
            message=f'{user.username}, вы успешно зарегистрировались!',
            from_email=None,  # будет использовано значение DEFAULT_FROM_EMAIL
            recipient_list=[user.email],
        )

        return user