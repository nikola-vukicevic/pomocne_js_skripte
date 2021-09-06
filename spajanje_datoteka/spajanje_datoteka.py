# ---------------------------------------------------------------------------- #
# Copyright (c) 2021. Nikola Vukićević
# ---------------------------------------------------------------------------- #

import re

# ----- konfiguracija -------------------------------------------------------- #

datoteka_za_ispis         = 'highlighter.js'
AUTOMATSKO_KODIRANJE      = True
ZAMENA_NAZIVA_PREKO_LISTE = True

# ----- funkcije ------------------------------------------------------------- #

datoteke_za_spajanje = [
	#'proba_01.js' ,
	'01_analiza_izraza.js' ,
	'02_highlighter_funkcije.js' ,
	'03_highlighter_funkcije_regex.js' ,
	'04_definicije_jezika.js' ,
	'05_obradaBlokova.js' ,
	'06_highlighter_demo.js'
]

kodiranje_naziva = [
	[ "analizaIzraza"                              , "aI1"         ] ,
	[ "analizaIzrazaInterpretacija"                , "aII1"        ] ,
	[ "analizaIzrazaTokenizacija"                  , "aIT1"        ] ,
	[ "analizaIzrazaUpisUListu"                    , "aIUUL1"      ] ,
	[ "analizaIzrazaZnak_broj"                     , "aIZ_b1"      ] ,
	[ "analizaIzrazaZnak_operator"                 , "aIZ_o1"      ] ,
	[ "analizaIzrazaZnak_otvorenaZagrada"          , "aIZ_oZ1"     ] ,
	[ "analizaIzrazaZnak_slovo"                    , "aIZ_s1"      ] ,
	[ "analizaIzrazaZnak_zatvorenaZagrada"         , "aIZ_zZ1"     ] ,
	[ "analiza_str_s_Substringova"                 , "assS1"       ] ,
	[ "daLiJeWhiteSpace"                           , "dLJWS1"      ] ,
	[ "daLiSuZnakovi_broj"                         , "dLSZ_b1"     ] ,
	[ "daLiSuZnakovi_operator"                     , "dLSZ_o1"     ] ,
	[ "daLiSuZnakovi_slovo"                        , "dLSZ_s1"     ] ,
	[ "formatiranjeIspisListe"                     , "fIL1"        ] ,
	[ "lekserOpsti"                                , "lO1"         ] ,
	[ "lekserRegex"                                , "lR1"         ] ,
	[ "listaBlokova"                               , "lB174"       ] ,
	[ "listaTokena"                                , "lT174"       ] ,
	[ "neuspesniPokusajUbacivanjaRegularnogIzraza" , "nOURI1"      ] ,
	[ "obradaBlokova"                              , "oB1"         ] ,
	[ "obradaKoda"                                 , "oK1"         ] ,
	[ "obradaLekserBroj"                           , "oLB1"        ] ,
	[ "obradaLekserEscapeSekvenca"                 , "oLES1"       ] ,
	[ "obradaLekserObicanZnak"                     , "oLOZ1"       ] ,
	[ "obradaLekserSpecZnak"                       , "oLSZ1"       ] ,
	[ "obradaLekserWhiteSpace"                     , "oLWS1"       ] ,
	[ "obradaPojedinacnogBloka"                    , "oPB1"        ] ,
	[ "obradaPrepoznatogTokena"                    , "oPT1"        ] ,
	[ "obradaPrepoznatogTokenaRegex"               , "oPTR1"       ] ,
	[ "parserOpsti"                                , "pO1"         ] ,
	[ "parserProveraRegularnogIzraza"              , "pPRI1"       ] ,
	[ "parserRegex"                                , "pR1"         ] ,
	[ "parserTokenPojedinacni"                     , "pTP1"        ] ,
	[ "pokusajUbacivanjaRegularnogIzraza"          , "pURI1"       ] ,
	[ "praznjenjeStringova"                        , "pS1"         ] ,
	[ "prethodniTip"                               , "pT74"        ] ,
	[ "prethodniZnak"                              , "pZ74"        ] ,
	[ "proveraSpecijalnihTokena"                   , "pST1"        ] ,
	[ "punjenjeListeBlokova"                       , "pLB1"        ] ,
	[ "tokeni"                                     , "t74"         ] ,
	[ "ubacivanjeSpecToken"                        , "uST1"        ] ,
	[ "ubacivanje_s_0"                             , "us1"         ] ,
	[ "uslov"                                      , "u94"         ] ,
	[ "utiskivanjeTokenPojedinacni"                , "uTP1"        ] ,
	[ "pomTekst:"                                  , "//pomTekst:" ] ,
]

def kodiranje_naziva_funkcija(tekst):
	lista = re.findall("function .*\(", tekst)

	i = 1

	for token in lista:
		token = token[ 9 : len(token) - 1 ]
		token = [ token , "f" + str(i) ]
		i = i + 1
		tekst = tekst.replace(token[0], token[1])

	return tekst

def zamena_naziva_preko_liste(tekst, lista):
	for zamena in lista:
		tekst = tekst.replace(zamena[0] , zamena[1])

	return tekst

def main():

	s = ""

	#         ----- ucitavanje teksta iz datoteke ------------------------------------ #

	for datoteka in datoteke_za_spajanje:
		f = open( datoteka , "rb")
		s = s + f.read().decode("utf-8") + '\n\n'

	# ----- zamena naziva funkcija ------------------------------------------- #

	if(AUTOMATSKO_KODIRANJE) == True:
		s = kodiranje_naziva_funkcija(s)

	if ZAMENA_NAZIVA_PREKO_LISTE == True:
		s = zamena_naziva_preko_liste(s, kodiranje_naziva)

	# ----- upis u datoteku -------------------------------------------------- #

	f = open(datoteka_za_ispis, "wb")
	s = s.strip() + "\n"
	s = s.encode("utf-8")
	f.write(s)
	f.close()

	print("Datoteke spojene")
