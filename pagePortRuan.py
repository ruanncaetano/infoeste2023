import cherrypy

class PaginaPortRuan():

    pagina = open("portRuan/main2.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.pagina

        return html