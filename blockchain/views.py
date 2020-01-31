from mocherry.library.views import APIViewset
from mocherry.library.databases import DatabaseConnection
from mocherry.library.http import status
from mocherry.settings import CONFIG
from .apps import Blockchain, Block

blockchain = Blockchain(difficulty=4)

class BlockchainViewset(APIViewset):
    def POST(self, request, *args, **kwargs):
        payload = request.json
        queued_transactions = blockchain.add_new_transaction(payload)

        return self.send_response({
            "queue": queued_transactions
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


class BlockchainMineViewset(APIViewset):
    def PUT(self, request, *args, **kwargs):
        chain_index = blockchain.mine()

        return self.send_response({
            "index": chain_index
        })
    
    

