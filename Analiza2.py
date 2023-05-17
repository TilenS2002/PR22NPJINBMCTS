#########################################################
#####                                               #####
#####  RFE - najbolši atributi za prediction model  #####
#####                                               #####
#########################################################



from sklearn.ensemble import RandomForestRegressor
from sklearn.feature_selection import RFECV
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.preprocessing import LabelEncoder

cas_df = pd.read_csv('baze/manjse/Cas.csv')
osebe_df = pd.read_csv('baze/manjse/Osebe.csv')
nesreca_df = pd.read_csv('baze/manjse/Nesreca.csv')
splosno_df = pd.read_csv('baze/manjse/Splosno.csv')
cesta_df = pd.read_csv('baze/manjse/Cesta.csv')
faktor_cest_df = pd.read_csv('baze/manjse/FaktorCest.csv')
faktor_oseb_df = pd.read_csv('baze/manjse/FaktorOseb.csv')

merged_df = cas_df.merge(osebe_df, on='ZaporednaStevilkaOsebeVPN')
merged_df = merged_df.merge(nesreca_df, on='ZaporednaStevilkaOsebeVPN')
merged_df = merged_df.merge(splosno_df, on='ZaporednaStevilkaOsebeVPN')
merged_df = merged_df.merge(cesta_df, on='ZaporednaStevilkaOsebeVPN')
merged_df = merged_df.merge(faktor_cest_df, on='ZaporednaStevilkaOsebeVPN')
merged_df = merged_df.merge(faktor_oseb_df, on='ZaporednaStevilkaOsebeVPN')


data = merged_df
data = data.drop("DatumPN", axis=1)
data = data.drop("ZaporednaStevilkaOsebeVPN", axis=1)
data = data.drop("Povzrocitelj", axis=1)
data = data.drop("Drzavljanstvo", axis=1)
print(data.columns)

label_encoder = LabelEncoder()
for column in data.select_dtypes(include='object'):
    data[column] = label_encoder.fit_transform(data[column])

X = data.drop('KlasifikacijaNesrece', axis=1)
y = data['KlasifikacijaNesrece']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf = RandomForestRegressor()

rfecv = RFECV(estimator=rf, cv=5)

rfecv.fit(X_train, y_train)

selected_feature_indices = rfecv.get_support(indices=True)

selected_feature_names = X.columns[selected_feature_indices]

print("Selected Features:")
print(selected_feature_names)
