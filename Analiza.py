import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report
from sklearn.preprocessing import MinMaxScaler
from scipy import stats

# Load and merge the datasets
cas_df = pd.read_csv('baze/manjse/Cas.csv')
faktoroseb_df = pd.read_csv('baze/manjse/Osebe.csv')
nesreca_df = pd.read_csv('baze/manjse/Nesreca.csv')
splosno_df = pd.read_csv('baze/manjse/Splosno.csv')

merged_df = cas_df.merge(faktoroseb_df, on='ZaporednaStevilkaOsebeVPN')
merged_df = merged_df.merge(nesreca_df, on='ZaporednaStevilkaOsebeVPN')
merged_df = merged_df.merge(splosno_df, on='ZaporednaStevilkaOsebeVPN')

print(merged_df.columns)
selected_features = ['VzrokNesrece', 'TipNesrece', 'Starost', 'Spol', 'Drzavljanstvo', 'MeseciIzpita', 'DatumPN','UraPN']
target_variable = 'KlasifikacijaNesrece'

X = merged_df[selected_features]
y = merged_df[target_variable]

# Perform encoding on categorical variables
X_encoded = pd.get_dummies(X, columns=['VzrokNesrece', 'TipNesrece', 'Starost', 'Spol', 'Drzavljanstvo', 'MeseciIzpita', 'DatumPN','UraPN'])

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X_encoded, y, test_size=0.2, random_state=42)

# Random Forest
clf = RandomForestClassifier(n_estimators=100, random_state=42)

# Train the model
clf.fit(X_train, y_train)

# Make predictions
y_pred = clf.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
classification_rep = classification_report(y_test, y_pred)

print("Accuracy:", accuracy)
print("Classification Report:")
print(classification_rep)
