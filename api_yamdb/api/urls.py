from django.urls import include, path

from users.views import SignUpView, CreateTokenView

app_name = 'api'


urlpatterns = [
    path('v1/auth/signup/', SignUpView.as_view(), name='signup'),
    path('v1/auth/token/', CreateTokenView.as_view(), name='token'),
]
