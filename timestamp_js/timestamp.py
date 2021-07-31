# -------------------------------------------------------------------------- #
# Copyright (c) 2021. Nikola Vukićević                                       #
# -------------------------------------------------------------------------- #

import math

sekundeUMinutu  = 60
sekundeUSatu    = sekundeUMinutu * 60;   # 360
sekundeUDanu    = sekundeUSatu   * 24;   # 8640
sekundeUGodiniN = sekundeUDanu   * 365;  # 3153600
sekundeUGodiniP = sekundeUDanu   * 366;  # 3162240

dani = [
	365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  # 1970 - 1979
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365,  # 1980 - 1989
    365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  # 1990 - 1999
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365,  # 2000 - 2010
    365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  # 2010 - 2019
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365,  # 2020 - 2029
    365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  # 2030 - 2039
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365,  # 2040 - 2049
    365, 365, 366, 365, 365, 365, 366, 365, 365, 365,  # 2050 - 2059
    366, 365, 365, 365, 366, 365, 365, 365, 366, 365,  # 2060 - 2069
]

meseciN = [
	0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]

meseciP = [
	0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31
]

def inicijalizacijaNiza(niz):
	r = range(1, len(niz))
	for i in r:
		niz[i] = niz[i] + niz[i - 1]

inicijalizacijaNiza(dani)
inicijalizacijaNiza(meseciN)
inicijalizacijaNiza(meseciP)


def binarnaPretraga(n, niz):
	le  = 0
	de  = len(niz) - 1;
	ind = math.floor((le + de) * 0.5)
		
	while(le < de):
		if n == niz[ind]: return ind
			
		if(n < niz[ind]):
			de = ind - 1
		else:
			le = ind + 1
		
		ind = math.floor((le + de) * 0.5)

	return ind;

def pronalazenjeGodine(dan, niz, epoha):
	if dan <= 365:
		return {
			'godina':    epoha,
			'korekcija': 0
		}

	ind = binarnaPretraga(dan, niz)

	return {
		'godina':    epoha + ind,
		'korekcija': niz[ind - 1]
	}


def daLiJePrestupna(godina):
	if godina % 4 == 0:
		if godina % 100 == 0:
			if godina % 400 == 0: return True
			return False
		else:
			return True
	
	return False

def pronalazenjeMeseca(dan, prestupna, nizN, nizP):
	if prestupna == True:
		niz = nizP
	else:
		niz = nizN
	
	ind = binarnaPretraga(dan, niz)
		
	return {
		'mesec':     ind,
		'korekcija': niz[ind - 1]
	}

def timestampUDatum(t):
	stamp          = t / sekundeUDanu
	stamp          = math.ceil(stamp)
	rez            = pronalazenjeGodine(stamp, dani, 1970)
	godina         = rez['godina']
	prestupna      = daLiJePrestupna(godina)
	danUGodini     = stamp - rez['korekcija']
	rez            = pronalazenjeMeseca(danUGodini, prestupna, meseciN, meseciP)
	mesec          = rez['mesec']
	dan            = danUGodini - rez['korekcija']

	return {
		'godina': godina,
		'mesec':  mesec,
		'dan':    dan
	}

print(timestampUDatum(1627723319))
