import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# ==============================
# 1. CREAR DATASET
# ==============================

data = {
    "tiempo": [10, 15, 20, 8, 12, 18, 25, 7],
    "transbordos": [0, 1, 2, 0, 1, 2, 3, 0],
    "hora_pico": [0, 1, 1, 0, 1, 0, 1, 0],
    "mejor_ruta": [1, 0, 0, 1, 1, 0, 0, 1]
}

df = pd.DataFrame(data)

# ==============================
# 2. VARIABLES
# ==============================

X = df[["tiempo", "transbordos", "hora_pico"]]
y = df["mejor_ruta"]

# ==============================
# 3. DIVIDIR DATOS
# ==============================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
# ==============================
# 4. ENTRENAR MODELO
# ==============================

modelo = DecisionTreeClassifier()
modelo.fit(X_train, y_train)

# ==============================
# 5. EVALUAR
# ==============================

y_pred = modelo.predict(X_test)
print("Precisión del modelo:", accuracy_score(y_test, y_pred))

# ==============================
# 6. PREDICCIÓN
# ==============================

nueva_ruta = pd.DataFrame([[9, 1, 0]],
                          columns=["tiempo", "transbordos", "hora_pico"])

prediccion = modelo.predict(nueva_ruta)

print("¿Es buena ruta? (1=Sí, 0=No):", prediccion[0])

# ==============================
# 7. PRUEBAS (QA)
# ==============================

def test_prediccion_valida():
    assert prediccion[0] in [0, 1]
    print("✔️ Test predicción válida OK")

def test_precision_aceptable():
    y_pred_test = modelo.predict(X_test)
    acc = accuracy_score(y_test, y_pred_test)
    assert acc >= 0.5
    print("✔️ Test precisión OK")

def test_ruta_simple():
    prueba = pd.DataFrame([[8, 0, 0]],
                          columns=["tiempo", "transbordos", "hora_pico"])
    resultado = modelo.predict(prueba)[0]
    assert resultado == 1
    print("✔️ Test ruta simple OK")

def test_ruta_compleja():
    prueba = pd.DataFrame([[25, 3, 1]],
                          columns=["tiempo", "transbordos", "hora_pico"])
    resultado = modelo.predict(prueba)[0]
    assert resultado == 0
    print("✔️ Test ruta compleja OK")

# ==============================
# 8. EJECUTAR PRUEBAS
# ==============================

if _name_ == "_main_":
    test_prediccion_valida()
    test_precision_aceptable()
    test_ruta_simple()
    test_ruta_compleja()
