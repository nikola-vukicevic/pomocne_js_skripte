# ---------------------------------------------------------------------------- #
# Copyright (c) 2021. Nikola Vukićević
# ---------------------------------------------------------------------------- #

import re # split, sub

# ----- konfiguracija -------------------------------------------------------- #

datoteka_ulaz               = "highlighter.js"
datoteka_izlaz              = "highlighter.js"
TOKEN_ENTER                 = "\n" # mooožda promenim u "\r\n", ako zatreba
ISPIS_PORUKA                = True
UKLANJANJE_PRAZNIH_REDOVA   = True
GRANICA_PRAZNI_REDOVI       = 1
WSP                         = ""
TEKST_KOMENTAR              = """/* -------------------------------------------------------------------------- */
// Syntax highlighter v1.4.2
// Copyright (c) 2021. Nikola Vukićević
/* -------------------------------------------------------------------------- */

"""

# ----- funkcije ------------------------------------------------------------- #

def rastavljanje_teksta(tekst):
	regex = "(\/\/|/\*|\*/|\\\.{1}|\"|\'|\`|\n|\r|\t| )"
	lista = re.split(regex, tekst)
	return lista

def da_li_je_whitespace(znak):
	return znak == " " or znak == "\n" or znak == "\r" or znak == "\t"

def obrada_wsp_stringa(nova_lista):
	global WSP
	if len(WSP) == 0: return

	s = ""
	i = len(WSP) - 1
	b = 0
	
	while WSP[i] != "\n" and WSP[i] != "\r" : # i ne sme da padne ispod nule,
		s = WSP[i] + s                        # ali, WSP se "načinje" samo kada
		i = i - 1                             # se naidje na "\n"

	while i >= 0 and b <= GRANICA_PRAZNI_REDOVI:
		if WSP[i] == "\n" or WSP[i] == "\r":
			b = b + 1
		i = i - 1

	while b > 0:
		s = "\r\n" + s
		b = b - 1

	nova_lista.append( s )
	WSP = ""

def obrada_tokena(kontekst, token, lista, nova_lista):
	if token == "": return
	global WSP
	
	if kontekst > 2 or UKLANJANJE_PRAZNIH_REDOVA  == False:
		nova_lista.append( token )
		return
	if token == "\n" or token == "\r":
		WSP = WSP + "\n"
		return

	if da_li_je_whitespace(token):
		if len(WSP) > 0:
			WSP = WSP + token
		else:
			nova_lista.append( token )
		return

	obrada_wsp_stringa(nova_lista)
	nova_lista.append( token )

def razvrstavanje_tokena(token, stek, lista, nova_lista):
	global WSP
	kontekst  = stek[len(stek) - 1]
	if token == "": return

	if token == "/*":
		if kontekst == 0:
			stek.append(1)
			return
	
	if token == "*/":
		if kontekst == 1:
			stek.pop()
			return
	
	if token == "//":
		if kontekst == 0:
			stek.append(2)
			return
	
	if token == "\n" or token == "\r":
		if kontekst == 2:
			stek.pop()
			WSP = WSP + token

	if token == "\"":
		if kontekst == 0: stek.append(3)
		if kontekst == 3: stek.pop()

	if token == "\'":
		if kontekst == 0: stek.append(4)
		if kontekst == 4: stek.pop()

	if token == "`":
		if kontekst == 0: stek.append(5)
		if kontekst == 5: stek.pop()
	
	if kontekst == 0 or kontekst > 2:
		obrada_tokena(kontekst, token, lista, nova_lista)

def precesljavanjeListe(lista):
	nova_lista = []
	stek       = [ 0 ]
	
	for token in lista:
		razvrstavanje_tokena(token, stek, lista, nova_lista)
	
	return nova_lista

def spajanje_praznih_redova(tekst):
	lista = rastavljanje_teksta(tekst)
	lista = precesljavanjeListe(lista)
	s = ""
	for token in lista:
		if token != "":
			s = s + token
	return s

def main():
	
	# ----- ucitavanje teksta iz datoteke ------------------------------------ #

	f   = open(datoteka_ulaz, "rb")
	s_1 = f.read().decode("utf-8").replace("\r\n", "\n")
	f.close()

	# ----- obrada teksta ---------------------------------------------------- #

	s_2 = spajanje_praznih_redova(s_1)
	s_2 = TEKST_KOMENTAR + s_2.strip() + "\n"
	s_2 = s_2.encode("utf-8")

	# ----- upis teksta u datoteku ------------------------------------------- #

	f = open(datoteka_izlaz, "wb")
	f.write(s_2)
	f.close()

	if ISPIS_PORUKA == True:
		print("Komentari uklonjeni")
		if UKLANJANJE_PRAZNIH_REDOVA == True:
			print("Prazni redovi uklonjeni")
