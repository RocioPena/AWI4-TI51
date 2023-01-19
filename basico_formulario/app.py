import web

urls = (
    '/', 'Formulario',
    "/"
    
)
app = web.application(urls, globals())
render = web.template.render('templates')

class Formulario:
    def GET(self):
        return render.formulario()
        
    def POST(self):
        form = web.input()
        return form["nombre"]

# class Error:

if __name__ == "__main__":
    web.config.debug = True
    app.run()