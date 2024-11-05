'''
Calculo del presupuesto anual consuderando mes con mes (6 meses)
'''

budget_enero = input("Introduce el presupuesto de enero: ")
budget_febrero = input("Presupuesto de febrero: ")
budget_marzo = input("Presupuesto de marzo: ")
budget_abril = input("Presupuesto de abril: ")
budget_mayo = input("Presupuesto de mayo: ")
budget_junio = input("Presupuesto de junio: ")

budget_enero = int(budget_enero)
budget_febrero = int(budget_febrero)
budget_marzo = int(budget_marzo)
budget_abril = int(budget_abril)
budget_mayo = int(budget_mayo)
budget_junio = int(budget_junio)

budget_total = budget_enero + budget_febrero + budget_marzo + budget_abril + budget_mayo + budget_junio
print("Esto es el presupuesto total: ", budget_total)

budget_total = int(budget_total)
budget_promedio = budget_total / 6
print("El presupuesto promedio total es: ", budget_promedio)