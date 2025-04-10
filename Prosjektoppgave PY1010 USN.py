# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 13:59:17 2025

@author: Jakob Sødal
"""

'''
Prosjektoppgave PY1010 USN
'''

'''
Analyse av Morse Supportavdelingens telefonhenvendelser uke 24.
'''

# Import av pakker:
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# innlesning av kolonner fra excel-fil med info om support tlf-henvendelser 'support_uke_24.xlsx

data = pd.read_excel('support_uke_24.xlsx') # Uke 24, innlesing av .xlsx fil
uke_dag = data['Ukedag'] .values # kolonne 1: ukedag for tlf-samtalen (Mandag osv.)
kl_slett = data['Klokkeslett'] .values # kolonne 2: Klokkeslett for tlf-samtalen
varighet = data['Varighet'] .values #Kolonne 3: tlf-samtalens varighet
tilfredshet = data['Tilfredshet'] .values #kolonne 4: kundens tilfredshet (score: 1-10) 


# søylediagram av antall henvendelser til support uke 24
antall_per_dag = data['Ukedag'] .value_counts() # opptelling av antall tlf-henvendelser per ukedag

# plot av søylediagram for antall tlf-henvendelser uke 24 fordelt på ukedager (mandag osv.)
plt.bar(antall_per_dag.index, antall_per_dag.values) # søylediagram plot
plt.xlabel('Ukedager med tlf-henvendelser') # tittel horisontal akse
plt.ylabel('Antall tlf-henvendelser') # tittel vetikal akse
plt.title('Antall tlf-hendvendeldser per arbeidsuke') # overskrift  
plt.show()

'''
# Korteste og lengste tlf-samtale 
'''

korteste_varighet = varighet.min() # Minste tlf-samtale varighet
lengste_varighet = varighet.max() # Lengste tlf-samtale
# print av korteste og lengste tlf-samtale
print('Korteste tlf-samtale var: ', korteste_varighet, )
print('Lengste tlf-samtale var: ', lengste_varighet)

'''
Gjennomsnittlig samtaletid på tlf-henvendelser uke 24

'''
# Gjennomsnittlig samtaletid på tlf-henvendelser uke 24

# Konverter til timedelta
data['Varighet'] = pd.to_timedelta(data['Varighet'])

# Summer varighetene
total_varighet = data['Varighet'].sum()

# Konverter til sekunder
henvendelser_i_sekunder = data['Varighet'].dt.total_seconds()

# Summer alle sekunder
henvendelser_total_sekunder = henvendelser_i_sekunder.sum()

# Antall henvendelser/tlf-samtaler i kolonnen Varighet
antall_henvendelserlser = len(varighet)

# utregning av gjennomsnittlig varighet på henvendelser/tlf-samtaler i sekunder.
gjennomsnittlig_varighet_sekunder = henvendelser_total_sekunder / antall_henvendelserlser

# Konvertering av gjennomsnittlig varighet fra sekunder til timer:minutter:sekunder
gjennomsnitt_varighet_timedelta = pd.to_timedelta(gjennomsnitt_varighet, unit='s')
# Fjern hundredelene
gjennomsnitt_varighet_timedelta = pd.to_timedelta(gjennomsnitt_varighet, unit='s').floor('s')


print('gjennomsnittlig tlf-samtaletid var:', gjennomsnitt_varighet_timedelta)

'''
Supportvaktene er delt inn i 2-timersbolker: kl 08-10, kl 10-12, kl 12-14 og kl
14-16.

antall henvendelser per 2 timers bolk, visualisert med sektor diagram
 
'''

# oppdeling av kollennen i 2-timers bolker

første_vakt = (kl_slett < '10:00:00' ) # første vakt kl. 08-10
andre_vakt = (kl_slett >= '10:00:00') & ( kl_slett <'12:00:00') # andre vakt kl. 10-12
tredje_vakt = (kl_slett >= '12:00:00') & (kl_slett < '14:00:00') # tredje vakt kl.12-14
fjerde_vakt = (kl_slett >= '14:00:00') & (kl_slett < '16:00:00') # fjerde vakt kl. 14-16


antall_første_vakt = sum(første_vakt)
antall_andre_vakt = sum(andre_vakt)
antall_tredje_vakt = sum(tredje_vakt)
antall_fjerde_vakt = sum(fjerde_vakt)


# Sektordiagram
# Størrelse på kakestykkene
sizes = [antall_første_vakt, antall_andre_vakt, antall_tredje_vakt, antall_fjerde_vakt]
# titler på kakestykkene
labels = ['Første vakt (kl. 08-10)', 'Andre vakt (kl. 10-12)', 'Tredje vakt (kl.12-14)', 'Fjerde vakt kl (14-16)']

# sektordiagram plot
plt.pie(sizes, labels=labels)
plt.title('Antall tlf-samtaler/henvendelser fortdelt på vakter: uke 24')
plt.show()    

'''
# Kundens tilfredshet i NPS (Net Promoter Score)
'''

# Variabelen tilfredshet er kolonne 4: kundens tilfredshet (score: 1-10)
# Tilfeller der kunden ikke har svart på tilfredshet er ikke med i utregningen.
negativ = (tilfredshet >= 1) & (tilfredshet <= 6) # 1-6 = negativ
nøytral = (tilfredshet >= 7) & (tilfredshet <= 8) # 7-8 = nøytral
positiv = (tilfredshet >= 9) & (tilfredshet <= 10) # 9-10 positiv

# summerer kun positive og negative tilbakemeldinger.
antall_negativ = sum(negativ)
antall_positiv = sum(positiv)

# plusser sammen negative og positive 
antall_positiv_negativ = antall_positiv + antall_negativ

# utregning i prosent for positive og negative
prosent_negativ = (antall_negativ / antall_positiv_negativ) * 100
prosent_positiv = (antall_positiv / antall_positiv_negativ) * 100

# NPS = % positive kunder - % negative kunder
NPS =  prosent_positiv - prosent_negativ
# desimal avrunding
NPS_desimal = round(NPS, 1) 

print('Supportavdelingens NPS for uke 24 er:', NPS_desimal,'%' )





