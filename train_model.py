import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
import joblib

# Membaca dataset dari file CSV
df = pd.read_csv('insurance.csv')  # Ganti dengan path file Anda jika berbeda

# Menyiapkan fitur (X) dan target (y)
X = df[['age', 'sex', 'bmi', 'children', 'smoker', 'region']]  # Fitur
y = df['charges']  # Target (biaya asuransi)

# Mengubah kategori menjadi angka (encoding)
X['sex'] = X['sex'].map({'male': 0, 'female': 1})
X['smoker'] = X['smoker'].map({'no': 0, 'yes': 1})
region_map = {'southeast': 0, 'southwest': 1, 'northeast': 2, 'northwest': 3}
X['region'] = X['region'].map(region_map)

# Membagi data menjadi data training dan data testing
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Membuat model RandomForestRegressor dan melatih model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Menyimpan model yang telah dilatih ke file .pkl
joblib.dump(model, 'model_asuransi.pkl')

print("Model telah disimpan sebagai 'model_asuransi.pkl'")
