(function () {
  var lang = document.documentElement.lang === "en" ? "en" : "sr";
  var base = document.body.getAttribute("data-base") || "";
  var P = window.PRODUCTS || [];
  var S = window.SHOP || {};

  var T = {
    sr: { onRequest: "Cena na upit", add: "Dodaj u korpu", added: "Dodato ✓", toast: "Dodato u korpu", more: "Detaljnije",
      all: "Sve", cats: { kozmetika: "Kozmetika", med: "Med", pcelinji: "Pčelinji proizvodi", oprema: "Sakupljači" },
      empty: "Korpa je prazna.", toShop: "Idi u prodavnicu", total: "Ukupno", plusReq: "+ stavke sa cenom na upit",
      remove: "Ukloni", sending: "Šaljem…", fail: "Porudžbina nije poslata. Pozovite nas na " ,
      waText: "Zdravo, želim da poručim:", currency: "din" },
    en: { onRequest: "Price on request", add: "Add to cart", added: "Added ✓", toast: "Added to cart", more: "Details",
      all: "All", cats: { kozmetika: "Cosmetics", med: "Honey", pcelinji: "Bee products", oprema: "Collectors" },
      empty: "Your cart is empty.", toShop: "Go to shop", total: "Total", plusReq: "+ items with price on request",
      remove: "Remove", sending: "Sending…", fail: "The order was not sent. Please call us at ",
      waText: "Hello, I would like to order:", currency: "RSD" }
  }[lang];

  function byId(id) { for (var i = 0; i < P.length; i++) if (P[i].id === id) return P[i]; }
  function fmt(p) { return p.price != null ? p.price.toLocaleString("sr-RS") + " " + T.currency : (p.priceEur != null ? p.priceEur.toLocaleString("sr-RS") + " €" : T.onRequest); }
  function totalText(s, cur) {
    var parts = [];
    if (s.sum > 0) parts.push(s.sum.toLocaleString("sr-RS") + " " + cur);
    if (s.eur > 0) parts.push(s.eur.toLocaleString("sr-RS") + " €");
    return parts.length ? parts.join(" + ") : null;
  }
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  /* ---- cart storage ---- */
  var mem = {};
  function load() { try { return JSON.parse(localStorage.getItem("ps_cart") || "{}"); } catch (e) { return mem; } }
  function save(c) { mem = c; try { localStorage.setItem("ps_cart", JSON.stringify(c)); } catch (e) {} updateCount(); }
  function addToCart(id, q) { var c = load(); c[id] = (c[id] || 0) + (q || 1); save(c); toast(T.toast); }
  function updateCount() {
    var c = load(), n = 0; for (var k in c) if (byId(k)) n += c[k];
    var els = document.querySelectorAll(".cartbtn .n"); for (var i = 0; i < els.length; i++) els[i].textContent = n;
  }

  var toastEl;
  function toast(msg) {
    if (!toastEl) { toastEl = document.createElement("div"); toastEl.className = "toast"; document.body.appendChild(toastEl); }
    toastEl.textContent = msg; toastEl.classList.add("show");
    clearTimeout(toastEl._t); toastEl._t = setTimeout(function () { toastEl.classList.remove("show"); }, 1800);
  }

  /* ---- shop grid ---- */
  function cardHtml(p) {
    var t = p[lang];
    var link = p.page ? p.page + ".html" : null;
    return '<article class="card" data-cat="' + p.cat + '">' +
      '<div class="im' + (p.light ? " light" : "") + '"><img src="' + base + p.img + '" alt="' + esc(t.name) + '" class="' + (p.cover ? "cover" : "") + '" loading="lazy"></div>' +
      '<h3>' + esc(t.name) + '</h3><p>' + esc(t.desc) + (p.unit ? " · " + esc(p.unit) : "") + '</p>' +
      (link ? '<a class="more" href="' + link + '">' + T.more + ' →</a>' : "") +
      '<div class="f2"><span class="price' + (p.price == null && p.priceEur == null ? " req" : "") + '">' + fmt(p) + '</span><button class="add" data-add="' + p.id + '">' + T.add + '</button></div></article>';
  }
  function renderShop() {
    var grid = document.getElementById("shop-grid"); if (!grid) return;
    var chips = document.getElementById("chips");
    var cats = []; P.forEach(function (p) { if (cats.indexOf(p.cat) < 0) cats.push(p.cat); });
    chips.innerHTML = '<button class="on" data-cat="">' + T.all + '</button>' +
      cats.map(function (c) { return '<button data-cat="' + c + '">' + (T.cats[c] || c) + '</button>'; }).join("");
    grid.innerHTML = P.map(cardHtml).join("");
    chips.addEventListener("click", function (e) {
      var b = e.target.closest("button"); if (!b) return;
      [].forEach.call(chips.children, function (x) { x.classList.toggle("on", x === b); });
      [].forEach.call(grid.children, function (card) { card.classList.toggle("hidden", !!b.dataset.cat && card.dataset.cat !== b.dataset.cat); });
    });
  }

  /* ---- product price on detail pages ---- */
  function renderDetail() {
    var el = document.querySelector("[data-price]"); if (!el) return;
    var p = byId(el.getAttribute("data-price")); if (p) el.textContent = fmt(p) + (p.unit ? " · " + p.unit : "");
  }

  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-add]"); if (!b) return;
    var q = 1, qi = document.getElementById("qty"); if (qi && b.hasAttribute("data-qty")) q = Math.max(1, parseInt(qi.value, 10) || 1);
    addToCart(b.getAttribute("data-add"), q);
    var old = b.textContent; b.textContent = T.added; b.classList.add("ok");
    setTimeout(function () { b.textContent = old; b.classList.remove("ok"); }, 1400);
  });
  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-step]"); if (!b) return;
    var qi = document.getElementById("qty"); qi.value = Math.max(1, (parseInt(qi.value, 10) || 1) + parseInt(b.dataset.step, 10));
  });

  /* ---- checkout ---- */
  function cartItems() {
    var c = load(), out = [];
    for (var k in c) { var p = byId(k); if (p && c[k] > 0) out.push({ p: p, q: c[k] }); }
    return out;
  }
  function summary(items) {
    var sum = 0, eur = 0, req = false;
    var lines = items.map(function (it) {
      if (it.p.price != null) sum += it.p.price * it.q; else if (it.p.priceEur != null) eur += it.p.priceEur * it.q; else req = true;
      return it.q + " × " + it.p.sr.name + (it.p.unit ? " (" + it.p.unit + ")" : "") + " – " + (it.p.price != null ? (it.p.price * it.q).toLocaleString("sr-RS") + " din" : it.p.priceEur != null ? (it.p.priceEur * it.q).toLocaleString("sr-RS") + " €" : "cena na upit");
    });
    return { lines: lines, sum: sum, eur: eur, req: req };
  }
  function renderCart() {
    var box = document.getElementById("cart-lines"); if (!box) return;
    var items = cartItems(), form = document.getElementById("order");
    if (!items.length) {
      box.innerHTML = '<div class="empty">' + T.empty + '<br><br><a class="btn arrow" href="prodavnica.html">' + T.toShop + '</a></div>';
      document.getElementById("cart-total").innerHTML = "";
      form.querySelector("button[type=submit]").disabled = true;
      return;
    }
    form.querySelector("button[type=submit]").disabled = false;
    box.innerHTML = items.map(function (it) {
      var t = it.p[lang];
      return '<div class="line"><img src="' + base + it.p.img + '" alt=""><div><b>' + esc(t.name) + '</b><br><small>' + fmt(it.p) + '</small></div>' +
        '<div class="qty"><button type="button" data-q="' + it.p.id + '" data-d="-1">−</button><input value="' + it.q + '" readonly><button type="button" data-q="' + it.p.id + '" data-d="1">+</button></div>' +
        '<button class="rm" type="button" title="' + T.remove + '" data-rm="' + it.p.id + '">×</button></div>';
    }).join("");
    var s = summary(items);
    document.getElementById("cart-total").innerHTML = '<div class="tot"><span>' + T.total + '</span><span>' +
      (totalText(s, T.currency) || T.onRequest) + '</span></div>' +
      (s.req && totalText(s, T.currency) ? '<p class="small">' + T.plusReq + '</p>' : "");
    var wa = document.getElementById("wa");
    if (wa) wa.href = "https://wa.me/" + (S.phone || "").replace(/\D/g, "") + "?text=" + encodeURIComponent(T.waText + "\n" + s.lines.join("\n"));
  }
  document.addEventListener("click", function (e) {
    var b = e.target.closest("[data-q],[data-rm]"); if (!b) return;
    var c = load();
    if (b.dataset.rm) delete c[b.dataset.rm];
    else { c[b.dataset.q] = (c[b.dataset.q] || 0) + parseInt(b.dataset.d, 10); if (c[b.dataset.q] < 1) delete c[b.dataset.q]; }
    save(c); renderCart();
  });

  var form = document.getElementById("order");
  if (form) form.addEventListener("submit", function (e) {
    e.preventDefault();
    var items = cartItems(); if (!items.length) return;
    var s = summary(items);
    form.elements["porudzbina"].value = s.lines.join("\n") + "\n\nUkupno: " + ((totalText(s, "din") || "cena na upit") + (s.req && totalText(s, "din") ? " + stavke sa cenom na upit" : ""));
    form.elements["jezik"].value = lang === "en" ? "engleski" : "srpski";
    var btn = form.querySelector("button[type=submit]"), old = btn.textContent;
    btn.disabled = true; btn.textContent = T.sending;
    var body = new URLSearchParams(new FormData(form)).toString();
    fetch("/", { method: "POST", headers: { "Content-Type": "application/x-www-form-urlencoded" }, body: body })
      .then(function (r) { if (!r.ok) throw new Error(r.status); })
      .then(function () { save({}); document.getElementById("checkout").classList.add("hidden"); document.getElementById("done").classList.remove("hidden"); window.scrollTo(0, 0); })
      .catch(function () { btn.disabled = false; btn.textContent = old; alert(T.fail + (S.phoneLabel || "")); });
  });

  /* ---- gallery lightbox ---- */
  var lb, list = [], idx = 0;
  function show(i) { idx = (i + list.length) % list.length; lb.querySelector("img").src = list[idx].href; lb.querySelector("p").textContent = list[idx].getAttribute("data-cap") || ""; }
  document.addEventListener("click", function (e) {
    var a = e.target.closest(".gal a"); if (!a) return; e.preventDefault();
    if (!lb) {
      lb = document.createElement("div"); lb.className = "lb";
      lb.innerHTML = '<img alt=""><p></p><button class="x" aria-label="Zatvori">×</button><button class="pv" aria-label="Prethodna">‹</button><button class="nx" aria-label="Sledeća">›</button>';
      document.body.appendChild(lb);
      lb.addEventListener("click", function (ev) {
        if (ev.target.classList.contains("nx")) show(idx + 1);
        else if (ev.target.classList.contains("pv")) show(idx - 1);
        else if (ev.target.tagName !== "IMG") lb.classList.remove("open");
      });
      document.addEventListener("keydown", function (ev) {
        if (!lb.classList.contains("open")) return;
        if (ev.key === "Escape") lb.classList.remove("open"); if (ev.key === "ArrowRight") show(idx + 1); if (ev.key === "ArrowLeft") show(idx - 1);
      });
    }
    list = [].slice.call(a.closest(".gal").querySelectorAll("a")); show(list.indexOf(a)); lb.classList.add("open");
  });

  /* ---- youtube: load the player only on click ---- */
  document.addEventListener("click", function (e) {
    var a = e.target.closest("a[data-yt]"); if (!a) return; e.preventDefault();
    var f = document.createElement("iframe");
    f.src = "https://www.youtube-nocookie.com/embed/" + a.getAttribute("data-yt") + "?autoplay=1&rel=0";
    f.allow = "autoplay; encrypted-media; picture-in-picture; fullscreen"; f.allowFullscreen = true;
    f.title = a.querySelector("img").alt;
    a.replaceWith(f);
  });

  /* ---- mobile menu ---- */
  var nav = document.querySelector("nav.main");
  document.addEventListener("click", function (e) {
    if (e.target.closest(".burger")) nav.classList.add("open");
    else if (e.target.closest("nav.main .close")) nav.classList.remove("open");
  });

  renderShop(); renderDetail(); renderCart(); updateCount();
})();
