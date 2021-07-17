let clanak         = document.getElementById("clanak_tekst");
let nasloviH       = clanak.querySelectorAll('h2, h3, h4');
let linkoviSadrzaj = `<h2 id='sadrzaj_glavni_naslov'>
    <span id='sadrzaj_naslov_span' class='iskljucena_selekcija'>Sadržaj</span>
    <span id='sadrzaj_glavni_naslov_razdvajac'></span>
    <img id='sadrzaj_slika_meni' class='iskljucena_selekcija' title='Otvaranje / zatvaranje sadržaja' src='slike/sadrzaj_meni_01.svg'/>
    <img id='sadrzaj_slika_pin'  class='iskljucena_selekcija' title='Fiksiran / oslobođen sadržaj' src='slike/pin_01.svg'/>
</h2>
<div id='sadrzaj_linkovi'>`;


function daLiJeSlovo(c) {
  return c.toLowerCase() != c.toUpperCase();
}

function daLiJeCifra(c) {
    return c >= '0' && c <= '9';
}

function generisanjeIda(s) {
    let s_p = "";
    for(let i = 0; i < s.length; i++) {
        let z = s[i];

        if(z == ' ') {
            s_p += "_";
            continue;
        }

        if(!daLiJeCifra(z) && !daLiJeSlovo(z)) continue;

        s_p += z;
    }

    return s_p;
}

function generisanjeSadrzaja() {
    nasloviH.forEach(naslov => {
        let iH   = naslov.innerHTML;
        let ajDi = generisanjeIda(iH);
        let tip  = naslov.tagName.toLowerCase();
        naslov.setAttribute("id", ajDi);
        linkoviSadrzaj += `<a class='sadrzaj_naslov_h sadrzaj_${tip}' href='#${ajDi}'>${iH}</a>`;
    });

    linkoviSadrzaj += "</div>";
}

console.log(linkoviSadrzaj);