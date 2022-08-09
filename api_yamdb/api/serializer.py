from rest_framework import serializers

from reviews.models import Review, Comment


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Review
        fields = '__all__'

    def validate(self, data):
        review = Review.objects.filter(
            author=self.context['request'].user,
            title=self.context['view'].kwargs.get('title_id')).exists()
        if review and self.context['request'].method == 'POST':
            raise serializers.ValidationError(
                'Вы уже оставляли отзыв на это произведение')
        return data


class CommentSerializer(serializers.ModelSerializer):
    review = serializers.SlugRelatedField(
        slug_field='text',
        read_only=True
    )
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        model = Comment
        fields = '__all__'
