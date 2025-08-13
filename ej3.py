from itertools import combinations

items = [
    {"id": 1, "peso": 1800, "valor": 72},
    {"id": 2, "peso": 600,  "valor": 36},
    {"id": 3, "peso": 1200, "valor": 60},
]
capacidad = 3000

def exhaustivo(items, capacidad):
    mejor_valor, mejor_combo = 0, tuple()
    evaluadas = 0
    n = len(items)
    for r in range(1, n + 1):
        for combo in combinations(items, r):
            evaluadas += 1
            peso  = sum(x["peso"] for x in combo)
            valor = sum(x["valor"] for x in combo)
            if peso <= capacidad and valor > mejor_valor:
                mejor_valor, mejor_combo = valor, combo
    mejor_peso = sum(x["peso"] for x in mejor_combo) if mejor_combo else 0
    return mejor_valor, mejor_peso, mejor_combo, evaluadas

def greedy(items, capacidad):
    orden = sorted(
        [{"id": x["id"], "peso": x["peso"], "valor": x["valor"], "ratio": x["valor"]/x["peso"]}
         for x in items],
        key=lambda d: d["ratio"],
        reverse=True
    )
    sel, peso, valor = [], 0, 0
    for x in orden:
        if peso + x["peso"] <= capacidad:
            sel.append(x)
            peso  += x["peso"]
            valor += x["valor"]
    return valor, peso, sel, orden

if __name__ == "__main__":
    val_opt, peso_opt, combo_opt, evals = exhaustivo(items, capacidad)

    val_greedy, peso_greedy, sel_greedy, orden = greedy(items, capacidad)

    print("EXHAUSTIVO")
    print(f"Valor máximo: ${val_opt} | Peso total: {peso_opt} g")
    print("Ítems:", [x["id"] for x in combo_opt])

    print("\nGREEDY")
    print(f"Valor: ${val_greedy} | Peso: {peso_greedy} g")
    print("Ítems:", [x["id"] for x in sel_greedy])

    print("\nOrden por ratio valor/peso (desc):")
    for x in orden:
        print(f"id {x['id']}: ratio={x['ratio']:.5f} (valor={x['valor']}, peso={x['peso']})")


