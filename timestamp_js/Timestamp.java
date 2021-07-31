/* -------------------------------------------------------------------------- */
// Copyright (c) 2021. Nikola Vukiæeviæ
/* -------------------------------------------------------------------------- */

package timestamp;

public class Timestamp {
	
	static int sekundeUMinutu  = 60;
    static int sekundeUSatu    = sekundeUMinutu * 60; // 3600
    static int sekundeUDanu    = sekundeUSatu * 24;   // 86400
    static int sekundeUGodiniN = sekundeUDanu * 365;  // 31536000
    static int sekundeUGodiniP = sekundeUDanu * 366;  // 31622400
    
    static int[] dani = {
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

    static int[] meseciN = {
        0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    };

    static int[] meseciP = {
        0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
    };

    static void inicijalizacijaNiza(int[] niz) {
        for(int i = 1; i < niz.length; i++) {
	        niz[i] = niz[i] + niz[i - 1];
        }
    }

    static int BinarnaPretraga(int a, int[] niz) {
        int le  = 0, de = niz.length - 1;
        int ind = (int)Math.floor((double)(le + de) * 0.5);
	
        while(le < de) {
	        if(a == niz[ind]) return ind;
		
	        if(a < niz[ind]) {
		        de = ind - 1;
	        }
	        else {
		        le = ind + 1;
	        }

	        ind = (int)Math.floor((double)(le + de) * 0.5);
        }

        return ind;
    }

    static Rezultat PronalazenjeGodine(int dan, int[] niz, int epoha) {
        Rezultat rezultat = new Rezultat();

        if(dan <= 365) {
	        rezultat.Rez       = epoha;
	        rezultat.Korekcija = 0;
	        return rezultat;
        }

        int ind = BinarnaPretraga(dan, niz);

        rezultat.Rez       = epoha + ind;
        rezultat.Korekcija = niz[ind - 1];

        return rezultat;
    }

    static Boolean DaLiJePrestupna(int godina) {
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

    static Rezultat pronalazenjeMeseca(int dan, Boolean prestupna, int[] nizN, int[] nizP) {

        int[] niz;

        if(prestupna) {
	        niz = nizP;
        }
        else {
	        niz = nizN;
        }

        int ind = BinarnaPretraga(dan, niz);
	
        Rezultat rezultat = new Rezultat();
        rezultat.Rez       = ind;
        rezultat.Korekcija = niz[ind - 1];

        return rezultat;
    } 

    static Datum timestampUDatum(int t) {
        double   stamp;
        Rezultat rezultat = new Rezultat();
        Datum    datum    = new Datum();

        stamp    = (double)t / sekundeUDanu;
        stamp    = Math.ceil(stamp);
        rezultat = PronalazenjeGodine((int)stamp, dani, 1970);

        int godina        = rezultat.Rez;
        Boolean prestupna = DaLiJePrestupna(godina);
        int danUGodini    = (int)stamp - rezultat.Korekcija;
        rezultat          = pronalazenjeMeseca(danUGodini, prestupna, meseciN, meseciP);
        int mesec         = rezultat.Rez;
        int dan           = danUGodini - rezultat.Korekcija;

        datum.Godina = godina;
        datum.Mesec  = mesec;
        datum.Dan    = dan;

        return datum;
    }
	
	public static void main(String[] args) {
		inicijalizacijaNiza(dani);
        inicijalizacijaNiza(meseciN);
        inicijalizacijaNiza(meseciP);

        Datum datum = timestampUDatum(1627723319);

        System.out.printf(datum.Ispis());
	}

}
