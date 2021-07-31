/* -------------------------------------------------------------------------- */
// Copyright (c) 2021. Nikola Vukićević
/* -------------------------------------------------------------------------- */

let sekundeUMinutu  = 60;
let sekundeUSatu    = sekundeUMinutu * 60;   // 3600
let sekundeUDanu    = sekundeUSatu   * 24;   // 86400
let sekundeUGodiniN = sekundeUDanu   * 365;  // 31536000
let sekundeUGodiniP = sekundeUDanu   * 366;  // 31622400

let dani = [
	365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  // 1970 - 1979
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365,  // 1980 - 1989
    365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  // 1990 - 1999
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365,  // 2000 - 2010
    365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  // 2010 - 2019
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365,  // 2020 - 2029
    365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  // 2030 - 2039
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365,  // 2040 - 2049
    365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  // 2050 - 2059
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365,  // 2060 - 2069
];

let meseciN = [
	0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]

let meseciP = [
	0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]

inicijalizacijaNiza(dani);
inicijalizacijaNiza(meseciN);
inicijalizacijaNiza(meseciP);

function inicijalizacijaNiza(niz) {
	for(let i = 1; i < niz.length; i++) {
		niz[i] = niz[i] + niz[i - 1];
	}
}

function binarnaPretraga(n, niz) {
	let le = 0, de = niz.length - 1;
	let ind = Math.floor((le + de) * 0.5);
		
	while(le < de) {
		if(n == niz[ind]) return ind;
			
		if(n < niz[ind]) {
			de = ind - 1;
		}
		else {
			le = ind + 1;
		}

		ind = Math.floor((le + de) * 0.5) ;
	}

	return ind;
}

function pronalazenjeGodine(dan, niz, epoha) {
	if(dan <= 365) {
		return {
			godina:    epoha,
			korekcija: 0
		}
	}

	let ind = binarnaPretraga(dan, niz);

	return {
		godina:    epoha + ind,
		korekcija: niz[ind - 1]
	}
}

function daLiJePrestupna(godina) {
	if(godina % 4   == 0) {
		if(godina % 100 == 0) {
			if(godina % 400 == 0) return true;
			return false;
		}
		else {
			return true;
		}
	}
	
	return false;
}

function pronalazenjeMeseca(dan, prestupna, nizN, nizP) {
	if(prestupna) {
		niz = nizP
	}
	else {
		niz = nizN;
	}

	let ind = binarnaPretraga(dan, niz);
		
	return {
		mesec:     ind,
		korekcija: niz[ind - 1]
	}
} 

function timestampUDatum(t) {
	let stamp, rez;
	stamp          = t / sekundeUDanu;
	stamp          = Math.ceil(stamp);
	//console.log(stamp)
	rez            = pronalazenjeGodine(stamp, dani, 1970);
	//console.log(rez)
	let godina     = rez.godina;
	let prestupna  = daLiJePrestupna(godina);
	let danUGodini = stamp - rez.korekcija;
	//console.log(danUGodini)
	rez            = pronalazenjeMeseca(danUGodini, prestupna, meseciN, meseciP);
	let mesec      = rez.mesec;
	let dan        = danUGodini - rez.korekcija;

	return {
		godina: godina,
		mesec:  mesec,
		dan:    dan
	}
}

let i = 1;

while(i < 31000000) {
	timestampUDatum(i);
	i++;
}
console.log(timestampUDatum(i));
console.log(timestampUDatum(1627723319));
console.log(dani);
console.log(meseciN);
console.log(meseciP);

let godina; 

godina = 2017;
console.log(`Da li je prestupna ${godina}: ${daLiJePrestupna(godina)}`);

godina = 1900;
console.log(`Da li je prestupna ${godina}: ${daLiJePrestupna(godina)}`);

godina = 2012;
console.log(`Da li je prestupna ${godina}: ${daLiJePrestupna(godina)}`);

godina = 2020;
console.log(`Da li je prestupna ${godina}: ${daLiJePrestupna(godina)}`);

//console.log(meseciN);
