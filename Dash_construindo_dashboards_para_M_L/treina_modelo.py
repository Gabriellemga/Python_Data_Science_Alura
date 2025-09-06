from ucimlrepo import fetch_ucirepo

heart_disease = fetch_ucirepo(id=45)
dados = heart_disease.data.features
dados["doenca"] = (heart_disease.data.targets > 0) * 1

X = dados.drop(columns='doenca')
y = dados['doenca']

from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=432, stratify=y)

import xgboost as xgb
modelo = xgb.XGBClassifier(objective='binary:logistic')
modelo.fit(X_train, y_train)
preds = modelo.predict(X_test)

from sklearn.metrics import accuracy_score
acuracia = accuracy_score(y_test, preds)
print(f'A acurácia do modelo é {acuracia:.2%}')

import joblib
joblib.dump(modelo, 'modelo_xgboost.pkl')

medianas = X.median()
joblib.dump(medianas, 'medianas.pkl')

