/* -------------------------------------------------------------------------- */
// Copyright (c) 2021. Nikola Vukićević
/* -------------------------------------------------------------------------- */

#include<iostream>
#include<math.h>
using namespace std;

int sekundeUMinutu  = 60;
int sekundeUSatu    = sekundeUMinutu * 60;   // 3600
int sekundeUDanu    = sekundeUSatu   * 24;   // 86400
int sekundeUGodiniN = sekundeUDanu   * 365;  // 31536000
int sekundeUGodiniP = sekundeUDanu   * 366;  // 31622400

struct Datum {
	int godina, mesec, dan;
};

struct Rezultat {
	int rez, korekcija;
};

int dani[] = {
	365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  // 1970 - 1979
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365,  // 1980 - 1989
    365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  // 1990 - 1999
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365,  // 2000 - 2010
    365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  // 2010 - 2019
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365,  // 2020 - 2029
    365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  // 2030 - 2039
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365,  // 2040 - 2049
    365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  // 2050 - 2059
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365   // 2060 - 2069
};

int meseciN[] = {
	0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
};

int meseciP[] = {
	0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
};

void inicijalizacijaNiza(int niz[], int n) {
	for(int i = 1; i < n; i++) {
		niz[i] = niz[i] + niz[i - 1];
	}
}

void ispisNiza(int niz[], int n) {
	for(int i = 0; i < n; i++) {
		cout << niz[i] << " ";
	}
	
	cout << endl;
}

int binarnaPretraga(int a, int niz[], int n) {
	int le  = 0, de = n - 1;
	int ind = floor((le + de) * 0.5);
		
	while(le < de) {
		if(a == niz[ind]) return ind;
			
		if(a < niz[ind]) {
			de = ind - 1;
		}
		else {
			le = ind + 1;
		}

		ind = floor((le + de) * 0.5) ;
	}

	return ind;
}

struct Rezultat pronalazenjeGodine(int dan, int niz[], int epoha) {
	struct Rezultat rezultat;

	if(dan <= 365) {
		rezultat.rez       = epoha;
		rezultat.korekcija = 0;
		return rezultat;
	}

	int ind = binarnaPretraga(dan, niz, 100);

	rezultat.rez       = epoha + ind;
	rezultat.korekcija = niz[ind - 1];
	
	return rezultat;
}

bool daLiJePrestupna(int godina) {
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

struct Rezultat pronalazenjeMeseca(int dan, bool prestupna, int nizN[], int nizP[]) {
	
	int* niz;
	
	if(prestupna) {
		niz = nizP;
	}
	else {
		niz = nizN;
	}
	
	int ind = binarnaPretraga(dan, niz, 13);
		
	struct Rezultat rezultat;
	rezultat.rez       = ind;
	rezultat.korekcija = niz[ind - 1];
	
	return rezultat;
} 

struct Datum timestampUDatum(int t) {
	double stamp;
	struct Rezultat rezultat;
	struct Datum    datum;
	
	stamp          = (double)t / sekundeUDanu;
	stamp          = ceil(stamp);
	rezultat       = pronalazenjeGodine(stamp, dani, 1970);
	
	int godina     = rezultat.rez;
	bool prestupna = daLiJePrestupna(godina);
	int danUGodini = stamp - rezultat.korekcija;
	rezultat       = pronalazenjeMeseca(danUGodini, prestupna, meseciN, meseciP);
	int mesec      = rezultat.rez;
	int dan        = danUGodini - rezultat.korekcija;

	datum.godina = godina;
	datum.mesec  = mesec;
	datum.dan    = dan;

	return datum;
}

int main() {
	
	inicijalizacijaNiza(dani, 100);
	inicijalizacijaNiza(meseciN, 13);
	inicijalizacijaNiza(meseciP, 13);
	
	struct Datum datum = timestampUDatum(1627723319);
	
	cout << datum.godina << "-" << datum.mesec << "-" << datum.dan << endl;
}

