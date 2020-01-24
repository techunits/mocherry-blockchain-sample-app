import cherrypy

from app.views import IndexViewset
from cms.views import ArticleViewset, ArticleDetailsViewset

def url_mapper():
    mapper = cherrypy.dispatch.RoutesDispatcher()
    mapper.connect('index', '/', controller=IndexViewset(), action='index')
    
    return mapper
