import cherrypy

class PaginaPortifolios():
    topo = open("html/topo.html", encoding="utf-8").read()
    conteudo = open("html/conteudo_portifolios.html", encoding="utf-8").read()
    rodape = open("html/rodape.html", encoding="utf-8").read()

    @cherrypy.expose()
    def index(self):
        html = self.topo
        html += self.conteudo
        html += self.rodape

        return html