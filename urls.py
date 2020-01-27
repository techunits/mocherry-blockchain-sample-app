import cherrypy

from app.views import IndexViewset
from blockchain.views import BlockchainViewset

def url_mapper():
    mapper = cherrypy.dispatch.RoutesDispatcher()
    mapper.connect('index', '/', controller=IndexViewset(), action='index')
    
    mapper.connect('blockchain_show_chain', '/chain/', controller=BlockchainViewset(), action='index')
    mapper.connect('blockchain_mine_block', '/mine/', controller=BlockchainViewset(), action='index')

    return mapper
