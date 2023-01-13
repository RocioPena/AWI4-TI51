import web

urls = (
    '/', 'Index', 
    '/bienvenida', 'Bienvenida'
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Index:
    def GET(self):
       
        return render.index()

class Bienvenida:
    def GET(self):
        n1=10
        n2=37
        suma=n1+n2
        return render.bienvenida(suma)

if __name__ == "__main__":
    app.run()