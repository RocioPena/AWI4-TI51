import web

urls = ('/', 'Calculadora', "/")
app = web.application(urls, globals())
render = web.template.render('templates')


class Calculadora:

    def GET(self):
        return render.calculadora()

    def POST(self):
        form = dict(web.input())
        # return form
        # opera = dict(web.submit())

        if form["opera"] == "suma":
            return ("la suma de " + form["num1"] + "+" + form["num2"] + "=" +
                    str(int(form["num1"]) + int(form["num2"])))
        elif form["opera"] == "resta":
            return ("la resta de " + form["num1"] + "-" + form["num2"] + "=" +
                    str(int(form["num1"]) - int(form["num2"])))
        elif form["opera"] == "multiplicacion":
            return ("la multiplicacion de " + form["num1"] + "*" +
                    form["num2"] + "=" +
                    str(int(form["num1"]) * int(form["num2"])))
        else:
            return ("la division de " + form["num1"] + "/" + form["num2"] +
                    "=" + str(int(form["num1"]) / int(form["num2"])))


# class Error:

if __name__ == "__main__":
    web.config.debug = True
    app.run()
