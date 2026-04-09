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

