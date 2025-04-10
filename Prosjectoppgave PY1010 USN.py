# -*- coding: utf-8 -*-
"""
Created on Mon Apr  7 13:59:17 2025

@author: Jakob Sødal
"""

'''
Prosjektoppgave PY1010 USN
'''



'''
Analyse av Morse Supportavdelingens telefonhenvendelser.
'''

# Import av pakker:

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# innlesning av excel-fil med info om support tlf-henvendelser 'support_uke_24.xlsx

data = pd.read_excel('support_uke_24.xlsx') # Uke 24, innlesing av .xlsx fil
uke_dag = data['Ukedag'] .values # kolonne 1: ukedag for tlf-samtalen (Mandag osv.)
kl_slett = data['Klokkeslett'] .values # kolonne 2: Klokkeslett for tlf-samtalen
varighet = data['Varighet'] .values #Kolonne 3: tlf-samtalens varighet
score = data['Tilfredshet'] .values #kolonne 4: kundens tilfredshet (score: 1-10) 


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
print('Korteste tlf-samtaletid for uke 24 var: ', korteste_varighet, )
print('Lengste tlf-samtale var: ', lengste_varighet)

'''
d)
'''
# Gjennomsnittlig samtaletid på tlf-henvendelser uke 24

# Konvertering av 'Varighet'-kolonnen til timedelta
#data['Varighet'] = pd.to_timedelta(data['Varighet'])

# Summer varighetene
total_varighet_sekunder = data['Varighet'].sum()
print(total_varighet_sekunder)

# Konverter til sekunder
#data['Sekunder'] = data['Varighet'].dt.total_seconds()


# Antall tlf-samtaler/henvendelser i uke 24 
Antall_henvendelser_varighet = len(varighet)

print(Antall_henvendelser_varighet)

# Konvertering av gjennomsnittlig varighet til timer:minutter:sekunder
#gjennomsnitt_varighet_format = pd.to_timedelta(gjennomsnitt_varighet, unit='s')
# Fjern hundredelene
#gjennomsnitt_varighet_format = pd.to_timedelta(gjennomsnitt_varighet, unit='s').floor('s')

#print('gjennomsnittlig tlf-samtale varte: ', gjennomsnitt_varighet_format)



