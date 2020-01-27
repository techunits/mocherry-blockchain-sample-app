from mocherry.library.views import APIViewset
from mocherry.library.databases import DatabaseConnection
from mocherry.library.http import status
from mocherry.settings import CONFIG
from .apps import Blockchain

blockchain = Blockchain()

class BlockchainViewset(APIViewset):
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

