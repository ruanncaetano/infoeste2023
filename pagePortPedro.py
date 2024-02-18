import cherrypy

class PaginaPortPedro():

    pagina = open("portPedro/index.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.pagina

        return html