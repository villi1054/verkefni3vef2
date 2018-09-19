from bottle import *

@route("/")
def index():
    return """<h2> Verkefni 3 <h2>
     <a href=/a> Liður A </a>
     <a href=/b> Liður B </a>
    """


@route("/a")
def index():
    return template("tempa.tpl")

frettir = [["Irma veldur usla á Flórída", "Það er bara ... vesen á Irmu í Flórída.  Milljónir manna hafa þurft að yfirgefa heimili sin vegna yfirvofandi eyðileggingar Irmu...", "irma.jpg", "dsg@frettir.is"],
           ["Veiðin er dræm þetta haustið", "Veiðin hefur heldur verið döpur þetta haustið þrátt fyrir ágætis rigninar upp á síðkastið...", "veidi.png", "est@frettir.is"],
           ["Ólafía stendur sig vel", "Ólafía er komin í 65 sæti peningalistans og hefur því tryggt sér keppnisrétt á LPG mótaröðinni á komandi keppnistimabili...", "golf.jpeg", "htg@frettir.is"],
           ["Ísland dottið úr leik", "Íslenska karlalandsliðið í körfubolta er dottið úr leik a Eurobasket þrátt fyrir ágætis spretti inn a milli.  Ísland spilaði lokaleik sinn á mótinu fyrir troðfullri höll gegn heimamönnum Finnum..", "karfa.jpeg", "dsg@frettir.is"]]


@route("/b")
def index():
    return template("base.tpl", frettir=frettir)

@route("/frett/<id: int>")
def index(id):
    return template("frett.tpl", frett=frettir[id], nr=id)

@route("/sida/<kt>")
def page(kt):
    return template("temp_kt.tpl", kt=kt)

@route('/static/<skra>')
def static_skrar(skra):
    return static_file(skra, root='./static')

@error(404)
def villa(error):
    return """<h2> Þessi síða finnst ekki </h2>
    <a href=/> Smelltu hér til að fara á forsíðu </a>"""


run(host='localhost', port=8080, reloader=True, debug=True)
