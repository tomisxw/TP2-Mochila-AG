objetos = [
    {"id": 1, "vol": 150, "val": 20},
    {"id": 2, "vol": 325, "val": 40},
    {"id": 3, "vol": 600, "val": 50},
    {"id": 4, "vol": 805, "val": 36},
    {"id": 5, "vol": 430, "val": 25},
    {"id": 6, "vol": 1200, "val": 64},
    {"id": 7, "vol": 770, "val": 54},
    {"id": 8, "vol": 60, "val": 18},
    {"id": 9, "vol": 930, "val": 46},
    {"id": 10, "vol": 353, "val": 28}
]

capacidad_max = 4200

for o in objetos:
    o["ratio"] = o["val"] / o["vol"]

objetos_ordenados = sorted(objetos, key=lambda x: x["ratio"], reverse=True)
capacidad_actual = 0
valor_total = 0
seleccionados = []

for o in objetos_ordenados:
    if capacidad_actual + o["vol"] <= capacidad_max:
        seleccionados.append(o)
        capacidad_actual += o["vol"]
        valor_total += o["val"]

print("===== Resultado algoritmo greedy =====")
print(f"Valor total obtenido: ${valor_total}")
print(f"Volumen total: {capacidad_actual} cm³")
print("Objetos seleccionados (id, volumen, valor, ratio):")
for o in seleccionados:
    print(f"- id {o['id']}: vol={o['vol']} cm³, val=${o['val']}, ratio={o['ratio']:.4f}")

