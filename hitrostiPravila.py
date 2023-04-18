import pandas as pd
import matplotlib.pyplot as plt

# preberemo datoteke
folk_df = pd.read_csv("baze/manjse/Osebe.csv")
problemi_df = pd.read_csv("baze/manjse/Nesreca.csv")

# pobere use voznike useh starosti katerih vzrok nesreče je "NEPRILAGOJENA HITROST"
skupi = pd.merge(folk_df, problemi_df, on='ZaporednaStevilkaOsebeVPN')

test = skupi[skupi['VzrokNesrece'].str.contains('NEPRILAGOJENA HITROST')]
meseci_izpita_counts = skupi['MeseciIzpita'].value_counts().sort_index()

# nwm kaj nej s tm
plt.bar(test['VzrokNesrece'], test['MeseciIzpita'])
plt.show()



# katera skupina večkrat ne upošteva cestnih pravil



