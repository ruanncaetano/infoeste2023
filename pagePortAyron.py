import cherrypy

class PaginaPortAyron():

    pagina = open("portAyron/formulario.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.pagina

        return html