from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, GenreViewSet, TitleViewSet

from users.views import SignUpView, CreateTokenView

app_name = 'api'

v1_router = DefaultRouter()
v1_router.register(r"titles", TitleViewSet, basename="titles")
v1_router.register(r"categories", CategoryViewSet, basename="categories")
v1_router.register(
    r"genres", GenreViewSet, basename="genres"
)

urlpatterns = [
    path('v1/auth/signup/', SignUpView.as_view(), name='signup'),
    path('v1/auth/token/', CreateTokenView.as_view(), name='token'),
    path("v1/", include(v1_router.urls)),
]
