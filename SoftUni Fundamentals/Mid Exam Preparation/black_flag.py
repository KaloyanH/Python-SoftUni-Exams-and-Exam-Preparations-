days = int(input())
plunder_a_day = int(input())
expected_plunder = float(input())

current_plunder = 0

for days in range(1, days+1):
    current_plunder += plunder_a_day

    if days % 3 == 0:
        current_plunder += plunder_a_day * 0.5

    if days % 5 == 0:
        current_plunder -= current_plunder * 0.3

percent_plunder = current_plunder / expected_plunder * 100

if current_plunder >= expected_plunder:
    print(f"Ahoy! {current_plunder:.2f} plunder gained.")

else:
    print(f"Collected only {percent_plunder:.2f}% of the plunder.")
