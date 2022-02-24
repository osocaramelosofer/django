from django.shortcuts import render
from django.http import JsonResponse

from .models import Publication, Article
from .api.serializers import ArticleSerializer


def list_articles(request):
    a1 = Article.objects.all()
    a1 = ArticleSerializer(a1, many=True).data
    

    # Si queremos usar .first() debemos de asegurarnos de que 
    # haya mas de una instancia en nuestra query filter()
    a2 = Article.objects.filter(publications__id=6)
    a2 = ArticleSerializer(a2, many=True).data
    
    # p1 = Publication(title="Mananero")
    # p1.save()
    # p2 = Publication(title="tarde")
    # p2.save()
    # p3 = Publication(title="noche")
    # p3.save()

    # a2 = Article(headline="Rusia invade ucrania")
    # a2.save()
    # print('Article 2 = ', a2)
    # a2.publications.add(p1, p2, p3)
    # a2 = ArticleSerializer(a2, many=True).data

    context = {
        'Article 2': a2,
    }
    return JsonResponse(context)