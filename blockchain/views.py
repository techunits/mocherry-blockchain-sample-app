from mocherry.library.views import APIViewset
from mocherry.library.databases import DatabaseConnection
from mocherry.library.http import status
from mocherry.settings import CONFIG
from datetime import datetime
from .models import Article

class ArticleViewset(APIViewset):
    def POST(self, request, *args, **kwargs):
        payload = request.json

        mongo_uri = CONFIG['database']['default']['uri']
        with DatabaseConnection(mongo_uri):
            article_info = Article()
            article_info.title = payload['title']
            article_info.description = payload['description']
            article_info.tags = payload['tags']
            article_info.modified_on = datetime.now()
            article_info.save()
            
        return self.send_response({
            'id': str(article_info.pk)
        })
    
    def GET(self):
        article_list = []

        mongo_uri = CONFIG['database']['default']['uri']
        with DatabaseConnection(mongo_uri):
            available_articles = Article.objects()
            for article_info in available_articles:
                article_list.append({
                    'id': str(article_info.pk),
                    'title': article_info.title,
                    'description': article_info.description,
                    'tags': article_info.tags,
                    'created_on': datetime.timestamp(article_info.created_on),
                    'modified_on': datetime.timestamp(article_info.modified_on)
                })

        return self.send_response({
            'articles': article_list
        })


class ArticleDetailsViewset(APIViewset):
    def GET(self, article_id):
        article_info = {}

        mongo_uri = CONFIG['database']['default']['uri']
        with DatabaseConnection(mongo_uri):
            available_article = Article.objects(pk=article_id).first()
            if available_article is None:
                return self.send_response({
                    'error': {
                        'message': 'Invalid article id'
                    }
                }, status_code=status.HTTP_404_NOT_FOUND)
            else:
                article_info = {
                    'id': str(available_article.pk),
                    'title': available_article.title,
                    'description': available_article.description,
                    'tags': available_article.tags,
                    'created_on': datetime.timestamp(available_article.created_on),
                    'modified_on': datetime.timestamp(available_article.created_on)
                }
        
        return self.send_response(article_info)

    def PUT(self, request, article_id):
        payload = request.json
        mongo_uri = CONFIG['database']['default']['uri']
        with DatabaseConnection(mongo_uri):
            available_article = Article.objects(pk=article_id).first()
            if available_article is None:
                return self.send_response({
                    'error': {
                        'message': 'Invalid article id'
                    }
                }, status_code=status.HTTP_404_NOT_FOUND)
            else:
                available_article.title = payload['title']
                available_article.description = payload['description']
                available_article.tags = payload['tags']
                available_article.modified_on = datetime.now()
                available_article.save()

        return self.send_response({
            'id': article_id
        })

    def DELETE(self, article_id):
        mongo_uri = CONFIG['database']['default']['uri']
        with DatabaseConnection(mongo_uri):
            available_article = Article.objects(pk=article_id).first()
            if available_article is None:
                return self.send_response({
                    'error': {
                        'message': 'Invalid article id'
                    }
                }, status_code=status.HTTP_404_NOT_FOUND)
            else:
                available_article.delete()

        return self.send_response({})

