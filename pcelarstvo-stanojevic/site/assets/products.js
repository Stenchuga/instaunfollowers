/*
  SPISAK PROIZVODA / PRODUCT LIST
  ---------------------------------
  Ovde se menjaju proizvodi i cene. Za svaki proizvod:
    id      – kratka oznaka bez razmaka (ne menjati posle objavljivanja)
    cat     – kategorija: "kozmetika", "med", "pcelinji", "oprema"
    price   – cena u dinarima (samo broj, npr. 1200). Ako stoji null, piše "Cena na upit".
    unit    – pakovanje (npr. "50 ml", "1 kg")
    img     – slika iz foldera img/
    cover   – true ako je slika fotografija koja treba da ispuni okvir
    page    – stranica sa detaljima (ako postoji)
    sr / en – naziv i kratak opis na srpskom i engleskom

  PRIMER: price: 1500  →  prikazuje se "1.500 din"
*/
window.PRODUCTS = [
  { id: "apifigura", cat: "kozmetika", price: null, unit: "", img: "img/proizvodi/apifigura.webp", page: "apifigura",
    sr: { name: "ApiFigura", desc: "Antirid krema sa pčelinjim otrovom i matičnim mlečom" },
    en: { name: "ApiFigura", desc: "Anti-wrinkle cream with bee venom and royal jelly" } },
  { id: "apisalus", cat: "kozmetika", price: null, unit: "", img: "img/005.png", page: "apisalus",
    sr: { name: "ApiSalus", desc: "Krema sa pčelinjim otrovom – pčelinje zdravlje" },
    en: { name: "ApiSalus", desc: "Cream with bee venom – bee health" } },
  { id: "propolis-krema", cat: "kozmetika", price: null, unit: "", img: "img/006.png", page: "propolis-krema",
    sr: { name: "ProPolis krema", desc: "Mast na bazi propolisa i prirodnih ulja" },
    en: { name: "ProPolis cream", desc: "Ointment made with propolis and natural oils" } },

  /* --- PRIMERI: dopuniti tačnim proizvodima, pakovanjima i cenama --- */
  { id: "med", cat: "med", price: null, unit: "", img: "img/049.jpg", cover: true,
    sr: { name: "Med", desc: "Med sa našeg pčelinjaka" },
    en: { name: "Honey", desc: "Honey from our apiary" } },
  { id: "polen", cat: "pcelinji", price: null, unit: "", img: "img/049.jpg", cover: true,
    sr: { name: "Polen", desc: "Cvetni prah" },
    en: { name: "Bee pollen", desc: "Flower pollen" } },
  { id: "propolis", cat: "pcelinji", price: null, unit: "", img: "img/049.jpg", cover: true,
    sr: { name: "Propolis", desc: "Propolis sa našeg pčelinjaka" },
    en: { name: "Propolis", desc: "Propolis from our apiary" } },
  { id: "maticni-mlec", cat: "pcelinji", price: null, unit: "", img: "img/049.jpg", cover: true,
    sr: { name: "Matični mleč", desc: "Svež matični mleč" },
    en: { name: "Royal jelly", desc: "Fresh royal jelly" } },
  { id: "apitox-sakupljac", cat: "oprema", price: null, unit: "", img: "img/017.jpg", cover: true, page: "apitox-sakupljac",
    sr: { name: "Apitox sakupljač", desc: "Uređaj za sakupljanje pčelinjeg otrova" },
    en: { name: "Apitox collector", desc: "Bee venom collecting device" } }
];

/* Kontakt za porudžbine / Order contact */
window.SHOP = {
  phone: "+381641285796",       // za WhatsApp i poziv
  phoneLabel: "064 128 5796",
  email: "goxyst@mts.rs"
};
