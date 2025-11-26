def fibonacci_change_greedy():
    # Input
    n = int(input())
    
    # Generate Fibonacci numbers seperti mines dalam gold mining
    # Buat list fibonacci numbers sampai batas yang dibutuhkan
    fibonacci = []
    a, b = 1, 1
    while a <= n:
        fibonacci.append(a)
        a, b = b, a + b
    
    # Sort descending seperti mines.sort() dalam gold mining
    # Dalam hal ini kita ingin yang terbesar dulu untuk greedy choice
    fibonacci.sort(reverse=True)
    
    # Inisialisasi seperti dalam gold mining dan activity selection
    remaining_amount = n  # seperti remaining_time dalam gold mining
    total_coins = 0       # seperti total_gold dalam gold mining
    selected_fibs = []    # seperti selected_activities untuk tracking
    
    # Loop greedy seperti dalam gold mining dengan constraint checking
    for fib_value in fibonacci:
        # Constraint check seperti time_needed <= remaining_time
        # Gunakan fibonacci terbesar yang masih <= remaining amount
        while fib_value <= remaining_amount:
            # Select seperti total_gold += gold_amount dalam gold mining
            selected_fibs.append(fib_value)
            total_coins += 1
            # Update seperti remaining_time -= time_needed dalam gold mining
            remaining_amount -= fib_value
            
        # Jika sudah habis, break seperti constraint check
        if remaining_amount == 0:
            break
    
    return total_coins

# Jalankan program
result = fibonacci_change_greedy()
print(result)