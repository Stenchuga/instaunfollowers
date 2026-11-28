/*
  SPISAK PROIZVODA / PRODUCT LIST
  ---------------------------------
  Ovde se menjaju proizvodi i cene. Za svaki proizvod:
    id      – kratka oznaka bez razmaka (ne menjati posle objavljivanja)
    cat     – kategorija: "kozmetika", "med", "pcelinji", "oprema"
    price   – cena u dinarima (samo broj, npr. 1200). Ako stoji null, piše "Cena na upit".
    priceEur – cena u evrima (umesto price), npr. za Apitox sakupljač
    unit    – pakovanje (npr. "50 ml", "1 kg")
    img     – slika iz foldera img/
    cover   – true ako je slika fotografija koja treba da ispuni okvir
    light   – true ako je slika na beloj pozadini (prikazuje se na svetloj podlozi)
    page    – stranica sa detaljima (ako postoji)
    sr / en – naziv i kratak opis na srpskom i engleskom

  PRIMER: price: 1500  →  prikazuje se "1.500 din"
*/
window.PRODUCTS = [
  { id: "apifigura", cat: "kozmetika", price: 1800, unit: "", img: "img/proizvodi/apifigura.webp", page: "apifigura",
    sr: { name: "ApiFigura", desc: "Antirid krema sa pčelinjim otrovom i matičnim mlečom" },
    en: { name: "ApiFigura", desc: "Anti-wrinkle cream with bee venom and royal jelly" } },
  { id: "apisalus", cat: "kozmetika", price: 1200, img: "img/proizvodi/apisalus.webp", unit: "30 ml", page: "apisalus",
    sr: { name: "ApiSalus", desc: "Krema sa pčelinjim otrovom – pčelinje zdravlje" },
    en: { name: "ApiSalus", desc: "Cream with bee venom – bee health" } },
  { id: "propolis-krema", cat: "kozmetika", price: 1200, unit: "30 ml", img: "img/proizvodi/propolis-krema.webp", page: "propolis-krema",
    sr: { name: "ProPolis krema", desc: "Mast na bazi propolisa i prirodnih ulja" },
    en: { name: "ProPolis cream", desc: "Ointment made with propolis and natural oils" } },

  { id: "med-suncokret", cat: "med", price: 1000, unit: "1 kg", img: "img/proizvodi/med-suncokret.webp", cover: true,
    sr: { name: "Suncokretov med", desc: "Taman, aromatičan med sa suncokreta" },
    en: { name: "Sunflower honey", desc: "Rich, aromatic sunflower honey" } },
  { id: "med-bagrem", cat: "med", price: 1500, unit: "1 kg", img: "img/proizvodi/med-bagrem.webp", cover: true,
    sr: { name: "Bagremov med", desc: "Svetao, blag bagremov med" },
    en: { name: "Acacia honey", desc: "Light, mild acacia honey" } },
  { id: "propolis-kapi", cat: "pcelinji", price: 200, unit: "10 ml", img: "img/proizvodi/propolis-kapi.webp", cover: true, pos: "50% 30%",
    sr: { name: "Propolis kapi 30%", desc: "Prečišćeni propolis u razblaženom alkoholu" },
    en: { name: "Propolis drops 30%", desc: "Purified propolis in diluted alcohol" } },
  { id: "propolis-sprej", cat: "pcelinji", price: 450, unit: "20 ml", img: "img/proizvodi/propolis-sprej.webp", cover: true, pos: "50% 30%",
    sr: { name: "Propolis sprej 30%", desc: "Prečišćeni propolis u spreju" },
    en: { name: "Propolis spray 30%", desc: "Purified propolis spray" } },
  { id: "apitox-sakupljac", cat: "oprema", price: null, priceEur: 400, unit: "", img: "img/sakupljac/komplet.jpg", cover: true, page: "apitox-sakupljac",
    sr: { name: "Apitox sakupljač", desc: "Uređaj za sakupljanje pčelinjeg otrova" },
    en: { name: "Apitox collector", desc: "Bee venom collecting device" } }
];

/* Kontakt za porudžbine / Order contact */
window.SHOP = {
  phone: "+381641285796",       // za WhatsApp i poziv
  phoneLabel: "064 128 5796",
  email: "goxyst@mts.rs"
};
