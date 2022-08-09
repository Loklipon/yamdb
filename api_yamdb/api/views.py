from rest_framework import viewsets
from .serializer import ReviewSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from rest_framework.pagination import PageNumberPagination
from .permissions import CommentReviewPermission
from reviews.models import Review, Title


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    pagination_class = PageNumberPagination
    permission_classes = [CommentReviewPermission]

    def get_queryset(self):
        title = get_object_or_404(Title, pk=self.kwargs['title_id'])
        return title.reviews.all()

    def perform_create(self, serializer):
        title = get_object_or_404(Title, pk=self.kwargs['title_id'])

        serializer.save(author=self.request.user, title=title)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        title_id = self.kwargs['title_id']
        review_id = self.kwargs['review_id']
        review = get_object_or_404(
            Review.objects.filter(title_id=title_id),
            pk=review_id
        )
        return review.comments.all()

    def perform_create(self, serializer):
        title_id = self.kwargs['title_id']
        review_id = self.kwargs['review_id']
        review = get_object_or_404(
            Review.objects.filter(title_id=title_id),
            pk=review_id
        )
        serializer.save(author=self.request.user, review=review)
