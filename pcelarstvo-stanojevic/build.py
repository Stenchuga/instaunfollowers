#!/usr/bin/env python3
"""Generates the static site (Serbian at site/, English at site/en/).

Run:  python3 build.py
Texts live in this file; products and prices live in site/assets/products.js.
"""
import os

ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "site")

PHONE = "064 128 5796"
PHONE_INTL = "+381641285796"
EMAIL = "goxyst@mts.rs"
PLACE = {"sr": "Smederevska Palanka, Srbija", "en": "Smederevska Palanka, Serbia"}
SITE = "https://www.pcelarstvo-stanojevic.com"

# Google titles (what shows up as the blue link in search results)
SEO_TITLE = {
    ("sr", "index"): "Pčelarstvo Stanojević – med, pčelinji otrov i apikomora | Smederevska Palanka",
    ("en", "index"): "Stanojević Beekeeping – honey, bee venom and api-chamber | Serbia",
    ("sr", "prodavnica"): "Prodavnica – med, propolis i kreme sa pčelinjim otrovom | Pčelarstvo Stanojević",
    ("en", "prodavnica"): "Shop – honey, propolis and bee venom creams | Stanojević Beekeeping",
    ("sr", "apitox-sakupljac"): "Apitox sakupljač pčelinjeg otrova – nagrađena inovacija | Pčelarstvo Stanojević",
    ("en", "apitox-sakupljac"): "Apitox bee venom collector – award-winning device | Stanojević Beekeeping",
    ("sr", "apikomora"): "Apikomora – inhalacija vazduhom iz košnice, Smederevska Palanka | Pčelarstvo Stanojević",
    ("en", "apikomora"): "Api-chamber – breathing beehive air, Serbia | Stanojević Beekeeping",
    ("sr", "apifigura"): "ApiFigura – krema sa pčelinjim otrovom protiv bora | Pčelarstvo Stanojević",
    ("en", "apifigura"): "ApiFigura – anti-wrinkle cream with bee venom | Stanojević Beekeeping",
    ("sr", "apisalus"): "ApiSalus – krema sa pčelinjim otrovom | Pčelarstvo Stanojević",
    ("en", "apisalus"): "ApiSalus – bee venom cream | Stanojević Beekeeping",
    ("sr", "propolis-krema"): "ProPolis krema – mast od propolisa | Pčelarstvo Stanojević",
    ("en", "propolis-krema"): "ProPolis cream – propolis ointment | Stanojević Beekeeping",
}
NOINDEX = {"korpa"}


def url(lang, slug):
    path = "" if slug == "index" else f"{slug}.html"
    return f"{SITE}/{'en/' if lang == 'en' else ''}{path}"


def jsonld(data):
    import json
    return '<script type="application/ld+json">' + json.dumps(data, ensure_ascii=False) + "</script>"


def business_ld(lang):
    return jsonld({
        "@context": "https://schema.org", "@type": "LocalBusiness",
        "name": "Pčelarstvo Stanojević", "alternateName": "Stanojević Beekeeping",
        "description": "Porodično pčelarstvo – med, pčelinji proizvodi, kozmetika sa pčelinjim otrovom, apikomora i Apitox sakupljač pčelinjeg otrova.",
        "url": SITE + "/", "image": SITE + "/img/054.jpg", "logo": SITE + "/img/001.png",
        "telephone": PHONE_INTL, "email": EMAIL, "founder": {"@type": "Person", "name": "Goran Stanojević"},
        "address": {"@type": "PostalAddress", "addressLocality": "Smederevska Palanka", "addressCountry": "RS"},
        "areaServed": "RS", "priceRange": "RSD",
    })

# ---------------------------------------------------------------- icons
IC = {
    "comb": '<svg viewBox="0 0 24 24"><path d="M12 2 16 4.5v5L12 12 8 9.5v-5z"/><path d="M8 9.5 4 12v5l4 2.5 4-2.5v-5M16 9.5l4 2.5v5l-4 2.5-4-2.5"/></svg>',
    "house": '<svg viewBox="0 0 24 24"><path d="M3 11 12 4l9 7"/><path d="M5 10v10h14V10"/><path d="M9 20v-5h6v5"/></svg>',
    "bee": '<svg viewBox="0 0 24 24"><ellipse cx="12" cy="14" rx="4" ry="6"/><path d="M8 12h8M8 16h8M10 6.5 9 4M14 6.5 15 4"/><path d="M8.5 10C4 7 2 10 4 12s4.5-.5 4.5-.5M15.5 10C20 7 22 10 20 12s-4.5-.5-4.5-.5"/></svg>',
    "award": '<svg viewBox="0 0 24 24"><circle cx="12" cy="9" r="6"/><path d="m9 9 2 2 4-4M8 14l-2 7 6-3 6 3-2-7"/></svg>',
    "frame": '<svg viewBox="0 0 24 24"><rect x="4" y="6" width="16" height="12" rx="1"/><path d="M4 10h16M4 14h16M8 6v12M12 6v12M16 6v12"/></svg>',
    "people": '<svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3"/><circle cx="17" cy="9" r="2.5"/><path d="M3 20c0-4 3-6 6-6s6 2 6 6M15 14c3 0 6 2 6 5"/></svg>',
    "phone": '<svg viewBox="0 0 24 24"><path d="M5 4h4l2 5-3 2a11 11 0 0 0 5 5l2-3 5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2"/></svg>',
    "mail": '<svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3 7 9 6 9-6"/></svg>',
    "pin": '<svg viewBox="0 0 24 24"><path d="M12 21s7-6 7-12a7 7 0 0 0-14 0c0 6 7 12 7 12z"/><circle cx="12" cy="9" r="2.5"/></svg>',
    "cart": '<svg viewBox="0 0 24 24"><path d="M3 4h2l2.5 11h11L21 7H6.5"/><circle cx="9" cy="19" r="1.5"/><circle cx="17" cy="19" r="1.5"/></svg>',
    "truck": '<svg viewBox="0 0 24 24"><path d="M3 6h11v10H3zM14 10h4l3 3v3h-7"/><circle cx="7" cy="17" r="2"/><circle cx="17" cy="17" r="2"/></svg>',
    "check": '<svg viewBox="0 0 24 24"><path d="m5 12 5 5 9-10"/></svg>',
    "chat": '<svg viewBox="0 0 24 24"><path d="M4 5h16v11H9l-5 4z"/></svg>',
}


def hexi(name):
    return f'<span class="hexi"><i>{IC[name]}</i></span>'


# ---------------------------------------------------------------- UI strings
UI = {
    "sr": {
        "nav": [("index", "Početna"), ("prodavnica", "Prodavnica"), ("apitox-sakupljac", "Apitox sakupljač"),
                ("apikomora", "Apikomora"), ("galerija", "Galerija"), ("kontakt", "Kontakt")],
        "cart": "Korpa", "brand_small": "Pčelarstvo", "motto": "Zdravlje iz košnice…",
        "menu": "Meni", "site": "Pčelarstvo Stanojević",
    },
    "en": {
        "nav": [("index", "Home"), ("prodavnica", "Shop"), ("apitox-sakupljac", "Apitox collector"),
                ("apikomora", "Api-chamber"), ("galerija", "Gallery"), ("kontakt", "Contact")],
        "cart": "Cart", "brand_small": "Beekeeping", "motto": "Health from the hive…",
        "menu": "Menu", "site": "Stanojević Beekeeping",
    },
}


def page(lang, slug, title, desc, body, current=None, ld="", image="054.jpg"):
    u = UI[lang]
    b = "" if lang == "sr" else "../"          # path back to site root (assets, img)
    here = "" if lang == "sr" else ""           # pages of same language are siblings
    other = ("en/" if lang == "sr" else "../") + f"{slug}.html"
    nav = "".join(
        f'<a href="{here}{s}.html"{" class=\"on\"" if s == (current or slug) else ""}>{n}</a>' for s, n in u["nav"])
    sr_on = ' class="on"' if lang == "sr" else ""
    en_on = ' class="on"' if lang == "en" else ""
    lang_sw = (f'<a{sr_on} href="{"" if lang == "sr" else "../"}{slug}.html" hreflang="sr">SR</a> | '
               f'<a{en_on} href="{"en/" if lang == "sr" else ""}{slug}.html" hreflang="en">EN</a>')
    full_title = SEO_TITLE.get((lang, slug)) or (u["site"] if slug == "index" else f"{title} – {u['site']}")
    alt_sr = f"{'' if lang == 'sr' else '../'}{slug}.html"
    return f"""<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{full_title}</title>
<meta name="description" content="{desc}">
{'<meta name="robots" content="noindex">' if slug in NOINDEX else ''}
<link rel="canonical" href="{url(lang, slug)}">
<link rel="alternate" hreflang="sr" href="{url('sr', slug)}">
<link rel="alternate" hreflang="en" href="{url('en', slug)}">
<link rel="alternate" hreflang="x-default" href="{url('sr', slug)}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{u['site']}">
<meta property="og:title" content="{full_title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url(lang, slug)}">
<meta property="og:image" content="{SITE}/img/{image}">
<meta property="og:locale" content="{'sr_RS' if lang == 'sr' else 'en_US'}">
<meta name="twitter:card" content="summary_large_image">
{ld}
<link rel="icon" href="{b}img/001.png">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Lora:ital,wght@0,500;0,600;0,700;1,500&family=Nunito+Sans:wght@400;600;700;800&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{b}assets/style.css">
</head>
<body data-base="{b}">
<header><div class="wrap">
 <a class="logo" href="index.html"><img src="{b}img/001.png" alt=""><span><small>{u['brand_small']}</small><b>Stanojević</b></span></a>
 <nav class="main"><a class="close" href="javascript:void 0" aria-label="×">×</a>{nav}</nav>
 <div class="hr"><span class="lang">{lang_sw}</span>
  <a class="cartbtn" href="korpa.html">{IC['cart']}<span class="t">{u['cart']}</span><span class="n">0</span></a>
  <button class="burger" aria-label="{u['menu']}"><svg viewBox="0 0 24 24"><path d="M3 6h18M3 12h18M3 18h18"/></svg></button>
 </div>
</div></header>
{body}
<footer class="wood"><div class="wrap">
 <a class="logo" href="index.html"><img src="{b}img/001.png" alt=""><span><small>{u['brand_small']}</small><b>Stanojević</b></span></a>
 <div class="ct">
  <div>{IC['phone']}<a href="tel:{PHONE_INTL}">{PHONE}</a></div>
  <div>{IC['mail']}<a href="mailto:{EMAIL}">{EMAIL}</a></div>
  <div>{IC['pin']}{PLACE[lang]}</div>
  <div><b>Goran Stanojević</b></div>
 </div>
 <div class="motto">{u['motto']}</div>
</div><div class="copy">© 2026 {u['site']}</div></footer>
<script src="{b}assets/products.js"></script>
<script src="{b}assets/app.js"></script>
</body>
</html>
"""


def banner(lang, img, kick, title, sub=""):
    b = "" if lang == "sr" else "../"
    s = f"<p>{sub}</p>" if sub else ""
    return (f'<section class="banner" style="background-image:url({b}img/{img})"><div class="wrap">'
            f'<div class="kick left">{kick}</div><h1>{title}</h1>{s}</div></section>')


def gal(lang, items):
    """items: list of (img, caption)"""
    b = "" if lang == "sr" else "../"
    return '<div class="gal">' + "".join(
        f'<a href="{b}img/{i}" data-cap="{c}"><img src="{b}img/{i}" alt="{c}" loading="lazy">'
        + (f"<span>{c}</span>" if c else "") + "</a>" for i, c in items) + "</div>"


def fig(lang, img, cap=""):
    b = "" if lang == "sr" else "../"
    fc = f"<figcaption>{cap}</figcaption>" if cap else ""
    return f'<figure><img src="{b}img/{img}" alt="{cap}" loading="lazy">{fc}</figure>'


# ================================================================ HOME
def home(lang):
    b = "" if lang == "sr" else "../"
    if lang == "sr":
        t = dict(kick="Tradicija, priroda i kvalitet", h1="Pčelarstvo<br>Stanojević",
                 s="Zdravlje iz košnice,<br>pravo sa našeg pčelinjaka.", cta="Pogledajte proizvode",
                 f=["Prirodni med<br>i pčelinji proizvodi", "Apikomora –<br>zdravlje iz košnice",
                    "Sakupljanje<br>pčelinjeg otrova", "Nagrada za<br>najbolju inovaciju"],
                 about_s="O nama", about_h="Pčelarstvo sa tradicijom",
                 about="Pčelarstvo Stanojević je porodično pčelarstvo iz Smederevske Palanke, koje vodi Goran Stanojević. Pored meda i ostalih "
                       "pčelinjih proizvoda, bavimo se sakupljanjem pčelinjeg otrova, izradom sopstvenih Apitox "
                       "sakupljača nagrađenih na državnom sajmu pčelarstva, kozmetikom na bazi pčelinjeg otrova i "
                       "propolisa, kao i apikomorom – boravkom u vazduhu iz košnice.",
                 welcome_h="Dobrodošli!",
                 welcome="Na čelu lestvice prirodne zdrave hrane su pčelinji proizvodi: med, polen, matični mleč i "
                         "propolis. Pčele su nam podarile idealnu hranu koja zadovoljava sve potrebe ljudskog organizma.",
                 more="Apitox sakupljač",
                 prod_h="Naši proizvodi", prod_s="Prirodni proizvodi sa našeg pčelinjaka",
                 hx=["Med", "Polen", "Propolis", "Matični mleč", "Pčelinji otrov"],
                 cos=[("apifigura", "004.png", "ApiFigura", "Krema sa pčelinjim otrovom"),
                      ("apisalus", "005.png", "ApiSalus", "Pčelinje zdravlje"),
                      ("propolis-krema", "006.png", "ProPolis", "Krema na bazi propolisa")],
                 shop="Pogledajte prodavnicu",
                 serv_s="Šta još radimo", serv_h="Naše usluge",
                 serv=[("house", "Apikomora", "Inhalacija i ležanje nad košnicama, od aprila do avgusta", "apikomora"),
                       ("frame", "Apitox sakupljač", "Nagrađeni uređaj za sakupljanje pčelinjeg otrova", "apitox-sakupljac"),
                       ("people", "Posete i predavanja", "Škole, studenti i pčelari iz zemlje i inostranstva", "galerija")],
                 gal_h="Galerija", gal_p="Naši pčelinjaci, apikomora i druženja", gal_b="Otvorite galeriju",
                 award="Prvo mesto na državnom sajmu pčelarstva za najbolju inovaciju")
        desc = "Porodično pčelarstvo iz Smederevske Palanke – domaći med, polen, propolis, matični mleč, kreme sa pčelinjim otrovom, apikomora i nagrađeni Apitox sakupljač."
    else:
        t = dict(kick="Tradition, nature and quality", h1="Stanojević<br>Beekeeping",
                 s="Health from the hive,<br>straight from our apiary.", cta="See our products",
                 f=["Natural honey<br>and bee products", "Api-chamber –<br>health from the hive",
                    "Bee venom<br>collection", "Award for<br>best innovation"],
                 about_s="About us", about_h="Beekeeping with tradition",
                 about="Stanojević Beekeeping is a family apiary from Smederevska Palanka, run by Goran Stanojević. Besides honey and other bee "
                       "products, we collect bee venom, build our own Apitox venom collectors – awarded at the national "
                       "beekeeping fair – make cosmetics based on bee venom and propolis, and run an api-chamber where "
                       "visitors breathe the air from the hive.",
                 welcome_h="Welcome!",
                 welcome="Bee products – honey, pollen, royal jelly and propolis – are at the very top of natural, "
                         "healthy food. Bees have given us an ideal food that meets all the needs of the human body.",
                 more="Apitox collector",
                 prod_h="Our products", prod_s="Natural products from our apiary",
                 hx=["Honey", "Pollen", "Propolis", "Royal jelly", "Bee venom"],
                 cos=[("apifigura", "004.png", "ApiFigura", "Cream with bee venom"),
                      ("apisalus", "005.png", "ApiSalus", "Bee health"),
                      ("propolis-krema", "006.png", "ProPolis", "Propolis-based cream")],
                 shop="Visit the shop",
                 serv_s="What else we do", serv_h="Our services",
                 serv=[("house", "Api-chamber", "Breathing hive air and lying above the hives, April to August", "apikomora"),
                       ("frame", "Apitox collector", "Award-winning device for collecting bee venom", "apitox-sakupljac"),
                       ("people", "Visits and lectures", "Schools, students and beekeepers from home and abroad", "galerija")],
                 gal_h="Gallery", gal_p="Our apiaries, the api-chamber and meetings", gal_b="Open the gallery",
                 award="First place at the national beekeeping fair for best innovation")
        desc = "Family apiary from Smederevska Palanka, Serbia – honey, pollen, propolis, royal jelly, bee venom creams, api-chamber and the award-winning Apitox collector."

    feats = "".join(f'<div class="f">{hexi(i)}<span>{x}</span></div>'
                    for i, x in zip(["comb", "house", "bee", "award"], t["f"]))
    hx_pos = ["72% 30%", "12% 40%", "45% 70%", "90% 60%"]
    hexes = "".join(
        f'<a class="hx" href="prodavnica.html"><div class="h"><div style="background-image:url({b}img/049.jpg);'
        f'background-position:{p};background-size:420%"></div></div>{n}</a>' for p, n in zip(hx_pos, t["hx"][:4]))
    hexes += (f'<a class="hx" href="apitox-sakupljac.html"><div class="h"><div style="background-image:url({b}img/033.jpg)">'
              f'</div></div>{t["hx"][4]}</a>')
    cos = "".join(f'<a class="c" href="{s}.html"><img src="{b}img/{i}" alt="{n}"><span><b>{n}</b><small>{d}</small></span></a>'
                  for s, i, n, d in t["cos"])
    serv = "".join(f'<a class="sv" href="{l}.html">{hexi(i)}<h3>{h}</h3><p>{p}</p></a>' for i, h, p, l in t["serv"])

    body = f"""
<section class="hero" style="background-image:url({b}img/055.jpg)"><div class="wrap">
 <div class="kick">{t['kick']}</div>
 <h1>{t['h1']}</h1>
 <p class="s">{t['s']}</p>
 <a class="btn arrow" href="prodavnica.html">{t['cta']}</a>
</div></section>

<section class="feat wood"><div class="wrap">{feats}</div></section>

<section class="about paper" id="o-nama"><div class="wrap">
 <div class="polaroid"><img src="{b}img/054.jpg" alt=""></div>
 <div><div class="sub">{t['about_s']}</div><h2>{t['about_h']}</h2>
  <p>{t['about']}</p>
  <h3 style="font-size:22px;margin-bottom:6px">{t['welcome_h']}</h3>
  <p style="margin-top:0">{t['welcome']}</p>
  <a class="btn arrow dark" href="apitox-sakupljac.html">{t['more']}</a></div>
</div></section>

<section class="prod" style="background-image:url({b}img/049.jpg)"><div class="wrap">
 <div class="head"><h2>{t['prod_h']}</h2><div class="sub">{t['prod_s']}</div></div>
 <div class="hexes">{hexes}</div>
 <div class="cos">{cos}</div>
 <div style="text-align:center;margin-top:36px"><a class="btn arrow" href="prodavnica.html">{t['shop']}</a></div>
</div></section>

<section class="serv paper">
 <div class="l"><div class="sub">{t['serv_s']}</div><h2>{t['serv_h']}</h2><div class="cards">{serv}</div></div>
 <div class="r" style="background-image:url({b}img/051.jpg)"></div>
</section>

<section class="ga wood"><div class="wrap">
 <div class="gl">
  <div style="min-width:200px"><h2>{t['gal_h']}</h2><p>{t['gal_p']}</p><a class="btn arrow" href="galerija.html">{t['gal_b']}</a></div>
  <div class="photos"><img src="{b}img/053.jpg" alt=""><img src="{b}img/042.jpg" alt=""><img src="{b}img/056.jpg" alt=""></div>
 </div>
 <a class="award" href="apitox-sakupljac.html"><img src="{b}img/011.jpg" alt=""><div><div class="kick left" style="margin-bottom:8px">Apitox</div><b>{t['award']}</b></div></a>
</div></section>
"""
    return page(lang, "index", "", desc, body, ld=business_ld(lang), image="055.jpg")


# ================================================================ SHOP
def shop(lang):
    if lang == "sr":
        bn = banner(lang, "049.jpg", "Prodavnica", "Naši proizvodi", "Izaberite proizvode, a mi vas pozivamo da potvrdimo porudžbinu.")
        info = [("cart", "Dodajte proizvode u korpu"), ("phone", "Pozivamo vas radi potvrde"), ("truck", "Plaćanje pouzećem")]
        desc = "Prodavnica Pčelarstva Stanojević – kreme sa pčelinjim otrovom, med, polen, propolis i Apitox sakupljač."
        title = "Prodavnica"
    else:
        bn = banner(lang, "049.jpg", "Shop", "Our products", "Choose your products and we will call you to confirm the order.")
        info = [("cart", "Add products to the cart"), ("phone", "We call you to confirm"), ("truck", "Cash on delivery")]
        desc = "Stanojević Beekeeping shop – bee venom creams, honey, pollen, propolis and the Apitox collector."
        title = "Shop"
    infob = "".join(f"<div>{hexi(i)}{x}</div>" for i, x in info)
    body = f"""{bn}
<section class="content paper"><div class="wrap">
 <div class="chips" id="chips"></div>
 <div class="grid" id="shop-grid"></div>
 <div class="infobar">{infob}</div>
</div></section>"""
    return page(lang, "prodavnica", title, desc, body)


# ================================================================ PRODUCT PAGES
CREAMS = {
    "apifigura": dict(img="004.png", sr=dict(
        name="ApiFigura", tag="Pčelinja lepota",
        lead="ApiFigura – antirid – jedinstvena krema sa pčelinjim otrovom na našem tržištu, koja u svom sastavu sadrži i "
             "liofilizirani matični mleč. Sem što će zategnuti vaše bore, lice će vam biti meko i negovano. Topla preporuka "
             "osobama koje imaju problematičnu kožu, poput akni.",
        sastav="Pčelinji otrov, devičansko arganovo ulje, devičansko maslinovo ulje, ricinusovo ulje, shea butter, cocoa "
               "butter, etarsko ulje geranijuma, pčelinji vosak, manuka med, destilovana voda, vitamin E.",
        upotreba="Kremu namazati i utrljati na ciljano mesto (1–2 puta dnevno).",
        napomena="Osobe alergične na pčelinji otrov ne smeju koristiti kremu bez konsultacije sa lekarom. Nakon otvaranja "
                 "krema je stabilna 6 meseci. Čuvati na temperaturi do 35 °C."),
        en=dict(name="ApiFigura", tag="Bee Beauty",
        lead="ApiFigura – anti-wrinkle – the only cream with bee venom on our market that also contains freeze-dried royal "
             "jelly. Besides tightening your wrinkles, it will leave your face soft and nourished. Warmly recommended for "
             "people with problem skin, such as acne.",
        sastav="Bee venom, virgin argan oil, virgin olive oil, castor oil, shea butter, cocoa butter, geranium essential "
               "oil, beeswax, manuka honey, distilled water, vitamin E.",
        upotreba="Apply and rub into the target area (1–2 times a day).",
        napomena="People allergic to bee venom must not use the cream without consulting a doctor. After opening, the "
                 "cream remains stable for 6 months. Store at temperatures up to 35 °C.")),
    "apisalus": dict(img="005.png", sr=dict(
        name="ApiSalus", tag="Pčelinje zdravlje",
        lead="ApiSalus – pčelinje zdravlje – zahvaljujući kapsaicinu, kao jednom od sastojaka kreme, apitoksin (pčelinji "
             "otrov) brzo prodire kroz kožu i dovodi do poboljšanja cirkulacije i protoka krvi u perifernim delovima tela. "
             "Najvažniji sastojci apitoksina su melitin i adolapin. Melitin ima ulogu u smanjivanju krvnog pritiska, "
             "sprečava zgrušavanje krvi, deluje antibakterijski, štiti od zračenja i deluje na centralni nervni sistem. "
             "Adolapin ima ulogu u ublažavanju bolova i deluje antireumatski.",
        sastav="Pčelinji otrov, devičansko maslinovo ulje, devičansko konopljino ulje, pčelinji vosak, manuka med, "
               "destilovana voda, etarsko ulje eukaliptusa, etarsko ulje ruzmarina, ekstrakt ljute paprike i vitamin E.",
        upotreba="Kremu namazati i utrljati na ciljano mesto. Postupak ponoviti 2–3 puta dnevno.",
        napomena="Osobe alergične na pčelinji otrov ne smeju koristiti kremu bez konsultacije sa lekarom."),
        en=dict(name="ApiSalus", tag="Bee Health",
        lead="ApiSalus – bee health – thanks to capsaicin, one of the cream's ingredients, apitoxin (bee venom) quickly "
             "penetrates the skin and improves circulation and blood flow in the peripheral parts of the body. The most "
             "important components of apitoxin are melittin and adolapin. Melittin plays a role in lowering blood pressure, "
             "prevents blood clotting, has an antibacterial effect, protects against radiation and acts on the central "
             "nervous system. Adolapin helps relieve pain and has an anti-rheumatic effect.",
        sastav="Bee venom, virgin olive oil, virgin hemp oil, beeswax, manuka honey, distilled water, eucalyptus essential "
               "oil, rosemary essential oil, chili pepper extract and vitamin E.",
        upotreba="Apply and rub into the target area. Repeat 2–3 times a day.",
        napomena="People allergic to bee venom must not use the cream without consulting a doctor.")),
    "propolis-krema": dict(img="006.png", sr=dict(
        name="ProPolis krema", tag="Na bazi propolisa",
        lead="ProPolis krema – propolis mast izrađena je na bazi prirodnih sastojaka. Zahvaljujući svom sastavu, može se "
             "koristiti za negu kože sa ekcemima, gljivičnim i bakterijskim bolestima, kod hemoroida, psorijaze, žuljeva, "
             "kurjih očiju, opekotina, promrzlina i slično.",
        sastav="Ekstrakt propolisa, sirovi propolis, devičansko maslinovo ulje, macerat nevenovog ulja, macerat "
               "kantarionovog ulja, kakao buter, med, vosak, geogard.",
        upotreba="Kremu namazati i utrljati na ciljano mesto. Postupak ponoviti 2–3 puta dnevno.",
        napomena="Osobe alergične na propolis ne smeju koristiti kremu bez konsultacije sa lekarom."),
        en=dict(name="ProPolis cream", tag="Propolis-based",
        lead="ProPolis cream – a propolis ointment made from natural ingredients. Thanks to its composition, it can be "
             "used for the care of skin with eczema, fungal and bacterial conditions, and for hemorrhoids, psoriasis, "
             "calluses, corns, burns, frostbite and similar.",
        sastav="Propolis extract, raw propolis, virgin olive oil, calendula oil macerate, St John's wort oil macerate, "
               "cocoa butter, honey, beeswax, Geogard.",
        upotreba="Apply and rub into the target area. Repeat 2–3 times a day.",
        napomena="People allergic to propolis must not use the cream without consulting a doctor.")),
}


def cream(lang, slug):
    d = CREAMS[slug]
    t = d[lang]
    b = "" if lang == "sr" else "../"
    L = dict(sr=("Sastav", "Način upotrebe", "Napomena", "Kontrolu vrši Gradski zavod za javno zdravlje. Broj: 15-08-1142",
                 "Dodaj u korpu", "← Nazad u prodavnicu"),
             en=("Ingredients", "How to use", "Note", "Tested by the City Institute of Public Health. No. 15-08-1142",
                 "Add to cart", "← Back to shop"))[lang]
    body = f"""{banner(lang, "002.jpg", "ApitoxCosmetics", t['name'], t['tag'])}
<section class="content paper"><div class="wrap"><div class="pd">
 <div class="ph"><img src="{b}img/{d['img']}" alt="{t['name']}"></div>
 <div>
  <a class="small" href="prodavnica.html" style="font-weight:700">{L[5]}</a>
  <h2 style="margin-top:10px">{t['name']}</h2>
  <div class="price" data-price="{slug}" style="margin-top:6px"></div>
  <p class="lead">{t['lead']}</p>
  <div class="buy"><div class="qty"><button type="button" data-step="-1">−</button><input id="qty" value="1" inputmode="numeric"><button type="button" data-step="1">+</button></div>
   <button class="btn" data-add="{slug}" data-qty>{L[4]}</button></div>
  <dl><dt>{L[0]}</dt><dd>{t['sastav']}</dd><dt>{L[1]}</dt><dd>{t['upotreba']}</dd><dt>{L[2]}</dt><dd>{t['napomena']}</dd></dl>
  <p class="small">{L[3]}</p>
 </div>
</div></div></section>"""
    ld = jsonld({"@context": "https://schema.org", "@type": "Product", "name": t["name"],
                 "image": f"{SITE}/img/{d['img']}", "description": t["lead"],
                 "brand": {"@type": "Brand", "name": "ApitoxCosmetics"},
                 "manufacturer": {"@type": "Organization", "name": "Pčelarstvo Stanojević"}})
    desc = (t["lead"][:155].rsplit(" ", 1)[0] + "…") if len(t["lead"]) > 155 else t["lead"]
    return page(lang, slug, t["name"], desc, body, current="prodavnica", ld=ld, image=d["img"])


# ================================================================ APITOX
def apitox(lang):
    F = lambda i, c="": fig(lang, i, c)
    if lang == "sr":
        bn = banner(lang, "010.jpg", "Apitox sakupljač", "Apitox sakupljač", "Nagrađeni uređaj za sakupljanje pčelinjeg otrova, razvijen u našoj radionici.")
        toc = [("prica", "Naša priča"), ("princip", "Princip rada"), ("tehnologija", "Tehnologija"),
               ("kolektor", "Naš kolektor"), ("tehnika", "Tehnika sakupljanja"), ("slike", "Slike")]
        award = ("Nagrada", "Prvo mesto na državnom sajmu pčelarstva za najbolju inovaciju",
                 "Apitox sakupljač je proglašen najboljom inovacijom na državnom sajmu pčelarstva.")
        stats = [("2013.", "prvi model uređaja"), ("5–12 g", "otrova dnevno"), ("45 min", "automatski rad")]
        order = ("Zainteresovani ste za sakupljač?", "Pozovite nas za ponudu ili dodajte sakupljač u korpu – javićemo vam se.", "Dodaj u korpu")
        S = f"""
<h2 id="prica">Naša priča</h2>
<p>Otkako je počeo da gaji pčele, Goran Stanojević nikada nije pčelario samo „na med“. Na samom početku shvatio je da isplativost pčelarenja zavisi i od sakupljanja polena i propolisa, pravljenja rojeva za tržište… Ako tome dodamo sve lošije i neizvesnije pašne prilike iz godine u godinu, ovakav način razmišljanja dobija na značaju.</p>
{F("012.jpg")}
<p>I kod sakupljanja pčelinjeg otrova Goran je razmišljao drugačije od ostalih pčelara. Mnogi su ga pitali kako može da računa na siguran plasman pčelinjeg otrova ako u našoj državi ne postoji zakonska regulativa vezana za ovaj proizvod, a samim tim ni organizovan otkup, niti tržište za pčelinji otrov. Njegov odgovor bio je da je ključna promena našeg načina razmišljanja o tržištu uopšte – da se moramo ugledati na to kako funkcioniše zapadno tržište, odnosno da sa gotovim proizvodom krenemo u potragu za kupcem.</p>
<p>To ima smisla, jer se pčelinji otrov uz adekvatno čuvanje može skladištiti i nekoliko godina, a da ne izgubi na kvalitetu. Verujemo da će se, uz naše angažovanje, nešto promeniti i kod nas.</p>

<h2 id="princip">Princip rada</h2>
<p>Princip rada elektrostimulatora svodi se na proizvodnju pulsirajućeg električnog signala određene frekvencije i amplitude (frekvencija impulsa 50–1000 Hz, napon 11–42 V), grupisanog u klastere određenog trajanja (impuls 2–3 sekunde), između kojih je pauza bez signala (3–6 sekundi). Promenu ovih parametara omogućavaju mikročipovi na ploči elektrostimulatora.</p>
<p>Kolektorski okvir se u većini konstrukcija postavlja izvan košnice – na leto – i može biti različitih veličina. Pčele prilikom sletanja na ploču dodiruju žičanu mrežu i zatvaraju strujni krug, pa dolazi do elektrostimulacije. Tada savijaju zadak prema ploči i pri dodiru žaoke sa pločom ispuštaju otrov na nju.</p>
{F("013.jpg")}

<h2 id="tehnologija">Tehnologija</h2>
<p>U svim sferama ljudske delatnosti tehnologija svakim danom postaje sve razvijenija i složenija, pa tako i tehnologija dobijanja pčelinjeg otrova. Osnovni princip, međutim, ostao je isti: pčelinji otrov dobijamo elektrostimulacijom, odnosno blagim elektrošokovima. To nije jedini način dobijanja otrova od pčela, ali je daleko efikasniji i jednostavniji od ostalih. Takođe, sa aspekta očuvanja zdravlja, kvaliteta i kvantiteta pčelinje zajednice, ovaj način je najmanje štetan, gotovo bezopasan. Podrazumeva se da se i prilikom sakupljanja pčelinjeg otrova moramo pridržavati pravila dobre pčelarske prakse – tada negativnih posledica po pčelinja društva i pčele kao jedinke sigurno neće biti.</p>
<p>Na tržištu se trenutno mogu pronaći uređaji koje serijski proizvode pojedinci, uglavnom pčelari, ili uređaji kineske proizvodnje. Na prvi pogled svi su slični i ponavljaju sličan patent uveden sredinom sedamdesetih godina prošlog veka. Većina se sastoji od izvora struje (akumulator ili baterija), elektrostimulatora (regulacija struje, napona, frekvencije…) i kolektorskih okvira (sa žičanom mrežom i staklenim pločama).</p>
<div class="pair">{F("015.jpg")}{F("016.jpg")}</div>
<p>Važno je napomenuti da, pored različitog dizajna, sakupljači pčelinjeg otrova imaju i velike razlike u elektronskim parametrima. Najveća razlika je u sistemu upravljanja (ručni ili automatski), u kontroli frekvencije i amplitude izlaznog signala, kao i u dužini rada uređaja. Razlike postoje i u pomoćnim elementima – svetlosnim i zvučnim indikatorima rada i pojedinih faza rada uređaja.</p>

<h2 id="kolektor">Naš kolektor</h2>
{F("019.jpg")}
<p>Mnogo vremena i truda bilo je potrebno da Goran izradi sopstveni uređaj za sakupljanje pčelinjeg otrova. Pomogla su mu saznanja sa interneta i iz literature, kao i poznavanje elektronike, koja mu je struka. Ideja vodilja bila je doći do optimalnih elektronskih parametara, a to je bilo moguće samo izradom više modela i testiranjem svakog od njih. Posle mnogo proba i neuspeha, Goran je 2013. godine došao do uređaja koji vam predstavljamo, a koji je danas usavršen i nadograđen iskustvom.</p>
<p>Uređaj radi na baterije napona 4,5 V, smeštene u kućištu elektrostimulatora, što je svakako praktičnije od automobilskog akumulatora. Mnogo dana provedenih u radionici i na pčelinjaku iznedrilo je najbolje rešenje: elektronske komponente ugrađene u elektrostimulator omogućavaju rad sa naizmeničnim naponom od 23 V do 30 V i frekvencijom oscilatora 700–1000 Hz, pri čemu impuls traje 3 sekunde, a pauza isto toliko. Ove karakteristike su se u praksi pokazale kao najbolje.</p>
<p>Što se tiče žica na kolektorskoj ploči, nije bilo dileme. Već nakon prvih testiranja odbačena je inoks žica, jer je bolje rezultate pokazala posrebrena žica – ona je bolji provodnik, otporna je na hemijsko dejstvo otrova, a srebro ima i antiseptička svojstva (manja verovatnoća prenošenja bolesti na pčelinjaku). Razmak između žica na kolektorskoj ploči iznosi 4,2 mm, što se kroz testiranja pokazalo kao najbolje.</p>
<p>Debljina stakla na kolektorskoj ploči je 3 mm, a staklo je sa donje strane presvučeno folijom u boji, da bi otrov bio lakše uočljiv prilikom struganja.</p>

<h2 id="tehnika">Tehnika sakupljanja pčelinjeg otrova</h2>
<p>Sa sakupljanjem pčelinjeg otrova počinjemo u drugoj polovini aprila, ili čak malo ranije, ali samo ako su zajednice dovoljno jake – ako imaju 6 ramova legla u DB košnicama, odnosno 8 ramova legla u LR.</p>
<p>Sve počinje postavljanjem kolektorskih ploča na poletaljke košnica. Ploča je debela 15 mm i duga 360 mm, što omogućava vađenje regulatora leta i postavljanje kolektorske ploče na njegovo mesto (sa bočnih strana fiksira se drvenim konusnim klinovima). Na podnjačama gde je regulator leta fiksiran, ploče se postavljaju uz pomoć plastičnih štipaljki. Razlika između unutrašnje mere košnice (372 mm) i kolektorske ploče (360 mm) podeljena je na po 6 mm sa obe strane, radi nesmetanog prolaska trutova.</p>
<div class="pair">{F("021.jpg", "Elektronika")}{F("022.jpg", "Kolektorske ploče")}</div>
<p>Uređaj je programiran da se posle 45 minuta sam isključi, a ponekad ga možemo isključiti i ranije, ako primetimo da se smanjio broj pčela na sakupljaču. Zatim ploče premeštamo na druge košnice, i tek posle drugog ili trećeg „tretmana“ menjamo staklene ploče i nastavljamo sa još jednim „tretmanom“.</p>
<p>Najbolje rezultate imamo u jutarnjim časovima, kada su pčele najaktivnije. Tokom dana uradimo 4 „tretmana“ na po 10 košnica odjednom. Prosečna količina pčelinjeg otrova koju na ovaj način dnevno sakupimo iznosi između 5 i 12 grama. Po košnici, odnosno po jednom tretmanu jedne košnice, količina sakupljenog otrova kreće se od 0,1 g do 0,3 g, u zavisnosti od jačine društva.</p>
"""
        slike_h = "Slike sakupljača"
        desc = "Apitox sakupljač pčelinjeg otrova – princip rada, tehnologija i tehnika sakupljanja. Prvo mesto za najbolju inovaciju."
        title = "Apitox sakupljač"
    else:
        bn = banner(lang, "010.jpg", "Apitox collector", "Apitox collector", "An award-winning bee venom collector, developed in our own workshop.")
        toc = [("prica", "Our story"), ("princip", "How it works"), ("tehnologija", "Technology"),
               ("kolektor", "Our collector"), ("tehnika", "Collecting technique"), ("slike", "Photos")]
        award = ("Award", "First place at the national beekeeping fair for best innovation",
                 "The Apitox collector was named the best innovation at the national beekeeping fair.")
        stats = [("2013", "first model"), ("5–12 g", "of venom per day"), ("45 min", "automatic operation")]
        order = ("Interested in the collector?", "Call us for a quote, or add the collector to your cart and we will get in touch.", "Add to cart")
        S = f"""
<h2 id="prica">Our story</h2>
<p>Ever since he started keeping bees, Goran Stanojević has never kept them "just for honey". From the very beginning he understood that beekeeping pays off only if you also collect pollen and propolis, raise swarms for sale… Add the forage conditions that get worse and less predictable every year, and this way of thinking becomes all the more important.</p>
{F("012.jpg")}
<p>Goran thought differently from other beekeepers when it came to bee venom, too. Many asked him how he could count on selling bee venom when our country has no regulations for this product, and therefore no organised buying and no market for it at all. His answer was that the key is to change the way we think about the market – to look at how Western markets work and to go out and find buyers with a finished product.</p>
<p>It makes sense: stored properly, bee venom keeps for several years without losing quality. We believe that, with our effort, things will change here too.</p>

<h2 id="princip">How it works</h2>
<p>The electrostimulator produces a pulsing electrical signal of a set frequency and amplitude (pulse frequency 50–1000 Hz, voltage 11–42 V), grouped into bursts of a set length (2–3 second pulses) separated by pauses with no signal (3–6 seconds). Microchips on the electrostimulator board make it possible to change these parameters.</p>
<p>In most designs the collector frame is placed outside the hive, at the entrance, and can come in different sizes. When bees land on the plate, they touch the wire grid and close the circuit, which stimulates them. They bend their abdomen towards the plate and, as the sting touches it, release venom onto it.</p>
{F("013.jpg")}

<h2 id="tehnologija">Technology</h2>
<p>Technology in every field grows more advanced and complex every day, and venom collection is no exception. The basic principle, however, has stayed the same: we obtain bee venom by electrostimulation, that is, by mild electric pulses. It is not the only way to collect venom, but it is by far the most efficient and the simplest. It is also the least harmful – almost harmless – to the health, quality and strength of the colony. Of course, good beekeeping practice must be followed when collecting venom as well; then there are no negative consequences for the colonies or for individual bees.</p>
<p>The devices available on the market are made in small series by individuals, mostly beekeepers, or manufactured in China. At first glance they are all similar and repeat a similar patent from the mid-1970s. Most consist of a power source (car battery or batteries), an electrostimulator (controlling current, voltage, frequency…) and collector frames (with a wire grid and glass plates).</p>
<div class="pair">{F("015.jpg")}{F("016.jpg")}</div>
<p>Beyond their different designs, venom collectors also differ greatly in their electronic parameters. The biggest differences are in the control system (manual or automatic), in how the frequency and amplitude of the output signal are controlled, and in how long the device runs. They also differ in auxiliary features – light and sound indicators for operation and for individual stages.</p>

<h2 id="kolektor">Our collector</h2>
{F("019.jpg")}
<p>It took Goran a great deal of time and effort to build his own bee venom collector. He drew on information from the internet and the literature, and on his knowledge of electronics, which is his profession. The goal was to find the optimal electronic parameters, and the only way to do that was to build several models and test each one. After many trials and failures, in 2013 Goran arrived at the device we present here, which has since been refined and upgraded with experience.</p>
<p>The device runs on 4.5 V batteries housed in the electrostimulator casing – far more practical than a car battery. Many days in the workshop and at the apiary produced the best solution: the electronic components built into the electrostimulator allow it to work with an alternating voltage of 23–30 V and an oscillator frequency of 700–1000 Hz, with 3-second pulses and equally long pauses. These settings have proven the best in practice.</p>
<p>There was no doubt about the wire on the collector plate. Stainless steel wire was rejected after the first tests, because silver-plated wire performed better: it conducts better, resists the chemical action of the venom, and silver is antiseptic (less chance of spreading disease in the apiary). The spacing between the wires is 4.2 mm, which testing showed to be optimal.</p>
<p>The glass on the collector plate is 3 mm thick and coated underneath with coloured film, so the venom is easier to see when scraping.</p>

<h2 id="tehnika">Collecting technique</h2>
<p>We start collecting bee venom in the second half of April, or slightly earlier, but only once the colonies are strong enough – 6 frames of brood in DB hives, or 8 frames of brood in LR hives.</p>
<p>It all starts by placing the collector plates at the hive entrances. The plate is 15 mm thick and 360 mm long, so the entrance reducer can be removed and the plate put in its place (fixed at the sides with wooden wedges). On bottom boards where the entrance reducer is fixed, the plates are held with plastic clips. The difference between the inside width of the hive (372 mm) and the plate (360 mm) leaves 6 mm on each side so drones can pass freely.</p>
<div class="pair">{F("021.jpg", "Electronics")}{F("022.jpg", "Collector plates")}</div>
<p>The device is programmed to switch off by itself after 45 minutes; sometimes we switch it off earlier if we see fewer bees on the collector. We then move the plates to other hives, and only after the second or third "treatment" do we change the glass plates and continue with another one.</p>
<p>The best results come in the morning, when bees are most active. During the day we do 4 "treatments" on 10 hives at a time. On average we collect between 5 and 12 grams of venom a day this way. Per hive, that is, per treatment of one hive, we collect 0.1 g to 0.3 g, depending on the strength of the colony.</p>
"""
        slike_h = "Collector photos"
        desc = "The Apitox bee venom collector – how it works, technology and collecting technique. First place for best innovation."
        title = "Apitox collector"

    tocs = "".join(f'<a href="#{a}">{n}</a>' for a, n in toc)
    st = "".join(f"<div><b>{v}</b><span>{k}</span></div>" for v, k in stats)
    pics = [f"0{n:02d}.jpg" for n in [25, 26, 27, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]]
    b = "" if lang == "sr" else "../"
    body = f"""{bn}
<section class="content paper"><div class="wrap">
 <div class="toc">{tocs}</div>
 <div class="prose">
  <div class="awardbox"><img src="{b}img/011.jpg" alt=""><div><div class="kick left">{award[0]}</div><h2>{award[1]}</h2><p>{award[2]}</p></div></div>
  <div class="stats">{st}</div>
  {S}
  <h2 id="slike">{slike_h}</h2>
 </div>
 {gal(lang, [(p, "") for p in pics])}
 <div class="prose"><div class="awardbox" style="grid-template-columns:1fr auto"><div><h2>{order[0]}</h2><p>{order[1]}</p></div>
  <div style="display:flex;flex-direction:column;gap:12px"><button class="btn" data-add="apitox-sakupljac">{order[2]}</button><a class="btn ghost" href="tel:{PHONE_INTL}">{PHONE}</a></div></div></div>
</div></section>"""
    return page(lang, "apitox-sakupljac", title, desc, body)


# ================================================================ APIKOMORA
def apikomora(lang):
    F = lambda i, c="": fig(lang, i, c)
    if lang == "sr":
        bn = banner(lang, "041.jpg", "Apiterapija", "Apikomora", "Zdravlje iz košnice – inhalacija i ležanje nad košnicama.")
        stats = [("april – avgust", "sezona tretmana"), ("10–20 min", "inhalacija"), ("30–60 min", "ležanje nad košnicama")]
        S = f"""
<h2>Apikomora – zdravlje iz košnice</h2>
<p>Etarska isparenja propolisa, meda, voska, matičnog mleča i perge, kao i aromatične materije cvetova, nektara i voska koje se oslobađaju iz košnice naseljene pčelama, ispunjavaju vazduh oko pčelinjaka. Boravak u takvom okruženju mnogi doživljavaju kao opuštajući i okrepljujući – bolje spavaju, imaju bolji apetit i raspoloženje. Tretmani u apikomori su noviji pravac u apiterapiji, tradicionalnoj metodi koja koristi pčelinje proizvode.</p>
<p>Apikomora je drvena kućica koja služi za inhalaciju vazduha iz košnice ili za ležanje nad košnicama, pri čemu osobe unutra nemaju direktan kontakt sa pčelama. Obe metode primenjuju se od aprila do polovine avgusta, kada su pčele aktivne. Košnice koje se koriste u ovu svrhu moraju imati jaka i zdrava pčelinja društva, i u periodu inhalacija ne tretiraju se protiv varoe hemijskim sredstvima. Protiv varoe se borimo isključivo prirodnim putem – ramom građevnjakom, a kasnije organskim kiselinama.</p>
<div class="pair">{F("042.jpg")}{F("043.jpg")}</div>
<h2>Inhalacija nad košnicom</h2>
<p>Inhalacija se vrši pomoću posebnih maski priključenih na ventilator, koji se postavlja na otvor na poklopcu košnice. Protok vazduha iz košnice reguliše se potenciometrom. Maske imaju nepovratni ventil, kako se izdahnuti vazduh ne bi vraćao u košnicu.</p>
<p>Mnogi korisnici inhalacije koriste radi jačanja opšte otpornosti organizma – sportisti, deca i starije osobe – a posebno ih biraju oni koji imaju tegobe sa disajnim putevima (nos, sinusi, grlo, bronhije).</p>
<p>Inhalacija traje 10 do 20 minuta, jednom ili dva puta dnevno, a broj i raspored tretmana dogovaramo pojedinačno.</p>
<h2>Ležanje nad košnicama</h2>
<p>Ležanje nad košnicama je druga metoda koja se primenjuje u apikomori. Osoba leži na leđima na drvenom poklopcu ispod kojeg su smeštene košnice, sa nogama savijenim u kolenima i rukama uz telo, dlanovima okrenutim nadole. Tako se osećaju mikrovibracije koje nastaju treperenjem krila pčela i njihovim radom u košnici – svojevrsna vibraciona masaža. Monotono zujanje pčela deluje kao vrsta „meditacije“: opušta i smiruje. Smatra se i da pčele u košnici jonizuju vazduh.</p>
<p>Ležanje traje od 30 minuta do sat vremena. Posebno ga cene osobe pod stresom, sa hroničnim umorom i problemima sa snom.</p>
{F("044.jpg")}
<h2>Važne napomene</h2>
<ul>
<li>Ako se tokom inhalacije jave otežano disanje ili uznemirenost, inhalaciju odmah prekinuti.</li>
<li>Inhalacija i ležanje ne preporučuju se osobama koje boluju od epilepsije, tuberkuloze, malignih i akutnih zaraznih bolesti, osobama sa povišenom telesnom temperaturom, alergijom na pčelinje proizvode i cističnom fibrozom.</li>
<li>Ležanje se ne preporučuje trudnicama; oprez je potreban kod osoba sa kamenom u bubregu ili žuči.</li>
<li>Inhalacija se ne preporučuje deci mlađoj od 3 godine.</li>
<li>Osobe sa hroničnim bolestima treba da se pre tretmana posavetuju sa lekarom.</li>
<li>U apikomoru se ne ulazi sa mobilnim telefonom, namirisan parfemom ili dezodoransom, niti u alkoholisanom stanju, jer to ometa normalan rad pčelinje zajednice.</li>
</ul>
<p class="note">Boravak u apikomori nije zamena za lečenje i terapiju koju je propisao lekar.</p>
<h2>Posete apikomori</h2>"""
        caps = [("045.jpg", "Poseta đaka i profesora OŠ „Olga Milošević“"), ("046.jpg", "Poseta studenata i profesora iz Holandije"),
                ("047.jpg", "Poseta kolega pčelara iz Slovenije"), ("048.jpg", "Poseta kolega pčelara iz Slovenije")]
        cta = ("Zakažite termin", "Termine u apikomori dogovaramo telefonom.")
        desc = "Apikomora u Smederevskoj Palanci – inhalacija vazduhom iz košnice i ležanje nad košnicama, od aprila do avgusta. Zakažite termin: 064 128 5796."
        title = "Apikomora"
    else:
        bn = banner(lang, "041.jpg", "Apitherapy", "Api-chamber", "Health from the hive – breathing hive air and lying above the hives.")
        stats = [("April – August", "session season"), ("10–20 min", "breathing hive air"), ("30–60 min", "lying above the hives")]
        S = f"""
<h2>Api-chamber – health from the hive</h2>
<p>The aromatic vapours of propolis, honey, wax, royal jelly and bee bread, together with the scents of flowers, nectar and wax released from a hive full of bees, fill the air around the apiary. Many people find time spent in this environment relaxing and refreshing – they sleep better and their appetite and mood improve. Api-chamber sessions are a newer branch of apitherapy, a traditional practice that uses bee products.</p>
<p>The api-chamber is a small wooden house used for breathing air from the hive or for lying above the hives, with no direct contact with the bees. Both are offered from April to mid-August, when the bees are active. The hives used for this must hold strong, healthy colonies, and they are not treated against varroa with chemicals while sessions are running. We fight varroa only by natural means – with a drone comb frame, and later with organic acids.</p>
<div class="pair">{F("042.jpg")}{F("043.jpg")}</div>
<h2>Breathing hive air</h2>
<p>Hive air is inhaled through special masks connected to a fan placed over an opening in the hive lid. A dial controls how much air flows from the hive. The masks have a one-way valve so that exhaled air does not go back into the hive.</p>
<p>Many visitors use these sessions to strengthen their general resilience – athletes, children and older people – and they are especially popular with people who have trouble with their airways (nose, sinuses, throat, bronchi).</p>
<p>A session lasts 10 to 20 minutes, once or twice a day; the number and schedule of sessions are arranged individually.</p>
<h2>Lying above the hives</h2>
<p>Lying above the hives is the second method offered in the api-chamber. You lie on your back on a wooden lid with the hives underneath, knees bent, arms by your sides, palms down. You feel the micro-vibrations made by the bees' wings and their work in the hive – a kind of vibration massage. The steady hum of the bees works like a form of "meditation": it relaxes and calms. Bees in the hive are also believed to ionise the air.</p>
<p>A session lasts from 30 minutes to an hour. It is especially appreciated by people under stress, with chronic fatigue or sleep problems.</p>
{F("044.jpg")}
<h2>Important notes</h2>
<ul>
<li>If breathing becomes difficult or you feel agitated during a session, stop immediately.</li>
<li>Sessions are not recommended for people with epilepsy, tuberculosis, cancer or acute infectious diseases, a fever, an allergy to bee products, or cystic fibrosis.</li>
<li>Lying above the hives is not recommended during pregnancy; people with kidney or gall stones should be careful.</li>
<li>Breathing hive air is not recommended for children under 3.</li>
<li>People with chronic illnesses should consult their doctor before a session.</li>
<li>Do not enter the api-chamber with a mobile phone, wearing perfume or deodorant, or after drinking alcohol, as this disturbs the bee colony.</li>
</ul>
<p class="note">Time in the api-chamber is not a substitute for medical treatment prescribed by a doctor.</p>
<h2>Visits to the api-chamber</h2>"""
        caps = [("045.jpg", "Visit by pupils and teachers of “Olga Milošević” Primary School"), ("046.jpg", "Visit by students and professors from the Netherlands"),
                ("047.jpg", "Visit by fellow beekeepers from Slovenia"), ("048.jpg", "Visit by fellow beekeepers from Slovenia")]
        cta = ("Book a session", "Api-chamber sessions are booked by phone.")
        desc = "The Stanojević api-chamber – breathing hive air and lying above the hives, April to August."
        title = "Api-chamber"
    st = "".join(f"<div><b>{v}</b><span>{k}</span></div>" for v, k in stats)
    body = f"""{bn}
<section class="content paper"><div class="wrap">
 <div class="prose"><div class="stats">{st}</div>{S}</div>
 {gal(lang, caps)}
 <div class="prose"><div class="awardbox" style="grid-template-columns:1fr auto"><div><h2>{cta[0]}</h2><p>{cta[1]}</p></div>
  <a class="btn" href="tel:{PHONE_INTL}">{PHONE}</a></div></div>
</div></section>"""
    return page(lang, "apikomora", title, desc, body)


# ================================================================ GALLERY
def galerija(lang):
    if lang == "sr":
        bn = banner(lang, "053.jpg", "Galerija", "Galerija", "Naši pčelinjaci, apikomora, posete i druženja.")
        groups = [
            ("Naši pčelinjaci", [("051.jpg", ""), ("052.jpg", ""), ("053.jpg", ""), ("054.jpg", ""), ("055.jpg", ""), ("056.jpg", "")]),
            ("Apikomora", [("042.jpg", ""), ("043.jpg", ""), ("044.jpg", ""), ("041.jpg", "")]),
            ("Posete", [("045.jpg", "Poseta đaka i profesora OŠ „Olga Milošević“"), ("046.jpg", "Poseta studenata i profesora iz Holandije"),
                        ("047.jpg", "Poseta kolega pčelara iz Slovenije"), ("048.jpg", "Poseta kolega pčelara iz Slovenije")]),
            ("Druženja", [("057.jpg", "Sa Veroljubom Umeljićem"), ("058.jpg", "Sa Boštjanom Nočem"), ("059.jpg", "Sa Janošem Balintom"),
                          ("060.jpg", "Sa Milutinom Batom Petrovićem"), ("061.jpg", "Poseta Novozelanđana u Austriji"),
                          ("062.jpg", "Predavanje u Grčkoj"), ("063.jpg", "Sajam u Celju 2019."), ("064.jpg", "Sajam u Celju 2019., sa Andrejem Severom")]),
        ]
        desc = "Galerija Pčelarstva Stanojević – pčelinjaci, apikomora, posete i druženja sa pčelarima."
        title = "Galerija"
    else:
        bn = banner(lang, "053.jpg", "Gallery", "Gallery", "Our apiaries, the api-chamber, visits and meetings.")
        groups = [
            ("Our apiaries", [("051.jpg", ""), ("052.jpg", ""), ("053.jpg", ""), ("054.jpg", ""), ("055.jpg", ""), ("056.jpg", "")]),
            ("Api-chamber", [("042.jpg", ""), ("043.jpg", ""), ("044.jpg", ""), ("041.jpg", "")]),
            ("Visits", [("045.jpg", "Visit by pupils and teachers of “Olga Milošević” Primary School"), ("046.jpg", "Visit by students and professors from the Netherlands"),
                        ("047.jpg", "Visit by fellow beekeepers from Slovenia"), ("048.jpg", "Visit by fellow beekeepers from Slovenia")]),
            ("Meetings", [("057.jpg", "With Veroljub Umeljić"), ("058.jpg", "With Boštjan Noč"), ("059.jpg", "With János Bálint"),
                          ("060.jpg", "With Milutin Bata Petrović"), ("061.jpg", "Visit by New Zealanders in Austria"),
                          ("062.jpg", "Lecture in Greece"), ("063.jpg", "Celje fair 2019"), ("064.jpg", "Celje fair 2019, with Andrej Sever")]),
        ]
        desc = "Stanojević Beekeeping gallery – apiaries, the api-chamber, visits and meetings with beekeepers."
        title = "Gallery"
    secs = "".join(f'<h2 class="galtitle">{h}</h2>{gal(lang, items)}' for h, items in groups)
    body = f'{bn}<section class="content paper"><div class="wrap">{secs}</div></section>'
    return page(lang, "galerija", title, desc, body)


# ================================================================ CONTACT
def kontakt(lang):
    if lang == "sr":
        bn = banner(lang, "054.jpg", "Kontakt", "Kontakt", "Pozovite nas ili pišite – rado ćemo odgovoriti.")
        L = ("Telefon", "E-pošta", "Viber / WhatsApp", "Mesto")
        desc = "Kontakt Pčelarstva Stanojević – Goran Stanojević, 064 128 5796, goxyst@mts.rs."
        title = "Kontakt"
    else:
        bn = banner(lang, "054.jpg", "Contact", "Contact", "Call or write to us – we will be happy to answer.")
        L = ("Phone", "Email", "Viber / WhatsApp", "Location")
        desc = "Contact Stanojević Beekeeping – Goran Stanojević, +381 64 128 5796, goxyst@mts.rs."
        title = "Contact"
    body = f"""{bn}
<section class="content paper"><div class="wrap">
 <div class="cgrid">
  <a class="cc" href="tel:{PHONE_INTL}">{hexi('phone')}{L[0]}<b>{PHONE}</b></a>
  <a class="cc" href="mailto:{EMAIL}">{hexi('mail')}{L[1]}<b>{EMAIL}</b></a>
  <a class="cc" href="https://wa.me/{PHONE_INTL[1:]}">{hexi('chat')}{L[2]}<b>{PHONE}</b></a>
  <a class="cc" href="https://maps.google.com/?q=Smederevska+Palanka" target="_blank" rel="noopener">{hexi('pin')}{L[3]}<b>{PLACE[lang]}</b></a>
 </div>
 <p style="text-align:center;margin-top:40px;font:italic 500 22px Lora,serif">Goran Stanojević</p>
</div></section>"""
    return page(lang, "kontakt", title, desc, body)


# ================================================================ CART / CHECKOUT
def korpa(lang):
    if lang == "sr":
        bn = banner(lang, "049.jpg", "Porudžbina", "Korpa", "Bez plaćanja na sajtu – pozvaćemo vas da potvrdimo porudžbinu.")
        L = dict(cart="Vaša korpa", data="Podaci za dostavu", name="Ime i prezime", phone="Telefon", email="E-pošta (nije obavezno)",
                 addr="Adresa", city="Mesto i poštanski broj", note="Napomena", send="Pošalji porudžbinu",
                 fine="Plaćanje pouzećem. Nakon slanja porudžbine pozvaćemo vas na navedeni broj radi potvrde, cene dostave i roka isporuke.",
                 wa="Ili pošaljite porudžbinu preko WhatsApp-a",
                 done_h="Hvala vam!", done_p="Primili smo vašu porudžbinu. Pozvaćemo vas uskoro radi potvrde.", back="Nazad na početnu")
        title = "Korpa"
        desc = "Korpa i porudžbina – Pčelarstvo Stanojević."
    else:
        bn = banner(lang, "049.jpg", "Order", "Cart", "No payment on the site – we will call you to confirm your order.")
        L = dict(cart="Your cart", data="Delivery details", name="Full name", phone="Phone", email="Email (optional)",
                 addr="Address", city="Town and postcode", note="Note", send="Send order",
                 fine="Cash on delivery. After you send the order, we will call you to confirm it and agree on delivery cost and time.",
                 wa="Or send your order via WhatsApp",
                 done_h="Thank you!", done_p="We have received your order. We will call you soon to confirm it.", back="Back to home")
        title = "Cart"
        desc = "Cart and order – Stanojević Beekeeping."
    body = f"""{bn}
<section class="content paper"><div class="wrap">
 <div class="box done hidden" id="done">{hexi('check')}<h2>{L['done_h']}</h2><p>{L['done_p']}</p><br><a class="btn arrow" href="index.html">{L['back']}</a></div>
 <div class="co" id="checkout">
  <div class="box"><h2>{L['cart']}</h2><div id="cart-lines"></div><div id="cart-total"></div></div>
  <form class="box" id="order" name="porudzbina" method="POST" data-netlify="true" netlify-honeypot="bot-field">
   <h2>{L['data']}</h2>
   <input type="hidden" name="form-name" value="porudzbina">
   <p class="hidden"><label>Ne popunjavati <input name="bot-field"></label></p>
   <textarea class="hidden" name="porudzbina" aria-hidden="true"></textarea>
   <input type="hidden" name="jezik">
   <label for="f-ime">{L['name']}</label><input id="f-ime" name="ime" required autocomplete="name">
   <div class="two">
    <div><label for="f-tel">{L['phone']}</label><input id="f-tel" name="telefon" type="tel" required autocomplete="tel"></div>
    <div><label for="f-mail">{L['email']}</label><input id="f-mail" name="email" type="email" autocomplete="email"></div>
   </div>
   <label for="f-adr">{L['addr']}</label><input id="f-adr" name="adresa" required autocomplete="street-address">
   <label for="f-grad">{L['city']}</label><input id="f-grad" name="mesto" required autocomplete="address-level2">
   <label for="f-nap">{L['note']}</label><textarea id="f-nap" name="napomena"></textarea>
   <br><br><button class="btn" type="submit" style="width:100%;justify-content:center">{L['send']}</button>
   <p class="small">{L['fine']}</p>
   <a class="wa" id="wa" href="#" target="_blank" rel="noopener">{IC['chat'].replace('<svg', '<svg width="20" height="20" stroke="currentColor" fill="none" stroke-width="2"')}{L['wa']}</a>
  </form>
 </div>
</div></section>"""
    return page(lang, "korpa", title, desc, body, current="prodavnica")


# ================================================================ BUILD
def main():
    pages = {"index": home, "prodavnica": shop, "apitox-sakupljac": apitox, "apikomora": apikomora,
             "galerija": galerija, "kontakt": kontakt, "korpa": korpa}
    for lang in ("sr", "en"):
        out = ROOT if lang == "sr" else os.path.join(ROOT, "en")
        os.makedirs(out, exist_ok=True)
        for slug, fn in pages.items():
            open(os.path.join(out, slug + ".html"), "w", encoding="utf-8").write(fn(lang))
        for slug in CREAMS:
            open(os.path.join(out, slug + ".html"), "w", encoding="utf-8").write(cream(lang, slug))
    slugs = ["index", "prodavnica", "apifigura", "apisalus", "propolis-krema",
             "apitox-sakupljac", "apikomora", "galerija", "kontakt"]
    sm = ['<?xml version="1.0" encoding="UTF-8"?>',
          '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for lang in ("sr", "en"):
        for sl in slugs:
            sm.append(f"<url><loc>{url(lang, sl)}</loc>"
                      f'<xhtml:link rel="alternate" hreflang="sr" href="{url("sr", sl)}"/>'
                      f'<xhtml:link rel="alternate" hreflang="en" href="{url("en", sl)}"/></url>')
    sm.append("</urlset>")
    open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8").write("\n".join(sm) + "\n")
    open(os.path.join(ROOT, "robots.txt"), "w").write(f"User-agent: *\nDisallow: /korpa.html\nDisallow: /en/korpa.html\n\nSitemap: {SITE}/sitemap.xml\n")
    # old Google Sites addresses -> new pages (keeps existing Google ranking)
    from urllib.parse import quote
    old = [("/početna", "/"), ("/apitoxcosmetics", "/prodavnica.html"), ("/ostali-proizvodi", "/prodavnica.html"),
           ("/apitox-sakupljači", "/apitox-sakupljac.html"),
           ("/apitox-sakupljači/tehnologija", "/apitox-sakupljac.html#tehnologija"),
           ("/apitox-sakupljači/tehnologija/kolektor-u-izradi-gorana-stanojevića", "/apitox-sakupljac.html#kolektor"),
           ("/apitox-sakupljači/tehnika-skupljanja", "/apitox-sakupljac.html#tehnika"),
           ("/apitox-sakupljači/princip-rada", "/apitox-sakupljac.html#princip"),
           ("/apitox-sakupljači/slike-sakupljača", "/apitox-sakupljac.html#slike"),
           ("/api-komora", "/apikomora.html"), ("/galerija", "/galerija.html"),
           ("/apifigura", "/apifigura.html"), ("/apisalus", "/apisalus.html"), ("/propolis-krema", "/propolis-krema.html")]
    lines = []
    for a, b in old:
        lines.append(f"{quote(a)}  {b}  301")
        if quote(a) != a:
            lines.append(f"{a}  {b}  301")
    open(os.path.join(ROOT, "_redirects"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    print("OK")


if __name__ == "__main__":
    main()
