# -*- coding: utf-8 -*-
"""Genera tutte le pagine del sito J@M (HTML statico) a partire dai contenuti qui sotto.
Uso:  python build.py      -> scrive index.html e le cartelle delle pagine interne.
Per pubblicare basta commit + push su main (GitHub Pages fa il resto).
"""
import os, html

BASE = "/jam-sito"          # con un dominio proprio (es. jam-srl.it) mettere ""
IMG = BASE + "/assets/img"
MUSEO = BASE + "/assets/museo"
ROOT = os.path.dirname(os.path.abspath(__file__))

# ---------------------------------------------------------------- icone svg
ICONS = """
<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="i-chev" viewBox="0 0 24 24"><path d="M9 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-down" viewBox="0 0 24 24"><path d="M6 9l6 6 6-6" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-arrow" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-arrow-l" viewBox="0 0 24 24"><path d="M19 12H5M11 6l-6 6 6 6" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></symbol>
<symbol id="i-phone" viewBox="0 0 24 24"><path d="M6.6 3h3l1.7 4.3-2.2 1.6a12 12 0 0 0 6 6l1.6-2.2L21 14.4v3a2 2 0 0 1-2.2 2A16.5 16.5 0 0 1 4.6 5.2 2 2 0 0 1 6.6 3z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/></symbol>
<symbol id="i-wa" viewBox="0 0 24 24"><path d="M4 20l1.3-3.8A8 8 0 1 1 8.2 19L4 20z" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"/><path d="M9.5 8.5c0 3 3 6 6 6l1-1.5-2-1-1 .8a5 5 0 0 1-2.3-2.3l.8-1-1-2-1.5 1z" fill="currentColor"/></symbol>
<symbol id="i-menu" viewBox="0 0 24 24"><path d="M4 7h16M4 12h16M4 17h16" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></symbol>
<symbol id="i-x" viewBox="0 0 24 24"><path d="M6 6l12 12M18 6L6 18" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></symbol>
<symbol id="i-in" viewBox="0 0 24 24"><path d="M4 9h4v11H4zM6 3a2 2 0 1 1 0 4 2 2 0 0 1 0-4zM10 9h4v2c.6-1.2 2-2.3 4-2.3 3.6 0 4 2.4 4 5.5V20h-4v-5c0-1.5-.3-2.8-1.9-2.8S14 13.6 14 15v5h-4z" fill="currentColor"/></symbol>
<symbol id="i-fb" viewBox="0 0 24 24"><path d="M14 8h3V4h-3c-2.8 0-4 1.8-4 4.4V11H7v4h3v6h4v-6h3l1-4h-4V8.6c0-.4.2-.6.6-.6z" fill="currentColor"/></symbol>
<symbol id="i-ig" viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="4" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="17.3" cy="6.7" r="1.2" fill="currentColor"/></symbol>
<symbol id="i-vimeo" viewBox="0 0 24 24"><path d="M22 7.4c-.1 2-1.5 4.7-4.2 8.1-2.8 3.6-5.2 5.4-7.1 5.4-1.2 0-2.2-1.1-3-3.3L6.1 11.7C5.5 9.5 4.9 8.4 4.2 8.4c-.2 0-.7.3-1.6.9L1.7 8.1c1-.9 2-1.8 3-2.7 1.3-1.2 2.3-1.8 3-1.8 1.6-.2 2.6.9 3 3.3.4 2.6.7 4.2.8 4.8.5 2.1 1 3.1 1.5 3.1.4 0 1.1-.7 1.9-2 .9-1.4 1.3-2.4 1.4-3.1.1-1.2-.3-1.8-1.4-1.8-.5 0-1 .1-1.5.3 1-3.3 2.9-4.9 5.8-4.8 2.1.1 3.1 1.5 2.8 4z" fill="currentColor"/></symbol>
<symbol id="i-tt" viewBox="0 0 24 24"><path d="M14 3h3.2c.3 2.3 1.6 3.7 3.8 4v3.2c-1.4 0-2.7-.4-3.8-1.2v6.3A5.7 5.7 0 1 1 11.5 9.6v3.3a2.5 2.5 0 1 0 2.5 2.5V3z" fill="currentColor"/></symbol>
<symbol id="i-xt" viewBox="0 0 24 24"><path d="M4 3h4.5l4 5.6L17.5 3H20l-6.3 7.4L21 21h-4.5l-4.4-6.1L6.5 21H4l6.9-8z" fill="currentColor"/></symbol>
<symbol id="i-pin" viewBox="0 0 24 24"><path d="M12 22s7-6.6 7-12a7 7 0 0 0-14 0c0 5.4 7 12 7 12z" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="10" r="2.5" fill="currentColor"/></symbol>
</defs></svg>
"""

# ---------------------------------------------------------------- navigazione
NAV = [
    ("Home", BASE + "/", []),
    ("L’isola", BASE + "/lisola/", [("Manifesto", BASE + "/lisola/manifesto/"), ("Storia di J@M", BASE + "/lisola/storia-di-jm/"), ("Gli abitanti", BASE + "/lisola/gli-abitanti/"), ("Amici & partner", BASE + "/lisola/amici-partner/"), ("Lavora con noi", BASE + "/lavora-con-noi/")]),
    ("Passioni", BASE + "/passioni/", [("Telecomunicazioni", BASE + "/passioni/telecomunicazioni/"), ("Energia", BASE + "/passioni/energia/"), ("Auto noleggio", BASE + "/passioni/noleggio-auto/"), ("Servizi web", BASE + "/passioni/servizi-web/"), ("Efficientamento energetico", BASE + "/passioni/efficientamento-energetico/")]),
    ("J@M Mood", BASE + "/jm-mood/", [("TV", BASE + "/jm-mood/tv/"), ("Museo", BASE + "/jm-mood/museo/"), ("Community", BASE + "/jm-mood/community/"), ("J@M Session", BASE + "/jm-mood/jm-session/")]),
    ("I villaggi", BASE + "/i-villaggi/", []),
]

def header(path):
    items = []
    for label, href, sub in NAV:
        cur = ' aria-current="page"' if path == href else ""
        if sub:
            dd = "".join('<a href="%s">%s</a>' % (h, l) for l, h in sub)
            items.append('<div><a href="%s"%s>%s</a><button type="button" aria-haspopup="true" aria-label="Apri %s"><svg><use href="#i-down"/></svg></button><div class="dd">%s</div></div>' % (href, cur, label, label, dd))
        else:
            items.append('<div><a href="%s"%s>%s</a></div>' % (href, cur, label))
    mob = []
    for label, href, sub in NAV:
        mob.append('<div class="grp"><a href="%s">%s</a>%s</div>' % (href, label, ('<div class="sub">' + "".join('<a href="%s">%s</a>' % (h, l) for l, h in sub) + '</div>') if sub else ""))
    return """
<header class="top" id="top"><div class="wrap">
  <a class="logo" href="%s/" aria-label="J@M Passion — home"><img src="%s/logo.webp" width="506" height="287" alt="J@M Passion"></a>
  <nav class="nav" aria-label="Principale">%s</nav>
  <div class="top-actions">
    <a class="icon-btn" href="tel:02898094" aria-label="Chiama 02 898094" title="02 898094"><svg><use href="#i-phone"/></svg></a>
    <a class="icon-btn" href="https://api.whatsapp.com/send?phone=+3902898094" rel="noopener" aria-label="Scrivici su WhatsApp" title="WhatsApp"><svg><use href="#i-wa"/></svg></a>
    <button class="icon-btn burger" id="burger" aria-label="Apri il menu" aria-expanded="false" aria-controls="menu"><svg><use href="#i-menu"/></svg></button>
  </div>
</div></header>
<nav class="menu" id="menu" aria-label="Menu"><button class="icon-btn close" id="menuClose" aria-label="Chiudi il menu"><svg><use href="#i-x"/></svg></button>%s<div class="grp"><a href="%s/#contatti">Contatti</a></div></nav>
""" % (BASE, IMG.replace("/img", ""), "".join(items), "".join(mob), BASE)

FOOTER = """
<footer class="site-footer"><div class="wrap">
  <div class="grid">
    <nav aria-label="Footer"><a href="%(b)s/lisola/">L’isola</a><a href="%(b)s/passioni/">Passioni</a><a href="%(b)s/jm-mood/">Mood</a><a href="%(b)s/i-villaggi/">I villaggi</a><a href="https://www.iubenda.com/privacy-policy/91688595" rel="noopener">Privacy policy</a><a href="https://www.iubenda.com/privacy-policy/91688595/cookie-policy" rel="noopener">Utilizzo dei cookie</a></nav>
    <div class="brand"><img src="%(a)s/logo.webp" width="506" height="287" alt="J@M Passion"><span class="claim">mettici passione</span></div>
    <div class="addr"><a href="https://www.google.com/maps/place/J@M+SRL/@45.4402045,9.1993427,15z" rel="noopener">Via Rutilia 2,4<br>20141 - Milano (MI)</a><a href="mailto:jam@jam-srl.it">jam@jam-srl.it</a><a href="tel:02898094">02 898094</a><a href="tel:0289809480">02 89809480</a></div>
  </div>
  <p class="rights">Tutti i diritti riservati © J@M srl · P.IVA 13329170156 · Designed by J@M</p>
</div></footer>
<button class="totop" id="totop" aria-label="Torna su"><img src="%(a)s/mascotte-mini.webp" width="100" height="87" alt=""></button>
<img class="guide" id="guide" src="%(i)s/girl-standing.webp" width="246" height="655" alt="">
""" % {"b": BASE, "a": BASE + "/assets", "i": IMG}

# ---------------------------------------------------------------- componenti
def art(name, lit=True, zoom=True):
    u = "%s/%s.webp" % (IMG, name)
    inner = '<div class="art dim" style="background-image:url(%s)"></div>' % u + ('<div class="art lit" style="background-image:url(%s)"></div>' % u if lit else "")
    return '<div class="art-wrap">%s</div>' % ('<div class="art-zoom">%s</div>' % inner if zoom else inner)

def hero(artname, title, lede="", eyebrow="", ctas="", ill=None, ill_alt="", credit="", size="", extra=""):
    cls = "art-hero" + (" " + size if size else "") + (" has-ill" if ill else "")
    return """
<section class="%s">%s<div class="veil"></div>
  <div class="wrap">%s<h1>%s</h1>%s%s</div>
  %s%s%s
</section>""" % (cls, art(artname), ('<p class="eyebrow">%s</p>' % eyebrow) if eyebrow else "", title,
                 ('<p class="lede">%s</p>' % lede) if lede else "", ('<div class="ctas">%s</div>' % ctas) if ctas else "",
                 ('<img class="hero-ill" src="%s/%s.webp" alt="%s">' % (IMG, ill, html.escape(ill_alt))) if ill else "",
                 ('<span class="credit">%s</span>' % credit) if credit else "", extra)

def split(title, text_html, ill, alt="", rev=False, eyebrow="", ctas="", compact=False, float_=40, ident=""):
    return """
<section class="split%s%s"%s><div class="wrap">
  <div class="txt" data-reveal>%s<h2>%s</h2>%s%s</div>
  <img class="ill" src="%s/%s.webp" alt="%s" loading="lazy" data-float="%s" data-reveal>
</div></section>""" % (" rev" if rev else "", " compact" if compact else "", (' id="%s"' % ident) if ident else "",
                        ('<p class="eyebrow">%s</p>' % eyebrow) if eyebrow else "", title, text_html,
                        ('<div class="ctas">%s</div>' % ctas) if ctas else "", IMG, ill, html.escape(alt), float_)

def feats(items, eyebrow="", title="", lede="", ident=""):
    cards = "".join('<div class="feat">%s<h3>%s</h3>%s</div>' % (('<span class="k">%s</span>' % k) if k else "", t, ('<p>%s</p>' % p) if p else "") for k, t, p in items)
    head = ""
    if title or eyebrow or lede:
        head = '<div class="narrow" style="margin-bottom:40px" data-reveal>%s%s%s</div>' % (('<p class="eyebrow">%s</p>' % eyebrow) if eyebrow else "", ('<h2 class="mt">%s</h2>' % title) if title else "", ('<p class="lede mt">%s</p>' % lede) if lede else "")
    return '<section class="pad-s"%s><div class="wrap">%s<div class="feats" data-stagger>%s</div></div></section>' % ((' id="%s"' % ident) if ident else "", head, cards)

def statement(text, sub="", light="", eyebrow=""):
    return '<section class="statement"><div class="wrap">%s<p class="big" data-light="%s">%s</p>%s</div></section>' % (('<p class="eyebrow" style="margin-bottom:22px">%s</p>' % eyebrow) if eyebrow else "", light, text, ('<p class="sub">%s</p>' % sub) if sub else "")

def art_band(artname, quote, credit="", ctas="", eyebrow="", lit=True):
    return '<section class="art-band">%s<div class="veil"></div><div class="wrap">%s<blockquote>%s</blockquote>%s</div>%s</section>' % (
        art(artname, lit), ('<p class="eyebrow">%s</p>' % eyebrow) if eyebrow else "", quote, ('<div class="ctas">%s</div>' % ctas) if ctas else "", ('<span class="credit">%s</span>' % credit) if credit else "")

def vimeo(vid, wide=False, title="Video J@M"):
    return '<div class="video%s"><iframe src="https://player.vimeo.com/video/%s?dnt=1&title=0&byline=0&portrait=0&color=ff6a00" title="%s" loading="lazy" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div>' % (" wide" if wide else "", vid, title)

def videos(ids, eyebrow="", title="", lede="", first_wide=False):
    head = '<div class="narrow" style="margin-bottom:36px" data-reveal>%s%s%s</div>' % (('<p class="eyebrow">%s</p>' % eyebrow) if eyebrow else "", ('<h2 class="mt">%s</h2>' % title) if title else "", ('<p class="lede mt">%s</p>' % lede) if lede else "") if (title or eyebrow) else ""
    vids = "".join(vimeo(v, wide=(first_wide and i == 0)) for i, v in enumerate(ids))
    return '<section class="pad-s"><div class="wrap">%s<div class="videos" data-stagger>%s</div></div></section>' % (head, vids)

def tv_set(vid):
    return '<div class="tv-set" data-reveal><img src="%s/tv.webp" width="1080" height="1080" alt="Il televisore di J@M"><div class="screen"><iframe src="https://player.vimeo.com/video/%s?dnt=1&title=0&byline=0&portrait=0&color=ff6a00" title="Video J@M" loading="lazy" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen></iframe></div></div>' % (BASE + "/assets", vid)

def form_section(title="Vuoi chiederci qualcosa?", lede="Compila il form e ti ricontatteremo presto per fornirti tutte le informazioni di cui hai bisogno.", subject="Richiesta dal sito J@M", msg_label="Il tuo messaggio (facoltativo)", extra_fields="", phone=True, button="invia"):
    return """
<section class="contact" id="contatti"><div class="wrap">
  <div data-reveal><p class="eyebrow">Contatti</p><h2 class="mt">%s</h2><p class="lede">%s</p>%s<img class="contact-mascot" src="%s/mascotte.webp" width="444" height="363" alt=""></div>
  <form class="panel" novalidate data-reveal data-subject="%s">
    <div class="field"><label for="c-nome">Nome Cognome / Ragione sociale</label><input id="c-nome" name="nome" type="text" autocomplete="name" required></div>
    <div class="row2"><div class="field"><label for="c-email">La tua email</label><input id="c-email" name="email" type="email" autocomplete="email" required></div><div class="field"><label for="c-tel">Il tuo telefono</label><input id="c-tel" name="telefono" type="tel" autocomplete="tel" required></div></div>
    %s<div class="field"><label for="c-msg">%s</label><textarea id="c-msg" name="messaggio"></textarea></div>
    <button class="btn btn-red" type="submit">%s</button><p class="sent" role="status"></p>
    <p class="legal">Cliccando su invia dichiari di aver preso visione e di accettare la nostra <a href="https://www.iubenda.com/privacy-policy/91688595" rel="noopener">privacy policy</a>.</p>
  </form>
</div></section>""" % (title, lede, ('<a class="phone" href="tel:02898094"><svg><use href="#i-phone"/></svg>02 898094</a>' if phone else ""), BASE + "/assets", html.escape(subject), extra_fields, msg_label, button)

SOCIALS = """<div class="socials" data-stagger>
<a href="https://www.linkedin.com/company/j-m-srl/" rel="noopener"><svg><use href="#i-in"/></svg>LinkedIn</a>
<a href="https://www.facebook.com/jam.srl" rel="noopener"><svg><use href="#i-fb"/></svg>Facebook</a>
<a href="https://www.instagram.com/jamsrl/" rel="noopener"><svg><use href="#i-ig"/></svg>Instagram</a>
<a href="https://vimeo.com/jamsrl" rel="noopener"><svg><use href="#i-vimeo"/></svg>Vimeo</a>
<a href="https://www.tiktok.com/@jampassion" rel="noopener"><svg><use href="#i-tt"/></svg>TikTok</a>
<a href="https://twitter.com/jam_passion?lang=it" rel="noopener"><svg><use href="#i-xt"/></svg>X / Twitter</a></div>"""

IG_POSTS = [("CsjAX24RmLF", "IoT e Machine To Machine per la tua azienda"), ("CsQcI6FoL43", "i vantaggi del fotovoltaico"), ("Cr_LWgYx3Cc", "consulenza energetica gratuita"), ("CrtB_uCRgoX", "buon 1 maggio"), ("Crixo3sRKEU", "noleggio auto full-electric"), ("CrbTRQpNmAp", "test dei pannelli fotovoltaici"), ("reel/CrRLMLSOD-r", "sistemi di accumulo"), ("CrJKpxIR84C", "fotovoltaico con batteria d'accumulo")]
def ig_band():
    posts = "".join('<a href="https://www.instagram.com/%s/" rel="noopener"><img src="%s/assets/ig/post%d.webp" width="480" height="480" loading="lazy" alt="Post Instagram J@M: %s"></a>' % (("p/" + p) if not p.startswith("reel") else p, BASE, i + 1, a) for i, (p, a) in enumerate(IG_POSTS))
    return '<section class="ig-band"><div class="wrap"><p class="ig-title" data-reveal><small>Instagram</small>fatti prendere da j@m</p><div class="ig" data-stagger>%s</div></div></section>' % posts

MUSEO_WORKS = [
    ("01-liechtenstein", "Comics", "Roy Lichtenstein", "1963", "Milano"), ("02-haring", "Senza titolo", "Keith Haring", "", "Milano"),
    ("03-rousseau", "L’incantatrice di serpenti", "Henri Rousseau", "1907", "Milano"), ("04-ligabue-leopardo-assalito-da-un-serpente", "Leopardo assalito da un serpente", "Antonio Ligabue", "1957", "Padova"),
    ("05-south-park", "South Park", "Trey Parker e Matt Stone", "1992", "Milano"), ("06-hopper", "I nottambuli", "Edward Hopper", "1942", "Milano"),
    ("07-miro", "Il carnevale di Arlecchino", "Joan Miró", "1925", "Milano"), ("08-dylan-dog-il-lungo-addio", "Il lungo addio", "Dylan Dog", "1992", "Milano"),
    ("09-hokusai-la-grande-onda", "La grande onda", "Hokusai", "1831", "Milano"), ("10-picasso", "Les demoiselles d’Avignon", "Pablo Picasso", "1907", "Milano"),
    ("11-van-gogh-notte-stellata150x1185cm", "Notte stellata", "Vincent van Gogh", "1889", "Milano"), ("12-klimt-def-15-01-2016", "Il bacio", "Gustav Klimt", "1907", "Milano"),
    ("13-piero-della-francesca", "La città ideale", "Piero della Francesca", "1420", "Roma"), ("14-lempicka", "Primavera", "Tamara de Lempicka", "1928", "Bologna"),
    ("15-manet", "Colazione sull’erba", "Édouard Manet", "1863", "Bologna"), ("16-van-eyck", "Ritratto dei coniugi Arnolfini", "Jan van Eyck", "1434", "Milano"),
    ("17-vettriano", "The Singing Butler", "Jack Vettriano", "1992", "Milano"), ("18-amano-minitokyo", "Minitokyo", "Yoshitaka Amano", "2007", "Lecce"),
    ("19-dali-la-persistenza-della-memoria", "La persistenza della memoria", "Salvador Dalí", "1931", "Milano"), ("20-gauguin-la-siesta", "La siesta", "Paul Gauguin", "1894", "Torino"),
    ("21-jam-magritte-golconda-vers-b", "Golconda", "René Magritte", "1953", "Milano"), ("22-jam-marilyn", "Marilyn", "Andy Warhol", "1962", "Cantù"),
    ("23-liechtenstein", "Comics", "Roy Lichtenstein", "1963", "Milano"), ("24-yerka-by-the-waters-24x285cm", "By the waters", "Jacek Yerka", "", "Milano"),
    ("25-escher-convesso-e-concavo", "Convesso e concavo", "M.C. Escher", "1955", "Verona"), ("26-caravaggio-il-baro", "I bari", "Caravaggio", "1594", "Roma"),
    ("27-botticelli-primavera", "La primavera", "Sandro Botticelli", "1477", "Cantù"), ("28-botero", "Stampa su tela", "Fernando Botero", "", "Milano"),
    ("29-escher-giorno-e-notte-40x235cm-mod", "Giorno e notte", "M.C. Escher", "1938", "Verona"), ("30-dylan-dog-by-lorenzo-ceccotti", "Dylan Dog", "Lorenzo Ceccotti", "2014", "Milano"),
    ("31-jam-magritte-il-castello-dei-pirenei", "Il castello dei Pirenei", "René Magritte", "1958", "Milano"), ("32-velazquez-las-meninas", "Las meninas", "Diego Velázquez", "1656", "Milano"),
    ("33-yerka-illustrazione", "Owl City", "Jacek Yerka", "", "Milano"), ("34-escher-relativita", "Relatività", "M.C. Escher", "1953", "Milano"),
]
def figure(w):
    f, t, a, y, c = w
    return '<figure><img src="%s/%s.webp" width="640" height="640" loading="lazy" alt="%s, %s, reinterpretato da J@M"><figcaption><b>%s</b>%s%s</figcaption></figure>' % (MUSEO, f, html.escape(t), html.escape(a), html.escape(t), html.escape(a) + (", " + y if y else ""), (" · " + c) if c else "")
def museo_wall(works, ident="museo"):
    return '<section class="wall-pin" id="%s"><div class="wall-stage"><div class="wall-track">%s</div></div></section>' % (ident, "".join(figure(w) for w in works))
def museo_grid(works):
    return '<section class="pad-s"><div class="wrap"><div class="wall-grid" data-stagger>%s</div></div></section>' % "".join(figure(w) for w in works)
LIGHTBOX = '<div class="lightbox" id="lightbox" role="dialog" aria-label="Opera ingrandita"><figure style="margin:0"><img src="" alt=""><figcaption></figcaption></figure></div>'

def cta_band(text, btn, href, sub=""):
    return '<section class="statement"><div class="wrap" data-reveal><p class="big" style="opacity:1">%s</p>%s<div class="ctas mt3" style="justify-content:center"><a class="btn btn-primary" href="%s">%s</a></div></div></section>' % (text, ('<p class="sub">%s</p>' % sub) if sub else "", href, btn)

# ---------------------------------------------------------------- layout
def layout(path, title, desc, body, extra_css="", extra_js="", og_image=None):
    depth = path.strip("/").count("/") + (1 if path.strip("/") else 0)
    return """<!doctype html>
<html lang="it">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>%(title)s</title>
<meta name="description" content="%(desc)s">
<meta name="theme-color" content="#050403">
<meta property="og:type" content="website"><meta property="og:title" content="%(title)s"><meta property="og:description" content="%(desc)s"><meta property="og:locale" content="it_IT">
<meta property="og:image" content="https://sagardelledonne.github.io%(og)s">
<link rel="icon" href="%(a)s/mascotte-mini.webp" type="image/webp">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;500;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="%(a)s/site.css">
%(css)s
</head>
<body>
%(icons)s
%(header)s
<main>
%(body)s
</main>
%(footer)s
<script src="%(a)s/site.js" defer></script>
%(js)s
</body>
</html>
""" % {"title": html.escape(title), "desc": html.escape(desc), "a": BASE + "/assets", "og": og_image or (IMG + "/ill-isola-castello.webp"),
       "css": ("<style>%s</style>" % extra_css) if extra_css else "", "icons": ICONS, "header": header(path), "body": body, "footer": FOOTER, "js": extra_js}

PAGES = {}
def page(path, title, desc, body, **kw):
    PAGES[path] = (title, desc, body, kw)

A = BASE + "/assets"
chev = '<svg><use href="#i-chev"/></svg>'

# ================================================================ HOME
HOME_CSS = """
.hero-home { align-items: center; text-align: center; min-height: 100svh; padding-top: calc(120px + env(safe-area-inset-top, 0px)); padding-bottom: 110px; }
.hero-home .wrap { justify-items: center; gap: 26px; pointer-events: none; }
.hero-home .wrap > * { pointer-events: auto; }
.hero-home canvas { position: absolute; inset: 0; width: 100%; height: 100%; pointer-events: none; }
.hero-home .art.dim { filter: brightness(.55) saturate(.9); }
.hero-home .veil { background: linear-gradient(to top, var(--bg) 0%, rgba(5,4,3,.55) 30%, rgba(5,4,3,.25) 60%, rgba(5,4,3,.55) 100%); }
.hero-home h1 { width: 100%; max-width: none; }
.word-slot { height: clamp(150px, 26vw, 330px); width: 100%; position: relative; display: grid; place-items: center; }
.word-slot .fallback { font-weight: 800; font-size: clamp(2.4rem, 8vw, 6.6rem); letter-spacing: -0.045em; line-height: .98; text-transform: uppercase; }
body.js .word-slot .fallback { visibility: hidden; }
.hero-home .lede { max-width: 46ch; }
.hero-hint { position: absolute; left: 50%; bottom: 26px; transform: translateX(-50%); font-size: .74rem; letter-spacing: .14em; text-transform: uppercase; color: var(--muted); display: grid; justify-items: center; gap: 10px; }
.hero-hint i { display: block; width: 1px; height: 40px; background: var(--line); position: relative; overflow: hidden; }
.hero-hint i::after { content: ""; position: absolute; inset: 0; background: var(--ember); transform: translateY(-100%); animation: drop 1.8s ease-in-out infinite; }
.hero-tap { position: absolute; left: var(--gutter); bottom: 26px; font-size: .74rem; letter-spacing: .14em; text-transform: uppercase; color: var(--muted); }
.hero-mascot { position: absolute; left: clamp(8px, 4vw, 60px); top: 36%; width: clamp(90px, 12vw, 170px); pointer-events: none; filter: drop-shadow(0 20px 40px rgba(255,45,74,.35)); animation: float 5s ease-in-out infinite; }
@keyframes drop { 0% { transform: translateY(-100%);} 60% { transform: translateY(100%);} 100% { transform: translateY(100%);} }
/* Passioni: sipario sul Vettriano */
.passioni-head { display: grid; gap: 16px; max-width: 760px; position: relative; }
.passioni-head .occhiali { width: clamp(90px, 12vw, 150px); margin-bottom: -10px; filter: drop-shadow(0 16px 30px rgba(255,45,74,.35)); }
.curtain { position: relative; height: clamp(300px, 52vw, 640px); margin-block: 44px 52px; border-radius: 28px; overflow: hidden; clip-path: inset(0 calc((1 - var(--open, 0)) * 50%) round 28px); box-shadow: 0 50px 100px -40px rgba(0,0,0,.9); }
.curtain-art { position: absolute; inset: -8%; background: center 30%/cover no-repeat; animation: pan 36s ease-in-out infinite alternate; }
.curtain::after { content: ""; position: absolute; inset: 0; background: linear-gradient(to top, rgba(5,4,3,.7), transparent 45%); }
.curtain .cap { position: absolute; left: 24px; bottom: 18px; font-size: .74rem; letter-spacing: .12em; text-transform: uppercase; color: rgba(245,240,236,.8); z-index: 2; }
.curtain .q { position: absolute; right: 24px; bottom: 18px; font-size: clamp(1rem, 1.6vw, 1.3rem); font-weight: 600; letter-spacing: -0.01em; max-width: 30ch; text-align: right; z-index: 2; text-shadow: 0 2px 20px rgba(0,0,0,.8); }
@keyframes pan { from { transform: translateX(-2%) scale(1); } to { transform: translateX(2%) scale(1.06); } }
.track { display: grid; grid-auto-flow: column; grid-auto-columns: min(380px, 84vw); gap: 20px; overflow-x: auto; scroll-snap-type: x mandatory; padding-bottom: 8px; scrollbar-width: none; margin-inline: calc(-1 * var(--gutter)); padding-inline: var(--gutter); scroll-padding-inline: var(--gutter); }
.track::-webkit-scrollbar { display: none; }
.card { --acc: var(--red); scroll-snap-align: start; position: relative; background: var(--bg-3); border-radius: 28px; padding: 30px; min-height: 460px; display: grid; grid-template-rows: auto 1fr auto; gap: 20px; overflow: hidden; text-decoration: none; color: inherit; transition: transform .35s cubic-bezier(.2,.7,.2,1); isolation: isolate; }
.card::before { content: ""; position: absolute; inset: 0; background: radial-gradient(520px circle at var(--mx, 85%) var(--my, -10%), color-mix(in srgb, var(--acc) 42%, transparent), transparent 55%); opacity: .55; transition: opacity .35s ease; z-index: -1; }
.card:hover { transform: translateY(-6px); } .card:hover::before { opacity: 1; }
.card .k { font-size: .78rem; letter-spacing: .12em; text-transform: uppercase; color: var(--muted); font-weight: 600; display: flex; justify-content: space-between; }
.card .k b { color: var(--acc); }
.card .ic { height: 96px; display: grid; align-items: center; justify-items: start; }
.card .ic img { height: 84px; width: auto; filter: drop-shadow(0 10px 26px rgba(216,46,0,.55)); transition: transform .4s cubic-bezier(.2,.7,.2,1); }
.card:hover .ic img { transform: translateY(-4px) scale(1.06); }
.card h3 { font-size: clamp(1.5rem, 2.2vw, 1.9rem); letter-spacing: -0.03em; font-weight: 700; text-transform: uppercase; }
.card .body { align-self: end; display: grid; gap: 12px; }
.card p { color: var(--muted); font-size: 1.05rem; }
.track-nav { display: flex; gap: 10px; justify-content: flex-end; margin-top: 22px; }
.track-nav button { width: 44px; height: 44px; border-radius: 50%; border: 0; background: rgba(245,240,236,.1); color: var(--paper); display: grid; place-items: center; cursor: pointer; }
.track-nav button:hover { background: rgba(245,240,236,.22); }
.track-nav svg { width: 18px; height: 18px; }
/* Isola che emerge sopra l'Escher */
.pin { position: relative; height: 240vh; }
.pin .stage { position: sticky; top: 0; height: 100svh; overflow: hidden; display: grid; align-items: center; }
.isola .stage .art-wrap { inset: -6%; }
.isola .stage .art.dim { filter: brightness(.3) saturate(.7); }
.isola .stage .wrap { display: grid; grid-template-columns: 1fr 1fr; gap: clamp(28px, 6vw, 96px); align-items: center; width: 100%; position: relative; z-index: 2; }
.isola h2 { font-size: clamp(2.3rem, 5.6vw, 5rem); }
.isola .quote { margin-top: 18px; font-size: clamp(1.1rem, 1.7vw, 1.5rem); line-height: 1.4; color: var(--muted); max-width: 40ch; }
.isola .quote b { color: var(--paper); font-weight: 600; }
.isola-links { display: flex; flex-wrap: wrap; gap: 8px 22px; margin-top: 22px; }
.isola-links a { text-decoration: none; font-size: .84rem; letter-spacing: .1em; text-transform: uppercase; font-weight: 600; color: var(--paper); display: inline-flex; align-items: center; gap: 6px; }
.isola-links a svg { width: 16px; height: 16px; color: var(--ember); }
.isola-links a:hover { color: var(--ember); }
.isola-art { justify-self: center; width: min(100%, 560px); will-change: transform; filter: drop-shadow(0 40px 60px rgba(0,0,0,.7)); }
.sea { position: absolute; left: -10%; right: -10%; bottom: -2%; height: 40%; z-index: 3; pointer-events: none; background: linear-gradient(to bottom, rgba(5,4,3,0) 0%, rgba(5,4,3,.85) 30%, var(--bg) 100%); }
.sea::before { content: ""; position: absolute; left: 0; right: 0; top: 18%; height: 2px; background: linear-gradient(90deg, transparent, rgba(255,106,0,.55), transparent); filter: blur(1px); }
.isola .credit { position: absolute; right: var(--gutter); bottom: 14px; z-index: 4; font-size: .68rem; letter-spacing: .12em; text-transform: uppercase; color: rgba(245,240,236,.5); }
/* Mood */
.mood-band { position: relative; height: clamp(220px, 34vw, 440px); display: grid; place-items: center; overflow: hidden; }
.mood-band .art-wrap { inset: -6%; }
.mood-band .art.dim { filter: brightness(.5) saturate(1.1); }
.mood-band .pattern { position: absolute; inset: -20% -50%; background: linear-gradient(90deg, #D82E00, #FF6A00, #FF2D4A, #D82E00); -webkit-mask: url(__A__/pattern-mood.webp) center/900px auto repeat; mask: url(__A__/pattern-mood.webp) center/900px auto repeat; opacity: .35; animation: panx 40s linear infinite; }
.mood-band::after { content: ""; position: absolute; inset: 0; background: radial-gradient(ellipse at center, rgba(5,4,3,.1), rgba(5,4,3,.85) 75%); }
.mood-band h2 { position: relative; z-index: 2; font-size: clamp(4rem, 16vw, 15rem); font-weight: 800; letter-spacing: -0.06em; line-height: 1; text-transform: uppercase; }
.mood-band .credit { position: absolute; right: var(--gutter); bottom: 12px; z-index: 2; font-size: .68rem; letter-spacing: .12em; text-transform: uppercase; color: rgba(245,240,236,.55); }
@keyframes panx { to { transform: translateX(-450px); } }
.tvh .wrap { display: grid; grid-template-columns: 1fr 1.2fr; gap: clamp(24px, 5vw, 80px); align-items: center; }
.tvh h2 { font-size: clamp(3rem, 8vw, 7rem); text-transform: uppercase; }
.museo-head { display: grid; gap: 16px; max-width: 820px; }
.museo-head h2 { font-size: clamp(3rem, 9vw, 8rem); text-transform: uppercase; }
/* Villaggi: la pioggia di Magritte */
.villaggi .art.dim { filter: brightness(.35) saturate(.9); animation: rain 24s linear infinite; }
.villaggi .art.lit { animation: rain 24s linear infinite; }
@keyframes rain { from { background-position: center 0%; } to { background-position: center 100%; } }
.villaggi .veil { background: linear-gradient(to right, rgba(5,4,3,.9) 0%, rgba(5,4,3,.5) 55%, rgba(5,4,3,.15) 100%); }
.villaggi .wrap { display: grid; grid-template-columns: .9fr 1.1fr; gap: clamp(24px, 5vw, 80px); align-items: center; }
.villaggi-art { width: min(100%, 440px); justify-self: center; filter: drop-shadow(0 30px 60px rgba(0,0,0,.7)); }
@media (max-width: 1000px) {
  .isola .stage .wrap, .tvh .wrap, .villaggi .wrap { grid-template-columns: 1fr; }
  .isola .stage .wrap { align-content: center; gap: 20px; }
  .isola-art { width: min(64%, 380px); order: -1; } .sea { height: 24%; }
  .tv-set { order: 2; }
}
@media (max-width: 560px) {
  .hero-home { padding-top: calc(96px + env(safe-area-inset-top, 0px)); padding-bottom: 120px; }
  .hero-tap, .hero-mascot { display: none; }
  .pin { height: 200vh; } .isola h2 { font-size: clamp(2rem, 9vw, 3rem); } .isola .quote { font-size: 1rem; } .isola-art { width: min(58%, 300px); }
  .card { min-height: 420px; padding: 24px; }
  .curtain { height: 62vw; border-radius: 18px; clip-path: inset(0 calc((1 - var(--open, 0)) * 50%) round 18px); }
  .curtain .q { display: none; }
}
""".replace("__A__", A)

PASSIONI_CARDS = [
    ("telecomunicazioni", "#FF3D71", "01", "icona-telecomunicazioni", 420, 334, "Telecomunicazioni", "Piani Telefonia e Internet"),
    ("energia", "#FF6A00", "02", "icona-energia", 309, 585, "Energia", "Forniture luce e gas, nuovi allacci, subentri e volture"),
    ("noleggio-auto", "#D82E00", "03", "icona-auto", 420, 370, "Auto noleggio", "A medio e lungo termine"),
    ("servizi-web", "#FF8A5B", "04", "icona-web", 420, 420, "Servizi web", "Web Design, SEO, Digital Marketing, Social Media"),
    ("efficientamento-energetico", "#FFB300", "05", "icona-efficientamento", 420, 377, "Efficientamento energetico", "Superbonus ed Ecobonus per immobili indipendenti e condomini"),
]
def passioni_cards():
    return "".join("""<a class="card" href="%s/passioni/%s/" style="--acc:%s"><div class="k"><span>Passione</span><b>%s</b></div><div class="ic"><img src="%s/%s.webp" width="%d" height="%d" alt=""></div><div class="body"><h3>%s</h3><p>%s</p><span class="link">scopri %s</span></div></a>""" % (BASE, slug, acc, n, A, ic, w, h, t, p, chev) for slug, acc, n, ic, w, h, t, p in PASSIONI_CARDS)

HOME_BODY = """
<section class="art-hero tall hero-home" id="home">%(art)s<div class="veil"></div><canvas id="heroCanvas" aria-hidden="true"></canvas>
  <div class="wrap">
    <p class="eyebrow">Consulenza professionale per imprese e privati</p>
    <h1><span class="word-slot" id="wordSlot"><span class="fallback grad">Testa, cuore<br>e spirito<br>d'iniziativa</span><span class="sr-only">Testa, cuore e spirito d'iniziativa</span></span></h1>
    <p class="lede">In J@M si crea, si sperimenta, si scommette perché le strade inesplorate nascondono un mare di possibilità.</p>
    <div class="ctas" style="justify-content:center"><a class="btn btn-primary" href="%(b)s/lisola/manifesto/">manifesto</a><a class="link" href="#contatti">Vuoi chiederci qualcosa? %(chev)s</a></div>
  </div>
  <img class="hero-mascot" src="%(a)s/mascotte.webp" width="444" height="363" alt="">
  <p class="hero-hint"><i></i> Scorri</p><p class="hero-tap">Clicca per far esplodere</p>
  <span class="credit">M.C. Escher, Giorno e notte · Museo J@M</span>
</section>

<section class="pad" id="passioni"><div class="wrap">
  <div class="passioni-head" data-reveal><img class="occhiali floaty" src="%(a)s/mascotte-occhiali.webp" width="444" height="363" alt=""><h2>Le nostre passioni</h2><p class="lede">Una gamma completa di servizi per la tua casa e per il tuo business</p></div>
  <div class="curtain" id="curtain"><div class="curtain-art" style="background-image:url(%(i)s/art-vettriano.webp)"></div><span class="cap">Jack Vettriano, The Singing Butler · Museo J@M</span><p class="q">Il consulente commerciale J@M può proporre numerosi prodotti, suggerendo efficaci strategie di investimento.</p></div>
  <div class="track" id="track" data-stagger>%(cards)s</div>
  <div class="track-nav"><button type="button" id="prevCard" aria-label="Scheda precedente"><svg><use href="#i-arrow-l"/></svg></button><button type="button" id="nextCard" aria-label="Scheda successiva"><svg><use href="#i-arrow"/></svg></button></div>
</div></section>

<section class="pin isola" id="isola"><div class="stage">%(art_isola)s
  <div class="wrap">
    <div><p class="eyebrow">L’isola</p><h2 class="mt">Un'isola coinvolgente</h2>
      <p class="quote">Non è la specie più intelligente a sopravvivere e nemmeno quella più forte. <b>È quella più predisposta ai cambiamenti.</b></p>
      <div class="mt2"><a class="btn btn-primary" href="%(b)s/lisola/">scopri l'isola</a></div>
      <div class="isola-links"><a href="%(b)s/lisola/storia-di-jm/">Storia di J@M <svg><use href="#i-arrow"/></svg></a><a href="%(b)s/lisola/gli-abitanti/">Gli abitanti <svg><use href="#i-arrow"/></svg></a><a href="%(b)s/lisola/amici-partner/">Amici &amp; partner <svg><use href="#i-arrow"/></svg></a></div>
    </div>
    <img class="isola-art" id="isolaArt" src="%(a)s/isola.webp" width="994" height="673" alt="L'isola di J@M: una ragazza in una conchiglia tra le palme, con due piccoli abitanti">
  </div>
  <div class="sea"></div><span class="credit">M.C. Escher, Convesso e concavo · Museo J@M</span>
</div></section>

<section id="mood">
  <div class="mood-band">%(art_mood)s<div class="pattern"></div><h2>Mood</h2><span class="credit">Roy Lichtenstein · Museo J@M</span></div>
  <div class="tvh pad-s"><div class="wrap">
    <div data-reveal><p class="eyebrow">J@M Mood</p><h2 class="mt">TV</h2><p class="lede mt">Tutto ciò che è J@M è online. Fatti prendere da J@M!</p><div class="mt2"><a class="btn btn-outline" href="%(b)s/jm-mood/tv/">tutti i video %(chev)s</a></div></div>
    %(tv)s
  </div></div>
</section>

<section class="pad-s"><div class="wrap"><div class="museo-head" data-reveal><p class="eyebrow">J@M Mood</p><h2>Museo</h2><p class="lede">J@M è uno specchio di così tante personalità ed esperienze diverse che non potrà mai restare identica a sé stessa a lungo.</p><div class="ctas"><a class="btn btn-primary" href="%(b)s/jm-mood/museo/">fatti ispirare</a></div></div></div></section>
%(wall)s

<section class="art-band">%(art_comm)s<div class="veil"></div><div class="wrap"><p class="eyebrow">La nostra community</p><blockquote>Se nasce una nuova piattaforma, un nuovo modo di connettersi, noi vogliamo essere i primi a scoprirla… per questo siamo ovunque.</blockquote>%(socials)s</div><span class="credit">Sandro Botticelli, La primavera · Museo J@M</span></section>
%(ig)s

<section class="art-band villaggi" id="villaggi">%(art_vill)s<div class="veil"></div><div class="wrap">
  <img class="villaggi-art" src="%(a)s/villaggi.webp" width="1000" height="1163" alt="Una ragazza pianta la bandiera J@M sulla cima di una montagna" data-float="30" data-reveal>
  <div data-reveal><p class="eyebrow">I villaggi</p><h2 class="mt">Una rete di villaggi</h2><p class="lede mt">Virtuali e fisici. Per J@M non esistono vincoli territoriali o di possibilità e le sue basi strategiche sono avamposti sulla terra ferma. E brulicano di vita.</p><div class="ctas mt2"><a class="btn btn-primary" href="%(b)s/i-villaggi/"><svg><use href="#i-pin"/></svg> trovaci</a></div></div>
</div><span class="credit">René Magritte, Golconda · Museo J@M</span></section>
%(form)s
%(lightbox)s
""" % {"art": art("art-escher-giorno-notte"), "art_isola": art("art-escher-convesso", lit=False), "art_mood": art("art-lichtenstein", lit=False, zoom=False),
       "art_comm": art("art-botticelli"), "art_vill": art("art-magritte-golconda", lit=True, zoom=False), "b": BASE, "a": A, "i": IMG, "chev": chev,
       "cards": passioni_cards(), "tv": tv_set("512464979"), "wall": museo_wall(MUSEO_WORKS[:14], "museo-parete"), "socials": SOCIALS, "ig": ig_band(), "form": form_section(), "lightbox": LIGHTBOX}

HOME_JS = """<script src="%s/home.js" defer></script>
<script>document.addEventListener("DOMContentLoaded",function(){var t=document.getElementById("track");document.getElementById("prevCard").addEventListener("click",function(){t.scrollBy({left:-400,behavior:"smooth"})});document.getElementById("nextCard").addEventListener("click",function(){t.scrollBy({left:400,behavior:"smooth"})});});</script>""" % A

page(BASE + "/", "J@M Passion - Consulenza professionale per imprese e privati",
     "Un'intera gamma di servizi per la tua casa e il tuo business: telefonia, luce e gas, auto noleggio, efficientamento energetico e servizi web.",
     HOME_BODY, extra_css=HOME_CSS, extra_js=HOME_JS, og_image=A + "/isola.webp")

# ================================================================ L'ISOLA
page(BASE + "/lisola/", "L'isola di J@M | Un territorio protetto e in continua espansione",
     "L'isola di J@M è emersa nel 2001: manifesto, storia, abitanti, amici e partner di un'agenzia di servizi insolita.",
     hero("art-escher-convesso", "Isola <span class=\"grad\">di J@M</span>", "L’isola di J@M è emersa nel 2001 ed è un territorio protetto ed in continua espansione. La popolazione è in costante aumento e gli abitanti sono soggetti singolari, a volte bizzarri ma sempre disponibili e accoglienti.", eyebrow="L’isola", ill="ill-isola-castello", ill_alt="La ragazza J@M davanti al castello dell'isola", credit="M.C. Escher, Convesso e concavo · Museo J@M")
     + art_band("art-escher-relativita", "“Non è la specie più intelligente a sopravvivere e nemmeno quella più forte. È quella più predisposta ai cambiamenti.”", credit="M.C. Escher, Relatività · Museo J@M", eyebrow="Manifesto", ctas='<a class="btn btn-primary" href="%s/lisola/manifesto/">leggi di più</a><a class="link" href="%s/jm-mood/museo/">lasciati ispirare %s</a>' % (BASE, BASE, chev))
     + split("Che lavoro fai?", "<p>Lavoro in un’agenzia di servizi. Ci occupiamo di telefonia, energia, servizi web, noleggio auto ed efficientamento energetico… questa è la versione letterale. E poi? E poi c’è la favola.</p>", "ill-storia-libro", "La ragazza J@M che legge un grande libro", ctas='<a class="btn btn-primary" href="%s/lisola/storia-di-jm/">storia di J@M</a>' % BASE)
     + split("Abitanti", "<p>Creature insolite, personalità irriverenti, propensione al cambiamento e passione da vendere.</p>", "ill-abitanti-skate", "Gli abitanti dell'isola sullo skateboard", rev=True, ctas='<a class="btn btn-primary" href="%s/lisola/gli-abitanti/">conoscili tutti</a>' % BASE)
     + split("Amici e partner", "<p>J@M sa adattarsi ad ogni nuovo tassello in modo che l’insieme sia eterogeneo e armonico allo stesso tempo.</p>", "ill-amici-partner", "La ragazza J@M abbraccia le mascotte", ctas='<a class="btn btn-primary" href="%s/lisola/amici-partner/">scoprili</a>' % BASE)
     + videos(["578444885", "580322413"], eyebrow="Dall’isola", title="Guarda l’isola")
     + cta_band("Vuoi essere uno dei nostri?", "salpa verso l'isola", BASE + "/lavora-con-noi/"), og_image=IMG + "/ill-isola-castello.webp")

# ================================================================ MANIFESTO
MANIFESTO_CSS = ".man p { color: var(--muted); font-size: clamp(1.1rem, 1.6vw, 1.35rem); line-height: 1.55; max-width: 62ch; } .man h2 { font-size: clamp(2rem, 4.6vw, 4rem); margin-top: 6px; } .man .blk { display: grid; gap: 18px; padding-block: clamp(40px, 6vw, 80px); border-top: 1px solid var(--line); } .man .blk:first-child { border-top: 0; }"
page(BASE + "/lisola/manifesto/", "Il manifesto J@M | Benvenuto intraprendente esploratore!",
     "Il manifesto di J@M: Darwin, il cambiamento e i pochi requisiti essenziali per vivere sull'isola: testa, cuore e spirito di iniziativa.",
     hero("art-escher-relativita", "Il manifesto", "Siamo nel 1859. Darwin, a seguito di lunghe esplorazioni intorno al mondo a bordo della nave Beagle, pubblica la sua teoria sull’evoluzione, in cui definisce, argomenta e verifica la tesi secondo cui le capacità di sopravvivenza di una specie sono definite dalla sua capacità di assimilare gradualmente una serie di piccoli cambiamenti positivi.", eyebrow="Benvenuto intraprendente esploratore", ill="ill-mettici-passione", ill_alt="La ragazza J@M con il cartello Mettici passione", credit="M.C. Escher, Relatività · Museo J@M", size="tall")
     + statement("È impossibile non rendersi conto di quanto il contenuto di questa citazione risulti ancora attuale. E così, non sulle incontaminate isole di allora ma nelle tecnologiche metropoli di oggi, vediamo ogni giorno quanto sia effettivamente il cambiamento a definire la capacità degli esseri viventi di adattarsi, progredire, crescere e garantirsi un futuro.", light="cambiamento|adattarsi|progredire|crescere")
     + """<section class="pad-s man"><div class="wrap narrow">
<div class="blk" data-reveal><p class="eyebrow">Salpa</p><p>L’isola di J@M è emersa nel 2001 ed è un territorio protetto ed in continua espansione. La popolazione è in costante aumento e gli abitanti sono soggetti singolari, a volte bizzarri ma sempre disponibili e accoglienti.</p><div class="ctas"><a class="btn btn-outline" href="%(b)s/lisola/gli-abitanti/">scopri gli abitanti %(c)s</a></div></div>
<div class="blk" data-reveal><p class="eyebrow">Approda</p><p>Il successo nei rapporti di affari con la terraferma è favorito dalla diversificazione delle attività produttive e dalla capacità di anticipare le tendenze dei mercati.</p><p>J@M vanta numeri da industria ma ha quell’attenzione al dettaglio tipica dell’artigianato. È una comunità operosa: tutti si danno da fare ed ogni mansione ha come imprescindibile obiettivo la cura del cliente.</p><p>Le idee circolano liberamente dentro e fuori dall’isola, grazie ad innovativi canali di comunicazione che garantiscono un vincente equilibrio tra velocità ed affidabilità.</p></div>
<div class="blk" data-reveal><p class="eyebrow">L’agricoltura</p><p>L’agricoltura si concentra sulla coltivazione di relazioni di lunga durata e non trascura mai il rispetto verso l’ambiente. Tutte le offerte Luce e Gas prevedono infatti Energia Verde e sostenibile per ogni utente senza alcun costo aggiuntivo.</p></div>
<div class="blk" data-reveal><p class="eyebrow">Gli spostamenti</p><p>Sull’isola gli spostamenti di lavoro e di piacere vengono agevolati da soluzioni di Noleggio Auto su misura degli abitanti e dei loro clienti che, per primi, hanno potuto sperimentare la guida di auto elettriche e a zero emissioni.</p></div>
<div class="blk" data-reveal><p class="eyebrow">La lingua</p><p>La lingua è trasparente come l’acqua e si basa sui principi di correttezza, semplicità e chiarezza, dal vivo come nel Web.</p><p>L’isola è infatti innamorata delle nuove forme di comunicazione e cura Siti, Seo e App per permettere a tutti di restare in contatto con il mondo intero in pochi click.</p></div>
<div class="blk" data-reveal><p class="eyebrow">Le leggi</p><p>Per gli isolani le leggi sono semplici e servono ad assicurare coesione e rispetto del gruppo.</p><h2>Bastano pochi, essenziali, requisiti: <span class="grad">testa, cuore e spirito di iniziativa.</span></h2><p>Ricorda che i confini dell’isola non sono definiti, ovunque tu ti trovi ora, quello è il tuo porto di arrivo.</p><p>Quando avrai finito di fare il tuo giro, apri bene gli occhi. Il panorama forse sarà completamente mutato, ma tu non ti sentirai perso o solo, perché avrai individuato nuovi punti di riferimento.</p></div>
</div></section>""" % {"b": BASE, "c": chev}
     + cta_band("Se il viaggio ti è piaciuto, potresti decidere di rimanere sull’isola!", "trasferisciti", BASE + "/lavora-con-noi/"), extra_css=MANIFESTO_CSS, og_image=IMG + "/art-escher-relativita.webp")

# ================================================================ STORIA
page(BASE + "/lisola/storia-di-jm/", "La storia di J@M | Che lavoro fai?",
     "C'era una volta e oggi più che mai un'agenzia di servizi di nome J@M: la versione letterale e la favola.",
     hero("art-amano", "Che lavoro fai?", "Lavoro in un’agenzia di servizi, ci occupiamo di telefonia ed energia per aziende e per privati, siamo competitivi nelle offerte di autonoleggio e realizziamo siti web e applicazioni per i nostri clienti. <b>Questa è la versione letterale. E poi c’è la favola.</b>", eyebrow="Storia di J@M", ill="ill-isola-castello", ill_alt="La ragazza J@M davanti al castello dell'isola", credit="Yoshitaka Amano, Minitokyo · Museo J@M")
     + split("C'era una volta e oggi più che mai...", "<p>…un’agenzia di servizi di nome J@M. Una formazione compatta di professionisti cresciuti sull’onda della liberalizzazione di telefonia ed energia e che, interpretando o anticipando le mosse dei mercati, hanno costruito una community che condivide un solido ed incrollabile pensiero: <b style=\"color:var(--paper)\">i clienti sono carissimi amici.</b></p><p>Un amico va ascoltato, compreso, non va mai lasciato solo. È questo l’impegno che prendiamo nei suoi confronti perché, come un buon amico, continui a scegliere noi e tutta la gamma dei servizi che proponiamo.</p>", "ill-storia-mongolfiera", "La mongolfiera 'Amici carissimi' di J@M", ctas='<a class="btn btn-primary" href="%s/lisola/manifesto/">leggi il manifesto di J@M</a>' % BASE)
     + statement("Ogni cliente è un grandissimo amico", light="amico", eyebrow="Rosso passione, rosso J@M")
     + split("Servizi web", "<p>È per questo che ci impegniamo nel curare la sua comunicazione con servizi web innovativi e App personalizzate, con campagne marketing che ottimizzino la sua visibilità tramite accorgimenti e analisi a partire dal posizionamento SEO.</p>", "ill-storia-web", "Le app e i social di J@M", rev=True, compact=True, ctas='<a class="btn btn-outline" href="%s/passioni/servizi-web/">servizi web %s</a>' % (BASE, chev))
     + split("Telefonia", "<p>È per questo che accompagniamo i nostri amici nella sostituzione di tecnologie obsolete per ottenere, grazie alla fibra o al 5G, le migliori prestazioni in vista dell’avvento dell’Internet Of Things.</p>", "ill-storia-telefonia", "La cabina telefonica J@M", compact=True, ctas='<a class="btn btn-outline" href="%s/passioni/telecomunicazioni/">telefonia %s</a>' % (BASE, chev))
     + split("Energia", "<p>È per questo che per luce e gas ci impegniamo a far godere i nostri clienti di sensibili risparmi con la sottoscrizione di contratti dinamici che variano al variare del prezzo delle materie prime, puntando sempre ad ottenere il massimo vantaggio.</p>", "ill-storia-energia", "La lampadina neon Passion", rev=True, compact=True, ctas='<a class="btn btn-outline" href="%s/passioni/energia/">energia %s</a>' % (BASE, chev))
     + split("Efficientamento", "<p>È per questo che miglioriamo le prestazioni degli immobili dei nostri clienti grazie all’accesso ai bonus energetici disponibili.</p>", "ill-storia-efficientamento", "La casa efficiente di J@M", compact=True, ctas='<a class="btn btn-outline" href="%s/passioni/efficientamento-energetico/">efficientamento %s</a>' % (BASE, chev))
     + split("Ma non basta!", "<p>Siamo imbattibili nelle proposte di autonoleggio a medio e lungo termine ed esploriamo con i nostri clienti le varie opportunità offerte dal campo assicurativo.</p>", "ill-storia-noleggio", "L'auto sportiva di J@M", rev=True, compact=True, ctas='<a class="btn btn-outline" href="%s/passioni/noleggio-auto/">noleggio auto %s</a>' % (BASE, chev))
     + """<section class="pad-s"><div class="wrap"><div class="narrow" style="margin-bottom:36px" data-reveal><p class="eyebrow">Rosso passione, rosso J@M</p><h2 class="mt">Siamo agenti, siamo assistenza telefonica, siamo back office e front office, siamo programmatori e designer, siamo ricerca del personale e scuola di formazione.</h2></div>
<div class="siamo" data-stagger>%s</div><div class="ctas mt3" style="justify-content:center"><a class="btn btn-primary" href="%s/lisola/gli-abitanti/">siamo J@M</a></div></div></section>""" % ("".join('<figure><img src="%s/siamo-%s.webp" width="800" height="800" loading="lazy" alt="Siamo %s"></figure>' % (IMG, s, s.replace("-", " ")) for s in ["irriverenti", "appassionati", "coinvolgenti", "sempre-diversi", "sognatori", "visionari"]), BASE)
     + videos(["647319404", "647318735", "647320084", "647316925", "647319998", "647319919"], eyebrow="In video", title="Siamo J@M"), og_image=IMG + "/ill-storia-mongolfiera.webp")

# ================================================================ ABITANTI
page(BASE + "/lisola/gli-abitanti/", "Gli abitanti dell'isola di J@M | Personalità irriverenti e passione da vendere",
     "Avventurieri ed esploratori: gli abitanti dell'isola di J@M, viaggiatori inarrestabili e appassionati.",
     hero("art-southpark", "Gli abitanti", "“J@M è uno specchio di così tante personalità ed esperienze diverse che non potrà mai restare identica a se stessa a lungo”.", eyebrow="L’isola", ill="ill-abitanti-cassetta", ill_alt="La ragazza J@M alla cassetta delle lettere", credit="South Park · Museo J@M")
     + split("Avventurieri ed esploratori", "<p>Devi sapere che avventurieri ed esploratori non mancano di certo, in questa eclettica realtà che è J@M. Sono stati proprio quelli più impavidi a dare origine a tutto quello che siamo oggi ed a guidare questa loro grande squadra alla scoperta del mondo del business.</p>", "ill-abitanti-nave", "La ragazza J@M al timone")
     + split("Con coraggio", "<p>Con coraggio, abbiamo timonato in direzione di isole precluse ai timorosi, verso le quali ci siamo diretti con vele gonfie di entusiasmo, tra correnti contrastanti di ragione e azzardo, per sbarcare infine come pionieri.</p>", "ill-nave-pirata", "La nave di J@M", rev=True)
     + split("Viaggiatori inarrestabili", "<p>Viaggiatori inarrestabili e appassionati, animati dalla giusta dose di follia e di propensione al mutamento. <b style=\"color:var(--paper)\">In una parola: siamo J@M!</b></p>", "ill-abitanti-danza", "La ragazza J@M che danza tra le stelle")
     + cta_band("Vuoi essere uno dei nostri?", "scopri come", BASE + "/lavora-con-noi/"), og_image=IMG + "/ill-abitanti-nave.webp")

# ================================================================ AMICI & PARTNER
page(BASE + "/lisola/amici-partner/", "Amici e partner | Gli elementi fondamentali di J@M",
     "Gli amici e i partner di J@M: Controcorrente Gas e Luce e PagineWeb.",
     hero("art-picasso", "Amici e partner", "J@M sa adattarsi ad ogni nuovo tassello in modo che l’insieme sia eterogeneo e armonico allo stesso tempo. Ogni nostro amico ci ispira e si fa ispirare da noi, proprio per questo non ci troverai mai uguali a lungo.", eyebrow="L’isola", ill="ill-amici-partner", ill_alt="La ragazza J@M con le mascotte", credit="Pablo Picasso, Les demoiselles d’Avignon · Museo J@M")
     + statement("Tutti i nostri amici sono come noi e mettono tanta passione in quello che fanno ma sono anche un po’ insoliti…", light="passione|insoliti")
     + """<section class="pad-s"><div class="wrap"><div class="partners" data-stagger>
<a class="partner" href="%s/passioni/energia/"><img src="%s/partner-controcorrente.webp" loading="lazy" alt="Controcorrente Gas e Luce"><b>Controcorrente Gas e Luce</b></a>
<a class="partner" href="http://www.pagineweb.it" rel="noopener"><img src="%s/partner-pagineweb.webp" loading="lazy" alt="PagineWeb"><b>PagineWeb</b></a>
</div></div></section>""" % (BASE, IMG, IMG) + ig_band(), og_image=IMG + "/ill-amici-partner.webp")

# ================================================================ LAVORA CON NOI
page(BASE + "/lavora-con-noi/", "Lavora con noi | Hai abbastanza carattere?",
     "J@M è insolita: solida come un'industria, visionaria come una startup. Requisiti: testa, cuore e spirito d'iniziativa.",
     hero("art-escher-giorno-notte", "Lavora con noi", "J@M è insolita. È la migliore disorganizzazione perfettamente organizzata. È solida come un’industria ma visionaria come una startup. È un’isola creativa, è sperimentale, è una scommessa.", eyebrow="Salpa verso l’isola", ill="ill-giostra", ill_alt="La giostra di J@M", credit="M.C. Escher, Giorno e notte · Museo J@M")
     + statement("Ogni abitante della nostra isola può emergere grazie a dinamismo, passione e originalità. Qui le opportunità sono tante e i requisiti sono pochi ma, attenzione, veramente essenziali: testa, cuore e spirito d’iniziativa.", light="dinamismo|passione|originalità|testa|cuore|spirito|d’iniziativa", sub="Ma c’è una cosa importantissima: non considerare mai una gara scontata, ci dev’essere sempre un fuoco che ti accenda.")
     + form_section("Hai abbastanza carattere?", "Dimostracelo e candidati!", subject="Candidatura dal sito J@M", msg_label="Lettera di presentazione (opzionale) — allega il CV alla mail che si aprirà", button="candidati", phone=False), og_image=IMG + "/ill-giostra.webp")

# ================================================================ PASSIONI
PASS_CSS = ".pass-list .split .ill { width: min(100%, 520px); }"
page(BASE + "/passioni/", "Le nostre passioni | Un'intera gamma di servizi per la casa e per il business",
     "J@M è un'azienda consolidata, eclettica e piena di iniziativa: telecomunicazioni, energia, servizi web, efficientamento energetico, noleggio auto.",
     hero("art-vettriano", "Le nostre passioni", "J@M è un’azienda consolidata, eclettica e piena di iniziativa, che si occupa di consulenza professionale per aziende e privati. Dedichiamo una particolare attenzione alla cura e alla fidelizzazione del cliente e lo facciamo grazie ad una eccezionale rete vendita, fidata e motivata.", eyebrow="Passioni", credit="Jack Vettriano, The Singing Butler · Museo J@M", size="tall")
     + statement("Il consulente commerciale J@M può proporre numerosi prodotti, suggerendo efficaci strategie di investimento: siti Web, Seo, App, auto a noleggio, telefonia, energia verde e molto altro.", light="siti|seo|app|auto|telefonia|energia", sub="La molteplicità delle sue specializzazioni arricchisce il suo valore ed apre al cliente uno stimolante ventaglio di possibilità.")
     + '<div class="pass-list">'
     + split("Telecomunicazioni", "<p>Proponiamo le migliori soluzioni e offerte di telefonia mobile e fissa per il tuo business e le personalizziamo a seconda delle tue esigenze. Chiami, messaggi e navighi senza limiti con la massima velocità, che tu sia in ufficio, fuori casa o in fondo al mare.</p>", "ill-tlc-alexa", "La ragazza J@M in ufficio con gli smart object", eyebrow="Passione 01", ctas='<a class="btn btn-primary" href="%s/passioni/telecomunicazioni/">scopri</a>' % BASE, compact=True)
     + split("Energia", "<p>Con energia e passione ti proponiamo soluzioni di fornitura luce e gas competitive da far paura. Progettiamo offerte innovative di energia verde e sostenibile, proveniente da fonti rinnovabili e a basso impatto ambientale.</p>", "ill-energia-malefica", "La ragazza J@M con la fata del bosco", rev=True, eyebrow="Passione 02", ctas='<a class="btn btn-primary" href="%s/passioni/energia/">scopri</a>' % BASE, compact=True)
     + split("Servizi web", "<p>Offriamo supporto e consulenza professionale in campo digitale. Come? Creiamo siti web e app ottimizzati in ottica SEO per scalare i motori di ricerca. Progettiamo campagne di digital marketing e ti aiutiamo ad accrescere il tuo business utilizzando il potere dei social media!</p>", "ill-web-alice", "La ragazza J@M nel paese delle meraviglie digitale", eyebrow="Passione 04", ctas='<a class="btn btn-primary" href="%s/passioni/servizi-web/">scopri</a>' % BASE, compact=True)
     + split("Efficientamento energetico", "<p>Offriamo consulenza e supporto per migliorare le prestazioni energetiche del tuo immobile grazie all’accesso ai bonus attivi. Superbonus, ecobonus, fotovoltaico e tanto altro per farti dire addio agli spifferi e ai ponti termici.</p>", "ill-eff-frozen-casa", "La casa con i pannelli solari", rev=True, eyebrow="Passione 05", ctas='<a class="btn btn-primary" href="%s/passioni/efficientamento-energetico/">scopri</a>' % BASE, compact=True)
     + split("Auto noleggio", "<p>Promuoviamo la mobilità sostenibile attraverso i nostri servizi di noleggio auto a medio e a lungo termine. Progettiamo soluzioni all-inclusive per semplificarti la vita e liberarti dalla burocrazia. Perché? Perché guidare deve essere un piacere!</p>", "ill-auto-tappeto", "L'auto volante di J@M", eyebrow="Passione 03", ctas='<a class="btn btn-primary" href="%s/passioni/noleggio-auto/">scopri</a>' % BASE, compact=True)
     + '</div>'
     + statement("Questo è quello che facciamo. Ma non basta a descriverci, non c’è un modo di definire J@M, c’è un mondo a definire J@M.", light="mondo|j@m") + form_section(), extra_css=PASS_CSS, og_image=IMG + "/art-vettriano.webp")

# ================================================================ TELECOMUNICAZIONI
page(BASE + "/passioni/telecomunicazioni/", "Telecomunicazioni | Piani telefonia e internet per il tuo business",
     "Fibra FTTH, 5G, Internet of Things e soluzioni business personalizzate: le telecomunicazioni secondo J@M.",
     hero("art-escher-giorno-notte", "Ma per chi mi hai presa?!", "Non è una conchiglia… <b>È uno smart object…</b>", eyebrow="Telecomunicazioni", ill="ill-tlc-conchiglia", ill_alt="La sirena J@M con la conchiglia", ctas='<a class="btn btn-primary" href="#soluzioni">le nostre soluzioni business</a>', credit="M.C. Escher, Giorno e notte · Museo J@M")
     + split("L'innovazione è intorno a noi", "<p>Il mondo è sempre più veloce e l’innovazione digitale e tecnologica ci fa scorgere un futuro sempre più ibrido in cui realtà virtuale e fisica si incontrano senza soluzione di continuità.</p><p>Prima controllare elettrodomestici con la voce sembrava fantascienza, oggi si chiama Internet of Things (Internet delle cose o IoT), quegli oggetti intelligenti si chiamano Smart Objects e sono sempre più numerosi e ovunque.</p>", "ill-tlc-alexa", "La ragazza J@M parla con l'assistente vocale")
     + split("È questione di connessioni", "<p>Nelle case, negli uffici, nelle città: l’integrazione digitale degli oggetti di uso comune diventa sempre più importante, mettendo in evidenza le innumerevoli possibilità di sostenibilità economica e ambientale.</p><p>Per abbracciare questo futuro con la migliore efficienza ti forniamo connessioni wifi sempre più veloci, efficienti e convenienti. Miglioriamo la tua copertura grazie all’utilizzo della banda larga, della fibra con tecnologia FTTH e delle ultime innovazioni tecnologiche permesse dalla rete 5G, quest’ultima sempre più diffusa sul territorio.</p>", "ill-tlc-pesci", "I pesci connessi di J@M", rev=True)
     + split("Ogni cliente è diverso", "<p>Perciò ogni soluzione non può che essere personalizzata a seconda delle specifiche esigenze di ogni azienda.</p>", "ill-tlc-sirena", "La sirena J@M", compact=True)
     + statement("Okay, ma in poche parole?", sub="Soluzioni business: componi la tua offerta personalizzata!", light="poche|parole")
     + feats([("Per parlare, per navigare", "Minuti e giga illimitati", "Per comunicare fuori e dentro l’azienda in maniera veloce, efficiente e sicura grazie alle ultime innovazioni del mercato."),
              ("Per viaggiare", "Roaming voce e dati", "Per annullare le distanze, anche se sei all’estero."),
              ("Per lavorare ovunque", "Smartworking", "I migliori strumenti di smartworking per adattare la tua attività a qualsiasi tipo di comunicazione e collaborazione a distanza."),
              ("Internet of Things", "Oggetti connessi", "Rendi tutti gli oggetti del tuo ufficio interconnessi tra loro e ottimizza l’organizzazione della tua azienda."),
              ("Sicurezza & App", "Dispositivi sicuri", "Lavora in totale sicurezza con tutti i tuoi dispositivi business e implementa i tuoi processi operativi con app digitali personalizzate.")], ident="soluzioni")
     + form_section(msg_label="Hai una richiesta in particolare? (facoltativo)", subject="Richiesta telecomunicazioni dal sito J@M"), og_image=IMG + "/ill-tlc-conchiglia.webp")

# ================================================================ ENERGIA
page(BASE + "/passioni/energia/", "Forniture luce e gas | Con J@M scegli energia verde e sostenibile!",
     "Offerte luce e gas per qualsiasi tipologia di cliente, energia 100% verde certificata, nuove attivazioni, volture, subentri e allacci.",
     hero("art-yerka", "È perché non hai mai usato energia così pura.", "", eyebrow="Energia", ill="ill-energia-malefica", ill_alt="La ragazza J@M e la fata della foresta", ctas='<a class="btn btn-primary" href="#sostenibile">energia sostenibile</a><a class="btn btn-outline" href="#servizi">servizi</a>', credit="Jacek Yerka, By the waters · Museo J@M")
     + split("Offriamo piani di fornitura energetica", "<p>Attraverso le offerte luce e gas più convenienti ed aggiornate per qualsiasi tipologia di cliente.</p><p>Personalizziamo ogni soluzione energetica in relazione allo specifico target di consumo e seguiamo la tua pratica costantemente in modo da tenerti sempre aggiornato riguardo ogni ribasso del mercato. Se c’è una novità più conveniente sei sempre il primo a saperlo.</p>", "ill-energia-orologio", "La mascotte J@M con l'orologio da taschino")
     + split("Energia sostenibile", "<p>Smettere d’inquinare non significa utilizzare meno energia ma utilizzare energia migliore e conoscere l’impatto del proprio stile di vita.</p><p>Perché? Perché le risorse del pianeta sono sempre meno e l’inquinamento è sempre maggiore: tutto ciò a ritmi record. Ma il cambiamento è iniziato.</p><p>Distributori coraggiosi, come i nostri amici di Controcorrente Gas e Luce, hanno scelto di offrire ai propri clienti solo energia verde e certificata, 100% naturale e proveniente da fonti rinnovabili come l’eolico, il fotovoltaico, il geotermico e l’idroelettrico.</p>", "ill-energia-eolico", "La ragazza J@M tra le pale eoliche", rev=True, ident="sostenibile")
     + split("Perché progresso significa semplicità", "<p>Per passare all’energia verde non devi cambiare i tuoi elettrodomestici o la tecnologia degli impianti. E il contatore? Neanche quello.</p><p>Se ti stai chiedendo cosa cambi la risposta è semplice. L’energia elettrica è la stessa ma il suo percorso è molto più bello perché ha origine dalla natura: niente più carbone, niente più combustibili fossili. In compenso respiri aria molto più pulita, specialmente perché un’azienda inquina in media più di un’abitazione.</p>", "ill-energia-barca", "La barca di J@M nella foresta", compact=True)
     + feats([("Rispetto", "È rispettosa", "nei confronti dell’ambiente e del pianeta"), ("Emissioni", "Emissioni minime", "rispetto all’energia tradizionale e proveniente dai combustibili fossili"), ("Disponibilità", "Disponibilità illimitata", "come le fonti rinnovabili da cui l’energia verde proviene"), ("Altruismo", "È altruista", "nei confronti delle future generazioni che verranno in nome di un futuro ancora vivibile")], eyebrow="Energia verde", title="I vantaggi")
     + feats([("Consulenza", "Nella fornitura di luce e gas", "Valutiamo la tua situazione con il fornitore attuale e i tuoi consumi per fascia oraria con l’obiettivo di fornirti la migliore offerta in relazione alle tue specifiche esigenze."), ("Gestione", "Delle forniture di luce e gas", "Nuove attivazioni, volture, subentri, nuovi allacci contatore.")], eyebrow="I nostri servizi", title="Consulenza e gestione", ident="servizi")
     + feats([("Come?", "Contratto", "relativo ad un nuovo allaccio, un subentro o una voltura"), ("", "Monitoraggio", "costante della pratica in ogni fase d’avanzamento"), ("", "Aggiornamento", "costante delle tariffe per farti stare sempre al passo con le novità")])
     + form_section(msg_label="Hai una richiesta in particolare? (facoltativo)", subject="Richiesta energia dal sito J@M"), og_image=IMG + "/ill-energia-malefica.webp")

# ================================================================ NOLEGGIO AUTO
page(BASE + "/passioni/noleggio-auto/", "Noleggio auto a medio e lungo termine | Così magico che non sembra vero",
     "Noleggio auto a medio e lungo termine con tutte le spese incluse, anche elettrico: guida senza pensare alla burocrazia.",
     hero("art-magritte-golconda", "“Così magico che non sembra vero.”", "cit. Chiunque provi la semplicità dei nostri servizi di noleggio auto.", eyebrow="Auto noleggio", ill="ill-auto-tappeto", ill_alt="L'auto volante di J@M", credit="René Magritte, Golconda · Museo J@M")
     + split("Crea le tue nuove certezze e guida verso il futuro", "<p>Grazie ai nostri servizi di auto noleggio a medio o a lungo termine puoi goderti il piacere della guida senza pensare alla burocrazia. Come? Scegliendo un pacchetto unico con tutte le spese incluse.</p>", "ill-auto-aladdin", "La ragazza J@M con l'auto rossa")
     + split("Mobilità sostenibile", "<p>Scopri la guida senza emissioni a bordo delle nostre auto elettriche a noleggio. Può essere l’occasione per decidere di testarla e comprarne una in futuro!</p>", "ill-auto-lampada", "La ragazza J@M con la lampada magica", rev=True)
     + feats([("Vantaggi", "Costi di ricarica ridotti", '<a class="link" href="%s/passioni/efficientamento-energetico/#colonnine">bonus colonnine elettriche %s</a>' % (BASE, chev)), ("Vantaggi", "Esenzione bollo auto", "per cinque anni"), ("Vantaggi", "Copertura assicurativa", "scontata del 50%"), ("Vantaggi", "Accesso alle ZTL", ""), ("Vantaggi", "Parcheggio gratuito", "in tantissime città italiane!"), ("Vantaggi", "Detrazione fiscale", "Per l’acquisto e l’installazione delle colonnine di ricarica rapida.")], eyebrow="Elettrico", title="I vantaggi")
     + statement("Sì sì, ma qual è il mio desiderio?", sub="Puoi scegliere.", light="desiderio")
     + feats([("Puoi scegliere", "Tipologia vettura", "utilitaria, sportiva etc."), ("Puoi scegliere", "Durata", "dai 12 ai 48 mesi"), ("Puoi scegliere", "Chilometraggio", "su misura"), ("Puoi scegliere", "Personalizzazione", "colori, finiture, accessori…"), ("Puoi scegliere", "Franchigia", "per danni e furto o incendio")])
     + form_section(msg_label="Hai una richiesta in particolare? (facoltativo)", subject="Richiesta noleggio auto dal sito J@M"), og_image=IMG + "/ill-auto-tappeto.webp")

# ================================================================ SERVIZI WEB
page(BASE + "/passioni/servizi-web/", "Servizi web | Web design, digital marketing e social media",
     "Siti web, SEO, campagne Google Ads, social advertising, contenuti e copywriting: il web secondo J@M, insieme agli amici di PagineWeb.",
     hero("art-lichtenstein", "Il web è pieno di matti", "Devi esserlo anche tu… Altrimenti non saresti qui!", eyebrow="Servizi web", ill="ill-web-alice", ill_alt="La ragazza J@M nel paese delle meraviglie digitale", ctas='<a class="btn btn-primary" href="#webdesign">web design</a><a class="btn btn-outline" href="#digitalmarketing">digital marketing</a><a class="btn btn-outline" href="#socialmedia">social media</a>', credit="Roy Lichtenstein · Museo J@M")
     + split("Rilassati", "<p>Siamo qui proprio per farti arrivare primo!</p>", "ill-web-relax", "La ragazza J@M dice Relax", compact=True)
     + split("Metti in scena il tuo business", "<p>Oggi essere online è indispensabile ma lo è anche il modo in cui ci presentiamo. Valorizzare un’azienda online è, per noi, come lavorare nel backstage di un teatro. Ci appassiona conoscere la trama della narrazione e quali attori sono coinvolti in modo che l’esibizione sia fantastica ed indimenticabile per il pubblico.</p><p>Come facciamo? Utilizziamo i migliori strumenti digitali per far spiccare il volo a tutte le tue piattaforme e farti avere la massima visibilità online.</p>", "ill-web-sipario", "Lo Stregatto sul sipario", rev=True)
     + feats([("Web design", "Realizzazione", "Progettazione e costruzione di siti web per il tuo business (vetrine, portfolio, e-commerce…)"), ("Web design", "Usabilità", "Progettazione dell’esperienza utente in modalità responsive (desktop, tablet, mobile) per una corretta visualizzazione su tutti i dispositivi"), ("Web design", "Mantenimento", "Implementazione e aggiornamento del tuo sito web già esistente"), ("Web design", "Ottimizzazione", "Ottimizzazione del tuo sito web per una corretta visualizzazione su tutti i browser (Chrome, Safari, Firefox, Edge etc.)")], eyebrow="Web", title="Design", ident="webdesign")
     + split("Strategia", "<p>Le nostre campagne pubblicitarie offrono un’estrema flessibilità, permettendoti di misurare concretamente le prestazioni e di analizzarle grazie a report dettagliati alla conclusione dell’attività promozionale.</p>", "ill-web-strategia", "La lavagna Strategia di J@M", compact=True)
     + feats([("Digital marketing", "SEO", "Search Engine Optimization | Miglioramento del posizionamento del tuo sito web sui motori di ricerca."), ("Digital marketing", "Insights", "Monitoraggio delle prestazioni (traffico online e rendimento) attraverso strumenti di analisi e reportistica."), ("Digital marketing", "Vetrine digitali", 'Creazione dello spazio online brandizzato insieme ai nostri amici di <a class="link" href="http://www.pagineweb.it" rel="noopener">Pagine Web</a>.'), ("Digital marketing", "Advertising", "Campagne pubblicitarie su Google Ads."), ("Digital marketing", "Email marketing", "Strategie di marketing attraverso l'azione su uno specifico target come, ad esempio, la tua lista di contatti.")], eyebrow="Digital", title="Marketing", ident="digitalmarketing")
     + split("Social media", "<p>Vuoi fornire ai tuoi clienti un’esperienza online inedita e fuori dagli schemi? Preparati, daremo il massimo per te.</p>", "ill-web-instagram", "Il profilo Instagram di J@M", rev=True, compact=True, ident="socialmedia", ctas='<a class="btn btn-primary" href="#contatti">contattaci</a>')
     + feats([("Social media", "Social advertising", "Creazione e gestione di inserzioni pubblicitarie su Facebook e Instagram con elaborazione di reportistica alla fine delle campagne."), ("Social media", "Contenuti", "Creazione di materiale multimediale brandizzato per la pubblicazione di post, stories e tanto altro."), ("Social media", "Copywriting", "Creazione di contenuti testuali persuasivi per aumentare le interazioni dei tuoi follower e aumentare l'engagement su tutti i tuoi account aziendali.")])
     + form_section(msg_label="Hai una richiesta in particolare? (facoltativo)", subject="Richiesta servizi web dal sito J@M"), og_image=IMG + "/ill-web-alice.webp")

# ================================================================ EFFICIENTAMENTO
page(BASE + "/passioni/efficientamento-energetico/", "Gli ecobonus | Aumenta l'efficienza energetica del tuo immobile con J@M",
     "Sostituzione caldaia e climatizzatore, fotovoltaico, colonnine elettriche, cappotto e infissi: efficientamento energetico con J@M.",
     hero("art-escher-convesso", "Almeno non sei freddolosa. Ne riparleremo d’estate!", "", eyebrow="Efficientamento energetico", ill="ill-eff-frozen-casa", ill_alt="La casa efficiente con i pannelli solari", credit="M.C. Escher, Convesso e concavo · Museo J@M")
     + split("Sostituzione caldaia", "<p>Sostituisci la tua caldaia con un impianto ibrido o full electric. Puoi ottenere fino al 50% sulla prima casa e il 36% sulla seconda.</p><p><b style=\"color:var(--paper)\">Detrai fino al 50% dell'importo.</b></p>", "ill-eff-caldaia", "La caldaia con le mascotte", eyebrow="Per privati · Ecobonus fino al 50%", ctas='<a class="btn btn-primary" href="#contatti">contattaci</a>')
     + feats([("Come interveniamo?", "Progettazione", "Con i migliori professionisti del settore e utilizziamo le migliori tecnologie leader di mercato: le più affidabili e con le migliori prestazioni."), ("", "Installazione", ""), ("", "Collaudo", ""), ("", "Smaltimento", "")])
     + split("Sostituzione climatizzatore", "<p>Rinnova il clima della tua casa con il minimo sforzo. Sostituisci il tuo vecchio climatizzatore ed installa un nuovo modello a pompa di calore e ad alta efficienza energetica!</p><p>Grazie alle migliori prestazioni del tuo impianto di climatizzazione potrai soddisfare i nuovi requisiti di efficientamento e accedere immediatamente ad uno sconto fino al 50% sul totale dei costi dell’intervento: progettazione, realizzazione, installazione, smaltimento.</p>", "ill-eff-clima", "Il climatizzatore installato", rev=True, eyebrow="Per privati · Ecobonus fino al 50%", ctas='<a class="btn btn-primary" href="#contatti">contattaci</a>')
     + split("Ecobonus fotovoltaico", "<p>Produci l’energia che ti serve in totale autonomia e dì addio alle bollette.</p>", "ill-eff-secchi", "La ragazza J@M porta l'energia", eyebrow="Per privati · Ecobonus fotovoltaico fino al 50%", ident="bonusfotovoltaico", ctas='<a class="btn btn-primary" href="#contatti">contattaci</a>')
     + feats([("Vantaggi", "Indipendenza energetica", "Grazie ad un impianto fotovoltaico trasformi l’energia solare in energia elettrica e puoi utilizzarla all’interno della tua abitazione o della tua azienda in totale autonomia."), ("Vantaggi", "Sostenibilità ambientale", "Installare un impianto fotovoltaico è uno dei modi più facili ed efficienti per consumare elettricità senza inquinare l’ambiente!"), ("Vantaggi", "Valore immobile", "La presenza di un impianto fotovoltaico migliora fortemente le prestazioni energetiche del tuo immobile aumentandone sia il valore sia la classe energetica. Inoltre, il valore aggiunto dal fotovoltaico dura nel tempo."), ("Vantaggi", "Risparmi denaro", "Il fotovoltaico è un investimento sicuro a lungo termine per il tuo portafogli perché ti permette di ridurre sensibilmente le tue spese legate all’energia e l’importo delle bollette. Oltre a produrre in totale autonomia la tua energia puoi addirittura conservare ciò che non consumi e utilizzarlo quando c’è buio o nelle giornate nuvolose."), ("Vantaggi", "Puoi guadagnare", "Il fotovoltaico rappresenta anche un valido strumento di guadagno per i possessori: l’energia “in avanzo” viene introdotta nella rete a vantaggio sia della comunità sia tuo, con un premio riconosciuto dal GSE.")])
     + feats([("Detrai il 50%", "Relazioni tecniche", "Compenso per relazioni tecniche di garanzia della conformità dell’impianto in relazione alla normativa vigente."), ("Detrai il 50%", "Progettazione e consulenza", "Spese di progettazione dell’impianto e prestazioni professionali connesse."), ("Detrai il 50%", "Manodopera", "Per l'installazione dell'impianto."), ("Detrai il 50%", "Installazione", "Dell’impianto fotovoltaico, dell’eventuale sistema di accumulo e di tutti gli accessori."), ("Detrai il 50%", "Burocrazia", "Gestione delle pratiche riguardanti il GSE")])
     + split("Ecobonus 50% colonnine elettriche", "<p>Grazie alla crescente domanda di mobilità elettrica sono lontani i tempi in cui le postazioni di ricarica per le auto elettriche apparivano come miraggi nelle nostre città. Oggi crescono come funghi e costituiscono una rete capillare anche in Italia, sia negli spazi pubblici sia in quelli privati!</p><p>Per accelerare il percorso verso una mobilità elettrica confortevole e per tutti, negli ultimi anni sono stati introdotti alcuni incentivi fiscali con l’obiettivo di incoraggiare l’installazione dei punti di ricarica.</p>", "ill-eff-colonnina", "L'auto elettrica alla colonnina", rev=True, eyebrow="Per privati · Detrai il 50% dell'importo", ident="colonnine", ctas='<a class="btn btn-primary" href="#contatti">contattaci</a>')
     + feats([("Colonnine", "Tipologia potenza", "3,7 - 22 kW"), ("Colonnine", "Fase", "monofase, trifase o altro"), ("Colonnine", "Modalità ricarica", "su misura per la tua auto")])
     + feats([("Impianto", "Nuove tecnologie", "Sostituiamo il tuo vecchio impianto climatico invernale con le ultime tecnologie del mercato come, ad esempio, caldaie a condensazione e pompe di calore."), ("Struttura", "Cappotto isolante", "Realizziamo nuovi sistemi di cappotto isolante e facciamo fare un salto di almeno due classi energetiche al tuo immobile. Avrai uno sconto in fattura."), ("Prestazioni", "Fotovoltaico e accumulo", "Installiamo nel tuo immobile un impianto fotovoltaico ad alte prestazioni implementato con accumulatori performanti e colonnine per la ricarica della tua auto elettrica."), ("Infissi", "Nuovi infissi", "Sostituiamo i tuoi infissi con nuovi modelli e con oscuranti di ultima generazione.")], eyebrow="Condomini e immobili", title="Come interveniamo")
     + form_section(msg_label="Hai una richiesta in particolare? (facoltativo)", subject="Richiesta efficientamento energetico dal sito J@M", extra_fields='<div class="field"><label for="c-bonus">Quale bonus ti interessa?</label><select id="c-bonus" name="bonus"><option>Ecobonus caldaia</option><option>Ecobonus climatizzatore</option><option>Ecobonus fotovoltaico</option><option>Ecobonus colonnine elettriche</option><option>Cappotto e infissi</option></select></div>'), og_image=IMG + "/ill-eff-frozen-casa.webp")

# ================================================================ J@M MOOD
page(BASE + "/jm-mood/", "J@M Mood | Le etichette sono per i prodotti, non per le persone",
     "TV, Museo, Community e J@M Session: il mood di J@M.",
     hero("art-lichtenstein", "Mood", "Le etichette sono per i prodotti, non per le persone.", eyebrow="J@M Mood", ill="ill-mood-pittrice", ill_alt="La ragazza J@M dipinge", credit="Roy Lichtenstein · Museo J@M")
     + split("TV", "<p>Tutto ciò che è J@M è online. Fatti prendere da J@M!</p>", "ill-mood-rec", "La ragazza J@M davanti alla telecamera", ctas='<a class="btn btn-primary" href="%s/jm-mood/tv/">buona visione</a>' % BASE)
     + split("Museo", "<p>Il fascino dell’ignoto, il gusto della scoperta che solo una realtà sempre uguale e sempre diversa come J@M ti può dare.</p>", "ill-mood-pittrice", "La ragazza J@M davanti al cavalletto", rev=True, ctas='<a class="btn btn-primary" href="%s/jm-mood/museo/">tutte le opere</a>' % BASE)
     + split("Community", "<p>Se nasce una nuova piattaforma, un nuovo modo di connettersi, noi vogliamo essere i primi a scoprirla… per questo siamo ovunque.</p>", "ill-community-telefono", "La ragazza J@M esce dallo smartphone", ctas='<a class="btn btn-primary" href="%s/jm-mood/community/">villaggi virtuali</a>' % BASE)
     + split("Session", "<p>Amiamo la condivisione. Per questo abbiamo dato inizio alle nostre Convention!</p>", "ill-session-globo", "La ragazza J@M sul mappamondo", rev=True, ctas='<a class="btn btn-primary" href="%s/jm-mood/jm-session/">tutte le convention</a><a class="link" href="%s/jm-mood/jm-session/#perilmondo">nel mondo %s</a><a class="link" href="%s/jm-mood/jm-session/#conventionitalia">in Italia %s</a>' % (BASE, BASE, chev, BASE, chev)), og_image=IMG + "/ill-mood-pittrice.webp")

# ================================================================ TV
TV_IDS = ["117800499", "512473622", "185233391", "1179828843", "1103047986", "896813618", "77122095", "77122208", "77129210", "77130633", "232316666", "118795260", "512473962"]
page(BASE + "/jm-mood/tv/", "J@M TV | Tutti i video",
     "Tutti immortalati nei momenti più belli e più improbabili: i video di J@M.",
     hero("art-lichtenstein", "TV", "Tutti immortalati nei momenti più belli e più improbabili. Stili di vita, visioni, prospettive, personalità. Tutto al plurale. Non ci piace semplificarci e descriverci in poche righe.", eyebrow="J@M Mood", credit="Roy Lichtenstein · Museo J@M", size="short")
     + '<section class="pad-s"><div class="wrap">' + tv_set("512464979") + '</div></section>'
     + videos(TV_IDS, eyebrow="Lasciati ispirare", title="Fatti prendere da J@M")
     + """<section class="pad-s"><div class="wrap"><div class="feats" data-stagger>
<div class="feat"><span class="k">Lasciati ispirare</span><h3>Scopri l’isola</h3><p><a class="link" href="%(b)s/lisola/manifesto/">il manifesto %(c)s</a></p></div>
<div class="feat"><span class="k">Fatti prendere da J@M</span><h3>Scopri gli abitanti</h3><p><a class="link" href="%(b)s/lisola/gli-abitanti/">gli abitanti %(c)s</a></p></div>
<div class="feat"><span class="k">Mettici passione</span><h3>Dai valore alla realtà</h3><p><a class="link" href="%(b)s/lisola/storia-di-jm/">la storia di J@M %(c)s</a></p></div>
<div class="feat"><span class="k">Condividere il momento</span><h3>Le convention</h3><p>Con questo intento abbiamo dato inizio alle nostre Convention, momenti in cui riunire tutta la nostra creativa e insolita rete di vendita. <a class="link" href="%(b)s/jm-mood/jm-session/">tutte le convention %(c)s</a></p></div>
</div></div></section>""" % {"b": BASE, "c": chev}
     + cta_band("C'è ancora molto altro...", "continua a guardare", "https://vimeo.com/jamsrl"), og_image=IMG + "/ill-mood-rec.webp")

# ================================================================ MUSEO
page(BASE + "/jm-mood/museo/", "Museo J@M | Il fascino dell'ignoto, il gusto della scoperta",
     "Le opere del Museo J@M: capolavori reinterpretati con la ragazza dai capelli rossi, appesi nelle sedi di Milano, Cantù, Torino, Lecce, Bologna, Roma, Verona e Padova.",
     hero("art-escher-relativita", "Museo", "Il fascino dell’ignoto, il gusto della scoperta che solo una realtà sempre uguale e sempre diversa come J@M ti può dare.", eyebrow="J@M Mood", credit="M.C. Escher, Relatività · Museo J@M", size="short")
     + statement("J@M è insolita. J@M è creativa. Un’inguaribile romantica. Quando riesci a descriverla è già diventata qualcos’altro. Cammina ad occhi chiusi, sogna ad occhi aperti.", light="insolita|creativa|romantica|sogna", sub="“Quest’opera non l’ho mai capita fino in fondo. Esattamente come J@M.”")
     + museo_grid(MUSEO_WORKS) + LIGHTBOX
     + cta_band("Fatti prendere da J@M", "vuoi chiederci qualcosa?", BASE + "/#contatti"), og_image=MUSEO + "/11-van-gogh-notte-stellata150x1185cm.webp")

# ================================================================ COMMUNITY
page(BASE + "/jm-mood/community/", "Community J@M | Siamo ovunque",
     "Quando nasce una nuova piattaforma, noi vogliamo essere i primi a scoprirla. Per questo siamo ovunque.",
     hero("art-botticelli", "Community", "Quando nasce una nuova piattaforma, un nuovo modo di connettersi, noi vogliamo essere i primi a scoprirla e ci piace esserci e sperimentare, sporcarci le mani e assorbire conoscenza e ispirazione da tutto ciò che è inedito e incredibile.", eyebrow="J@M Mood", ill="ill-community-telefono", ill_alt="La ragazza J@M esce dallo smartphone", credit="Sandro Botticelli, La primavera · Museo J@M")
     + statement("Per questo siamo ovunque.", light="ovunque") + '<section class="pad-s"><div class="wrap">' + SOCIALS + '</div></section>' + ig_band() + form_section(), og_image=IMG + "/ill-community-telefono.webp")

# ================================================================ SESSION
def tl(items):
    return '<div class="timeline"><div class="prog"></div>%s</div>' % "".join('<div class="tstep"><span class="dot"></span><span class="y">%s</span><h3>%s</h3>%s</div>' % (y, t, ('<p>%s</p>' % q) if q else "") for y, t, q in items)
MONDO = [("2019", "Dubai", "“Il deserto è Gold Passion.”"), ("2015", "Cuba", "“Divertirsi lavorando o lavorare divertendosi? Entrambe le cose direi.”"), ("2013", "Djerba", "“… è un momento di discontinuità, un momento in cui fondiamo le basi per quello che saremo.”"), ("2011", "Mykonos", "“La migliore disorganizzazione perfettamente organizzata. La perfetta gestione degli opposti.”"), ("2009", "Ibiza", "“La gara non deve essere mai scontata perché altrimenti non c’è quel fuoco che vi deve accendere.”")]
ITALIA = [("2019", "18 anni di J@M", ""), ("2018", "Buena vista social J@M", "“Noi siamo a volte online, a volte offline ma siamo sempre ONLIFE.”"), ("2017", "Controcorrente", "“Un futuro che è controcorrente a quella che è l’attività tipica di ogni agenzia. La rottura di un paradigma.”"), ("2016", "Andiamo a comandare", "“J@M è ancora un’adolescente e come tutti gli adolescenti ha ancora voglia di divertirsi e ha ancora voglia di combattere”."), ("2016", "FollowApp", "“J@M è relativa, dipende da dove la guardi, da come la guardi e da quanto la guardi.”"), ("2014", "Pedala", "“Il coraggio sta nello scegliere tra essere standard o essere J@M.”"), ("2014", "J@M yourself", "“Chi è che lascia una strada certa e facile per una incerta? Solo chi è così sicuro di quello che sta facendo.”"), ("2012", "Yes we J@M!", ""), ("2006", "Bringing it all together", "")]
SESSION_IDS = ["512473962", "167712868", "84664681", "44094296", "44094436", "333702326", "309853017", "248291367", "232316666", "231360550", "185233391", "128161394", "96504894", "51907529", "645995961"]
page(BASE + "/jm-mood/jm-session/", "J@M Session | Le convention di J@M nel mondo e in Italia",
     "Amiamo la condivisione: le convention J@M da Ibiza a Dubai e in Italia, con la nostra creativa e insolita rete di vendita.",
     hero("art-mappa-convention", "J@M session", "Amiamo la condivisione. Per questo abbiamo dato inizio alle nostre Convention, momenti in cui riunire tutta la nostra creativa e insolita rete di vendita per celebrare gli obiettivi raggiunti con passione e inaugurare l’inizio di nuove avventure visionarie.", eyebrow="J@M Mood", ill="ill-session-globo", ill_alt="La ragazza J@M sul mappamondo", ctas='<a class="btn btn-primary" href="#perilmondo">nel mondo</a><a class="btn btn-outline" href="#conventionitalia">in Italia</a>', credit="La mappa delle convention J@M")
     + split("Le convention", "<p>In ogni Convention abbiamo portato la nostra isola per il mondo scegliendo dei luoghi speciali che sprigionassero la nostra stessa energia. Perché siamo una marea trascinante.</p><p>Requisiti per partecipare? Tanta voglia di avventura e nuove possibilità.</p>", "ill-nave-pirata", "La nave delle convention")
     + '<section class="pad-s" id="perilmondo"><div class="wrap narrow"><p class="eyebrow" data-reveal>Nel mondo · …finora…</p><h2 class="mt" style="margin-bottom:40px" data-reveal>Nel mondo</h2>%s</div></section>' % tl(MONDO)
     + '<section class="pad-s" id="conventionitalia"><div class="wrap narrow"><p class="eyebrow" data-reveal>In Italia · …finora…</p><h2 class="mt" style="margin-bottom:40px" data-reveal>In Italia</h2>%s</div></section>' % tl(ITALIA)
     + videos(SESSION_IDS, eyebrow="In video", title="Le convention")
     + cta_band("C'è ancora molto altro...", "continua a guardare", "https://vimeo.com/jamsrl"), og_image=IMG + "/ill-session-globo.webp")

# ================================================================ I VILLAGGI
SEDI = [("sede-milano", "Milano", "Via Rutilia 2,4 · 20141 Milano (MI)"), ("sede-cantu", "Cantù", "Il villaggio in Brianza"), ("sede-torino", "Torino", "Il villaggio piemontese"), ("sede-lecce", "Lecce", "Il villaggio nel Salento"), ("sede-bacau", "Bacău", "L’avamposto in Romania")]
page(BASE + "/i-villaggi/", "Sedi J@M | Scopri tutti i nostri villaggi virtuali e avamposti sulla terra ferma",
     "Le sedi di J@M: Milano, Cantù, Torino, Lecce, Bacău. Villaggi fisici e virtuali costruiti con passione ardente e follia creativa.",
     hero("art-magritte-golconda", "Una rete di villaggi", "Ci servivano tanti luoghi, fisici e virtuali, che ci aiutassero a non disperdere le nostre idee una volta uscite dalle nostre teste. Così ci siamo divertiti a invadere il territorio.", eyebrow="I villaggi", ill="ill-villaggi-virtuali", ill_alt="I villaggi virtuali di J@M", credit="René Magritte, Golconda · Museo J@M")
     + statement("Fatti prendere da J@M e fai un tour dei nostri villaggi: sono tappe obbligate. Costruiti con passione ardente e follia creativa. Ogni sede ha la sua storia, la sua personalità, il suo stile.", light="passione|follia|creativa")
     + '<section class="pad-s"><div class="wrap"><div class="sedi" data-stagger>%s</div></div></section>' % "".join('<div class="sede"><img src="%s/%s.webp" loading="lazy" alt="La sede J@M di %s"><h3>%s</h3><p>%s</p></div>' % (IMG, f, c, c, d) for f, c, d in SEDI)
     + split("Villaggi virtuali", "<p>Virtuali e fisici. Per J@M non esistono vincoli territoriali o di possibilità e le sue basi strategiche sono avamposti sulla terra ferma. E brulicano di vita.</p>", "ill-villaggi-virtuali", "I villaggi virtuali di J@M", ctas='<a class="btn btn-primary" href="https://goo.gl/maps/fMUuxLyYvvjXLSaB6" rel="noopener"><svg><use href="#i-pin"/></svg> trovaci</a><a class="link" href="%s/jm-mood/community/">la community %s</a>' % (BASE, chev))
     + form_section() + cta_band("Hai abbastanza carattere? Dimostracelo e candidati.", "inizia l'avventura", BASE + "/lavora-con-noi/"), og_image=IMG + "/sede-milano.webp")

# ---------------------------------------------------------------- scrittura
def write():
    n = 0
    for path, (title, desc, body, kw) in PAGES.items():
        rel = path[len(BASE):].strip("/")
        out_dir = os.path.join(ROOT, rel.replace("/", os.sep)) if rel else ROOT
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "index.html"), "w", encoding="utf-8", newline="\n") as f:
            f.write(layout(path, title, desc, body, **kw))
        n += 1
    print("scritte", n, "pagine")

if __name__ == "__main__":
    write()
