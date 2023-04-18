import pandas as pd
faktorji_df = pd.read_csv("baze/manjse/FaktorOseb.csv")

# pomen kode: očevanje nesreč po faktorjih osebe
# izpis: je označeno ob izpisu

# PAS
PasDA_df= faktorji_df.loc[faktorji_df["UporabaVarnostnegaPasu"] == "DA"]
PasNE_df= faktorji_df.loc[faktorji_df["UporabaVarnostnegaPasu"] == "NE"]
PasNEZNANO_df= faktorji_df.loc[faktorji_df["UporabaVarnostnegaPasu"] == "NEZNANO"]
percentage = len(PasDA_df) / (len(PasDA_df)+len(PasNE_df)) * 100
print(f"The percentage of rows where UporabaVarnostnegaPasu is 'DA' is: {percentage:.2f}%")
print(f"The number of rows where UporabaVarnostnegaPasu is 'NEZNANO is {len(PasNEZNANO_df)}")

# ALKOHOL
alkoDA_df= faktorji_df.loc[faktorji_df["VrednostAlkotesta"] > 0]
percentageA = len(alkoDA_df) / len(faktorji_df) * 100
print(f"The percentage of rows where VrednostAlkotesta is greater than 0 is: {percentageA:.2f}%")

# STROKOVNI
strokovniDA_df= faktorji_df.loc[faktorji_df["VrednostStrokovnegaPregleda"] > 0]
percentageS = len(strokovniDA_df) / len(faktorji_df) * 100
print(f"The percentage of rows where VrednostStrokovnegaPregleda is greater than 0 is: {percentageS:.2f}%")

# vizualizacija
import matplotlib.pyplot as plt
import seaborn as sns

fig, axs = plt.subplots(ncols=3, figsize=(15, 5))

sns.countplot(data=faktorji_df, x='UporabaVarnostnegaPasu', ax=axs[0])
axs[0].set_title('Uporaba varnostnega pasu')

sns.histplot(data=faktorji_df, x='VrednostAlkotesta', bins=10, ax=axs[1]) # type: ignore
axs[1].set_title('Vrednost alkotesta')

sns.histplot(data=faktorji_df, x='VrednostStrokovnegaPregleda', bins=10, ax=axs[2])# type: ignore
axs[2].set_title('Vrednost strokovnega pregleda')

plt.suptitle('Faktorji oseb', fontsize=16)
plt.show()