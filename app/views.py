import cherrypy

from mocherry.library.views import APIViewset

class IndexViewset(APIViewset):
    def GET(self):
        return self.send_response({
            'success': 'OK'
        })

