from itertools import combinations

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
mejor_valor = 0
mejor_combinacion = []
combinaciones_evaluadas = 0

for r in range(1, len(objetos) + 1):
    for combo in combinations(objetos, r):
        combinaciones_evaluadas += 1
        volumen_total = sum(o["vol"] for o in combo)
        valor_total = sum(o["val"] for o in combo)

        if volumen_total <= capacidad_max and valor_total > mejor_valor:
            mejor_valor = valor_total
            mejor_combinacion = combo 

print(f"Valor máximo obtenido: ${mejor_valor}")
volumen_total_mejor = sum(o["vol"] for o in mejor_combinacion)
print(f"Volumen total: {volumen_total_mejor} cm³")
print("Objetos elegidos (id, volumen, valor):")
for o in mejor_combinacion:
    print(f"- id {o['id']}: vol={o['vol']} cm³, val=${o['val']}")
print(f"Combinaciones evaluadas: {combinaciones_evaluadas}")

