#########################################################
#####                                               #####
#####         RandomForest Prediction Model         #####
#####                                               #####
#########################################################

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import MinMaxScaler
from scipy import stats

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

print(merged_df.columns)

selected_features = ['UraPN', 'Starost', 'VrstaUdelezenca', 'PoskodbaUdelezenca',
       'MeseciIzpita', 'VzrokNesrece', 'TipNesrece', 'VrstaCesteNaselja',
       'VremenskeOkoliscine', 'StanjePrometa']

target_variable = 'KlasifikacijaNesrece'

X = merged_df[selected_features]
y = merged_df[target_variable]


X_encoded = pd.get_dummies(X, columns=['UraPN', 'Starost', 'VrstaUdelezenca', 'PoskodbaUdelezenca',
       'MeseciIzpita', 'VzrokNesrece', 'TipNesrece', 'VrstaCesteNaselja',
       'VremenskeOkoliscine', 'StanjePrometa'])

# X_encoded = pd.get_dummies(X, columns=['UraPN', 'Starost',
#        'MeseciIzpita', 'VrstaCesteNaselja',
#        'VremenskeOkoliscine', 'StanjePrometa'])

# 'UraPN', 'Starost', 'VrstaUdelezenca',
#        'MeseciIzpita', 'VzrokNesrece', 'TipNesrece', 'VrstaCesteNaselja',
#        'VremenskeOkoliscine', 'StanjePrometa']


X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Accuracy:", accuracy) #current Accuracy: 0.790845710821461  15.5. 17:40
print("Classification Report:")
print(classification_rep)


