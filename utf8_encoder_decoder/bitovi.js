let bitoviOkvir1  = document.getElementById("bitovi_okvir_1");
let poljeVrednost = document.getElementById("vrednost");
let bitoviNiz     = [];

function inicijalizacijaNiza() {
    bitoviNiz = [
        0, 0, 0, 0, 0, 0, 0, 0
    ];
}

function generisanjeTabeleBitova(niz, polje) {
    let stepen = 256;
    niz.forEach(bit => {
        polje.innerHTML += `<div class='bit' title='${stepen}'>${bit}</div`;
        stepen = parseInt(stepen / 2);
    });
}

function popunjavanjeBitova(v, niz) {
    inicijalizacijaNiza();
    let i = 7;
    while(v > 0) {
        console.log(v);
        niz[i] = parseInt(v % 2);
        i--;
        v = parseInt(v / 2);
    }

    generisanjeTabeleBitova();
}
