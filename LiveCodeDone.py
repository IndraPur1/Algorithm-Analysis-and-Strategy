import random

# Part 1: Function to generate random employee data
def generate_employee_data(N):
    """
    Generate random employee data for N employees.
    
    Parameters:
        N (int): Number of employees to generate.
        
    Returns:
        list: List of dictionaries containing employee data.
    """
    if N <= 0:
        return []
    
    employees = []
    for i in range(1, N + 1):
        employee = {
            "id": f"EMP{i}",
            "tahun": random.randint(0, 5),
            "bulan": random.randint(0, 11),
            "target": random.randint(50, 200),
            "realisasi": random.randint(0, 250),
            "base_bonus": random.randint(5, 50)
        }
        employees.append(employee)
    
    return employees

# Part 2: Program to determine optimal Hak Bonus
# Helper functions for bonus calculation
def calculate_kpi(employee):
    kpi = employee["realisasi"] / employee["target"]
    return kpi >= 0.7

def calculate_bonus_ratio(tahun, bulan):
    total_months = (tahun * 12) + bulan
    if total_months <= 15:
        return 0.5
    elif total_months <= 25:
        return 0.7
    elif total_months <= 35:
        return 0.9
    else:
        return 1.0

def calculate_hak_bonus(employee):
    if not calculate_kpi(employee):
        return 0
    ratio = calculate_bonus_ratio(employee["tahun"], employee["bulan"])
    return employee["base_bonus"] * ratio

# Dynamic Programming function to allocate bonuses
def allocate_bonuses(employees, max_budget):
    n = len(employees)
    hak_bonuses = [calculate_hak_bonus(emp) for emp in employees]
    
    # DP table: dp[i][b] = max total Hak Bonus with budget b using first i employees
    dp = [[0 for _ in range(int(max_budget) + 1)] for _ in range(n + 1)]
    # Keep track of which employees are selected
    selected = [[False for _ in range(int(max_budget) + 1)] for _ in range(n + 1)]
    
    # Step-by-step DP table filling
    print("\nStep-by-Step DP Table Construction:")
    print("Budget values are in Juta Rupiah.")
    print("dp[i][b] represents the maximum total Hak Bonus using the first i employees with budget b.")
    print("-" * 80)
    
    # List of budget points to display (to match slide style, not showing all budgets)
    budget_points = [0] + [int(hak_bonuses[i]) for i in range(n) if hak_bonuses[i] > 0]
    budget_points = sorted(set(budget_points + [int(max_budget)]))
    
    # Fill DP table
    for i in range(1, n + 1):
        for budget in range(int(max_budget) + 1):
            # Option 1: Skip employee i-1
            dp[i][budget] = dp[i-1][budget]
            selected[i][budget] = False
            # Option 2: Include employee i-1 if budget allows and they are eligible
            cost = hak_bonuses[i-1]
            if cost > 0 and budget >= cost:
                if dp[i-1][budget - int(cost)] + cost > dp[i-1][budget]:
                    dp[i][budget] = dp[i-1][budget - int(cost)] + cost
                    selected[i][budget] = True
        
        # Display the row for this employee (only for selected budget points)
        if hak_bonuses[i-1] > 0:  # Only show for eligible employees
            print(f"i={i} (Employee {employees[i-1]['id']}, Hak Bonus={hak_bonuses[i-1]}):")
            row = [str(dp[i][b]) for b in budget_points]
            print(f"Budget: {budget_points}")
            print(f"DP Row: {row}")
            print("-" * 80)
    
    # Backtrack to find selected employees
    allocated_bonuses = [0] * n
    remaining_budget = int(max_budget)
    selected_employees = []
    for i in range(n, 0, -1):
        if selected[i][remaining_budget]:
            allocated_bonuses[i-1] = hak_bonuses[i-1]
            selected_employees.append(employees[i-1]["id"])
            remaining_budget -= int(hak_bonuses[i-1])
    
    return allocated_bonuses, selected_employees, dp[n][int(max_budget)]

# Main program
def main():
    # Generate employee data (let's use N=4 as in the original problem)
    N = 4
    max_budget = 50  # Example: 50 Juta Rupiah (can be changed as needed)
    
    print("Generating Employee Data...")
    employees = generate_employee_data(N)
    print("\nEmployee Data Table:")
    print("ID\tTahun\tBulan\tTarget\tRealisasi\tBase Bonus")
    print("-" * 50)
    for emp in employees:
        print(f"{emp['id']}\t{emp['tahun']}\t{emp['bulan']}\t{emp['target']}\t{emp['realisasi']}\t\t{emp['base_bonus']}")
    
    # Calculate Hak Bonus for each employee
    print("\nCalculating Hak Bonus for Eligible Employees:")
    hak_bonuses = []
    for emp in employees:
        hak_bonus = calculate_hak_bonus(emp)
        kpi = emp["realisasi"] / emp["target"]
        total_months = (emp["tahun"] * 12) + emp["bulan"]
        ratio = calculate_bonus_ratio(emp["tahun"], emp["bulan"])
        print(f"{emp['id']}: KPI={kpi:.2f}, Lama Bekerja={total_months} months, Ratio={ratio*100}%, Hak Bonus={hak_bonus} Juta")
        hak_bonuses.append(hak_bonus)
    
    # Allocate bonuses using DP
    print(f"\nAllocating Bonuses with Maximum Budget = {max_budget} Juta Rupiah...")
    allocated_bonuses, selected_employees, max_total_bonus = allocate_bonuses(employees, max_budget)
    
    # Display results
    print("\nFinal Bonus Allocation Results:")
    print(f"Maximum Total Hak Bonus Achieved: {max_total_bonus} Juta Rupiah")
    print("Selected Employees (by ID):", selected_employees if selected_employees else "None")
    print("\nEmployee Bonuses:")
    for i, emp in enumerate(employees):
        print(f"{emp['id']}: {allocated_bonuses[i]} Juta Rupiah")
    print(f"Total Biaya Bonus: {sum(allocated_bonuses)} Juta Rupiah")

# Complexity Analysis
def complexity_analysis(N, max_budget):
    print("\nComplexity Analysis:")
    print(f"- Time Complexity: O(N * max_budget), where N is the number of employees and max_budget is the maximum budget.")
    print(f"  - The DP table has N+1 rows and max_budget+1 columns, and each cell is computed in O(1) time.")
    print(f"  - For N={N} and max_budget={max_budget}, total operations ≈ {N * max_budget}.")
    print(f"- Space Complexity: O(N * max_budget) for the DP table.")
    print(f"  - The table stores (N+1) * (max_budget+1) entries.")

if __name__ == "__main__":
    main()
    complexity_analysis(N=4, max_budget=50)