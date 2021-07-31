/* -------------------------------------------------------------------------- */
// Copyright (c) 2021. Nikola Vukićević
/* -------------------------------------------------------------------------- */

using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace Timestamp
{
    public class Datum {
	    public int Godina, Mesec, Dan;

        public String Ispis()
        {
            return Godina.ToString() + "-" +
                   Mesec.ToString() + "-" +
                   Dan.ToString() + "\r\n";
        }
    }

    public class Rezultat {
	    public int Rez, Korekcija;
    }
    
    class Program
    {
        static Int32 sekundeUMinutu  = 60;
        static Int32 sekundeUSatu    = sekundeUMinutu * 60; // 3600
        static Int32 sekundeUDanu    = sekundeUSatu * 24;   // 86400
        static Int32 sekundeUGodiniN = sekundeUDanu * 365;  // 31536000
        static Int32 sekundeUGodiniP = sekundeUDanu * 366;  // 31622400
        
        static Int32[] dani = {
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

        static Int32[] meseciN = {
	        0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        };

        static Int32[] meseciP = {
	        0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
        };

        static void inicijalizacijaNiza(Int32[] niz) {
	        for(int i = 1; i < niz.Length; i++) {
		        niz[i] = niz[i] + niz[i - 1];
	        }
        }

        static Int32 BinarnaPretraga(Int32 a, Int32[] niz) {
	        Int32 le  = 0, de = niz.Length - 1;
	        Int32 ind = (Int32)Math.Floor((Double)(le + de) * 0.5);
		
	        while(le < de) {
		        if(a == niz[ind]) return ind;
			
		        if(a < niz[ind]) {
			        de = ind - 1;
		        }
		        else {
			        le = ind + 1;
		        }

		        ind = (Int32)Math.Floor((Double)(le + de) * 0.5);
	        }

	        return ind;
        }

        static Rezultat PronalazenjeGodine(Int32 dan, Int32[] niz, Int32 epoha) {
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

        static Boolean DaLiJePrestupna(Int32 godina) {
            if (godina % 4 == 0)
            {
                if (godina % 100 == 0)
                {
                    if (godina % 400 == 0) return true;
                    return false;
                }
                else
                {
                    return true;
                }
            }

            return false;
        }

        static Rezultat pronalazenjeMeseca(Int32 dan, Boolean prestupna, Int32[] nizN, Int32[] nizP) {
	
	        Int32[] niz;
	
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

        static Datum timestampUDatum(Int32 t) {
	        Double   stamp;
	        Rezultat rezultat = new Rezultat();
	        Datum    datum    = new Datum();
	
	        stamp          = (Double)t / sekundeUDanu;
	        stamp          = Math.Ceiling(stamp);
	        rezultat       = PronalazenjeGodine((Int32)stamp, dani, 1970);
	
	        int godina     = rezultat.Rez;
	        bool prestupna = DaLiJePrestupna(godina);
	        int danUGodini = (Int32)stamp - rezultat.Korekcija;
	        rezultat       = pronalazenjeMeseca(danUGodini, prestupna, meseciN, meseciP);
	        int mesec      = rezultat.Rez;
	        int dan        = danUGodini - rezultat.Korekcija;

	        datum.Godina = godina;
	        datum.Mesec  = mesec;
	        datum.Dan    = dan;

	        return datum;
        }

        static void Main(string[] args)
        {
            inicijalizacijaNiza(dani);
	        inicijalizacijaNiza(meseciN);
	        inicijalizacijaNiza(meseciP);
	
	        Datum datum = timestampUDatum(1627723319);

            Console.WriteLine(datum.Ispis());
            Console.ReadLine();
        }
    }
}
