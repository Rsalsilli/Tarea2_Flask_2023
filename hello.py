from random import choice, shuffle
from flask import Flask, render_template
app = Flask(__name__)


Comp={"Nintendo", "Sony", "Microsoft", "Varios"}
def otros(compañia):
    k = list(Comp-{compañia})
    shuffle(k)
    k = map(str.upper, k)
    return k

compañias = {
    "nintendo": {
        "nombre": 'Nintendo',
        "nick":"Nintendo",
        "url": "https://datawrapper.dwcdn.net/uTNfY/1/",
        "urlimg": "https://cdn.icon-icons.com/icons2/2429/PNG/512/nintendo_logo_icon_147258.png",
        "descripcion":"Nintendo ha producido y distribuido varias plataformas de videojuegos, entre las cuales se incluyen videoconsolas de sobremesa, portátiles, dedicadas e híbridas —es decir, sistemas con características de sobremesa y portátiles",
    },
    "sony":{
        "nombre": 'PlayStation',
        "nick":"Playstation",
        "url":"https://datawrapper.dwcdn.net/93fPT/1/",
        "urlimg": "https://cdn.icon-icons.com/icons2/2429/PNG/512/playstation_logo_icon_147249.png",
        "descripcion":"Playstation es el nombre de una serie de consolas de videojuegos creadas y desarrolladas por Sony Interactive Entertainment. Han estado presentes en la quinta, sexta, séptima, octava y novena generación de videoconsolas; la compañía promotora está actualmente en el mercado con su PlayStation 5",
    },
    "microsoft":{
        "nombre": 'Microsoft',
        "nick": "Microsoft",
        "url": "https://datawrapper.dwcdn.net/3suwD/1/",
        "urlimg": "https://i.pinimg.com/originals/71/fe/82/71fe82ae95593cb9977cc4cd0305089d.png",
        "descripcion":"Xbox es una marca de videojuegos creada por y propiedad de Microsoft que incluye una serie de videoconsolas desarrolladas por la misma compañía, de sexta a novena generación, así como aplicaciones (juegos), servicios de streaming y el servicio en línea Xbox Live. La marca fue introducida por primera vez el 8 de noviembre de 2001 en los Estados Unidos, con el lanzamiento de la consola Xbox",
    },
    "varios":{
        "nombre": 'Atari, Sega, Nec',
        "nick": "Varios",
        "url": "https://datawrapper.dwcdn.net/zgHTt/1/",
        "urlimg": "https://logowik.com/content/uploads/images/atari7759.jpg",
        "descripcion":"Atari y Sega tambien estan dentro de top, ya que, en los años 90 era la competecia directa de Nintendo",
    }
}


@app.route("/")
def index():
    return render_template("index.html", compañias=map(str.upper,Comp))

@app.route("/<string:slug>/")
def show_candidate(slug):
    if slug== "about":
        return render_template("post_view.html", compañias=map(str.upper,Comp))
    else:
        compañias[slug.lower()]["otros"] = otros(slug.lower())
        return render_template("pagina_ventas.html", compañia=compañias[slug.lower()])