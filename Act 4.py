# =========================
# 1. LIBRERÍAS
# =========================
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# =========================
# 2. CREAR DATASET (SIMULADO)
# =========================
np.random.seed(0)

data = pd.DataFrame({
    "hora": np.random.randint(5, 22, 100),
    "latitud": np.random.uniform(4.5, 4.8, 100),
    "longitud": np.random.uniform(-74.2, -74.0, 100),
    "pasajeros": np.random.randint(10, 100, 100),
    "tiempo_espera": np.random.randint(1, 20, 100),
    "distancia_ruta": np.random.uniform(1, 15, 100)
})

print("Datos iniciales:")
print(data.head())

# =========================
# 3. NORMALIZACIÓN
# =========================
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)


