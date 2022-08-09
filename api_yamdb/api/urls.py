from api.views import CommentViewSet, ReviewsViewSet
from rest_framework.routers import DefaultRouter

router_v1 = DefaultRouter()

router_v1.register(r'titles/(?P<title_id>\d+)/reviews', ReviewsViewSet,
                   basename='reviews')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')
