# Pčelarstvo Stanojević – sajt

Statični sajt (HTML/CSS/JS), srpski na `site/`, engleski na `site/en/`.

- **Proizvodi i cene:** `site/assets/products.js` – izmeni cenu (`price`), sačuvaj, objavi.
- **Tekstovi stranica:** `build.py` – posle izmene pokreni `python3 build.py`.
- **Porudžbine:** formular na `korpa.html` koristi Netlify Forms (`data-netlify="true"`).
  Na Netlify-u: Site configuration → Forms → Form notifications → Email → upiši adresu na koju stižu porudžbine.
- **Hosting:** Netlify, publish folder `site` (podešeno u `netlify.toml`).
- Lokalni pregled: `cd site && python3 -m http.server` pa otvori http://localhost:8000
