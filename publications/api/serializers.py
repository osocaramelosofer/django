from rest_framework import serializers

from ..models import Article, Publication

class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['title']

class ArticleSerializer(serializers.ModelSerializer):

    publications = PublicationSerializer(many=True)

    class Meta:
        model = Article
        fields = ['headline', 'publications']