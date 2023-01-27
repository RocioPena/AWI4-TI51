import web
from datetime import date
from datetime import datetime

urls = (
    '/(.*)', 'Visitas'
)

class Visitas:
    def GET(self, name):
        try: 
            cookie = web.cookies()
            visitas="0"
            ahora=datetime.now()
            fecha = ahora.strftime("%Y-%m-%d")
            hora = ahora.strftime("%H:%M")
            print(cookie)
            if name:
                web.setcookie("nombre", name ,expires="", domain=None)
            else:
                name ="NA"
                web.setcookie("nombre", name ,expires="", domain=None)

            if cookie.get("visitas"):
                visitas = int(cookie.get("visitas"))
                visitas += 1
                web.setcookie("visitas", str(visitas), expires="", domain=None)
            else:
                web.setcookie("visitas", str(1), expires="", domain=None)
                visitas= "1"

            if fecha:
                web.setcookie("fecha", fecha ,expires="", domain=None)
            else:
                web.setcookie("fecha", fecha ,expires="", domain=None)

            if hora:
                web.setcookie("hora", hora ,expires="", domain=None)
            else:
                web.setcookie("hora", hora ,expires="", domain=None)
            
            return "Visitas "+ str(visitas) + " Nombre " + name + " Fecha " + str(fecha) + " Hora " + str(hora)
        except Exception as e:
               return "Error " + str(e.args)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()