import cherrypy

class PaginaPortGustavo():

    pagina = open("portGustavo/index.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.pagina

        return html