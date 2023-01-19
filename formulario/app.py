import web

urls = ('/', 'Calculadora', "/")
app = web.application(urls, globals())
render = web.template.render('templates')


class Calculadora:

    def GET(self):
        return render.calculadora()

    def POST(self):
        # form = web.input()
        form = dict(web.input())
        print(form)
        # return form[suma]


# class Error:

if __name__ == "__main__":
    web.config.debug = True
    app.run()
