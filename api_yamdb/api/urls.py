from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import CategoryViewSet, CommentViewSet, GenreViewSet, ReviewsViewSet, TitleViewSet

from users.views import SignUpView, CreateTokenView

app_name = 'api'

router_v1 = DefaultRouter()

router_v1.register(r"titles", TitleViewSet, basename="titles")
router_v1.register(r'titles/(?P<title_id>\d+)/reviews', ReviewsViewSet, basename='reviews')
router_v1.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentViewSet, basename='comments')
router_v1.register(r"categories", CategoryViewSet, basename="categories")
router_v1.register(r"genres", GenreViewSet, basename="genres")

urlpatterns = [
    path('v1/auth/signup/', SignUpView.as_view(), name='signup'),
    path('v1/auth/token/', CreateTokenView.as_view(), name='token'),
    path("v1/", include(v1_router.urls)),
]

