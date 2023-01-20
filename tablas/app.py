import web

urls = (
    '/',
    'Tablas',
)
app = web.application(urls, globals())
render = web.template.render('templates')


class Tablas:

    def GET(self):
        datos = [["1", "Dejah"], ["2", "Jhon"]]
        return render.tabla(datos)


if __name__ == "__main__":
    web.config.debug = True
    app.run()
