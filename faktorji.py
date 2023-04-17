import pandas as pd
faktorji_df = pd.read_csv("baze/manjse/FaktorOseb.csv")

PasDA= faktorji_df.loc[faktorji_df["UporabaVarnostnegaPasu"] == "DA"]
PasNE= faktorji_df.loc[faktorji_df["UporabaVarnostnegaPasu"] == "NE"]
PasNEZNANO= faktorji_df.loc[faktorji_df["UporabaVarnostnegaPasu"] == "NEZNANO"]
percentage = len(PasDA) / (len(PasDA)+len(PasNE)) * 100
print(f"The percentage of rows where UporabaVarnostnegaPasu is 'DA' is: {percentage:.2f}%")
print(f"The number of rows where UporabaVarnostnegaPasu is 'NEZNANO is {len(PasNEZNANO)}")

alkoDA= faktorji_df.loc[faktorji_df["VrednostAlkotesta"] > 0]
percentageA = len(alkoDA) / len(faktorji_df) * 100
print(f"The percentage of rows where VrednostAlkotesta is greater than 0 is: {percentageA:.2f}%")

strokovniDA= faktorji_df.loc[faktorji_df["VrednostStrokovnegaPregleda"] > 0]
percentageS = len(strokovniDA) / len(faktorji_df) * 100
print(f"The percentage of rows where VrednostStrokovnegaPregleda is greater than 0 is: {percentageS:.2f}%")


