import random

# generate random employee data
def generate(N):
    if N <= 0:
        return []
    employees = []
    for i in range (1, n + 1):
        employee = {
            "id": f"EMP{i}",
            "Lama Bekerja (Tahun)": random.randint(0,5),
            "Lama Bekerja (Bulan)": random.randint(0,11),
            "Target Penjualan": random.randint(50,200),
            "Realisasi Target": random.randint(0,250),
            "Hak Bonus(Juta)": random.randint(5,50)
        }
        employees.append(employee)
    return employees

#hitung hak bonus
def hitung_kpi(employee):
    kpi = employee["Realisasi Penjualan"] / employee["Target Penjualan"]
    return kpi >= 0.7

def hitung_rasio_bonus(tahun, bulan):
    totalbulan = (tahun * 12) + bulan
    if totalbulan <= 15:
        return 0.5
    elif totalbulan <= 25:
        return 0.7
    elif totalbulan <= 35:
        return 0.9
    else:
        return 1.0

def hitung_hak_bonus(employee):
    if not hitung_kpi(employee):
        return 0
    rasio = hitung_rasio_bonus(employee["Lama Bekerja (Tahun)"], employee["Lama Bekerja (Bulan)"])
    return employee["Hak Bonus"] * rasio

def alokasi_bonus(employees, maxbudget):
    n = len(employees)
    hak_bonus = [hitung_hak_bonus(emp) for emp in employees]

    dp = [[0 for _ in range(int(maxbudget) + 1)] for _ in range (n + 1)]
    selected = [[False for _ in range(int(maxbudget) + 1)] for _ in range(n + 1)]

    budgetnya = [0] + [int(hak_bonus[i]) for i in range(n) if hak_bonus[i] > 0]
    budgetnya = sorted(set(budgetnya + [int(maxbudget)]))

    for i in range(1, n + 1):
        for budget in range(int(maxbudget) + 1):
            dp[i][budget] = dp[i-1][budget]
            selected[i][budget] = False
            cost = hak_bonus[i-1]
            if cost > 0 and budget >= cost:
                if dp[i-i][budget - int(cost)] + cost > dp[i-1][budget]:
                    dp[i][budget] = dp[i-1][budget - int(cost)] + cost
                    selected[i][budget] = True
            
        if hak_bonus[i-1] > 0 :
            print(f"i={i} (Employee {employees[i-1][id]}, Hak Bonus={hak_bonus[i-1]}):")
            row = [str(dp[i][b]) for b in budgetnya]
            print(f"Budget: {budgetnya}")
            print(f"DP Row: {row}")
            print("-" * 80)
        
    allocated_bonus = [0] * n
    sisa_budget = int(maxbudget)
    selected_employees = []
    for i in range (n, 0, -1):
        if selected[i][sisa_budget]:
            allocated_bonus[i-1] = hak_bonus[i-1]
            selected_employees.append(employees[i-1]["id"])
            sisa_budget -= int(hak) int(hak_bonus[i-1])
    
    return allocated_bonus  