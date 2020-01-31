import cherrypy

from app.views import IndexViewset
from blockchain.views import BlockchainViewset, BlockchainMineViewset

def url_mapper():
    mapper = cherrypy.dispatch.RoutesDispatcher()
    mapper.connect('index', '/', controller=IndexViewset(), action='index')
    
    mapper.connect('blockchain_show_chain', '/transactions/', controller=BlockchainViewset(), action='index')
    mapper.connect('blockchain_mine_block', '/transactions/mine/', controller=BlockchainMineViewset(), action='index')

    return mapper
