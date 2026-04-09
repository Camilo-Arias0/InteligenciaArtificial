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

# =========================
# 4. MÉTODO DEL CODO (para elegir K)
# =========================
inertia = []

for k in range(1, 10):
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(data_scaled)
    inertia.append(kmeans.inertia_)

plt.plot(range(1, 10), inertia, marker='o')
plt.xlabel("Número de clusters")
plt.ylabel("Inercia")
plt.title("Método del codo")
plt.show()

# =========================
# 5. MODELO K-MEANS
# =========================
kmeans = KMeans(n_clusters=3, random_state=0)
kmeans.fit(data_scaled)

data["cluster"] = kmeans.labels_

# =========================
# 6. EVALUACIÓN
# =========================
score = silhouette_score(data_scaled, data["cluster"])
print("\nSilhouette Score:", score)


