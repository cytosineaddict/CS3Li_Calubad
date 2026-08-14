ship_wt = 50000
max_wt = 10000

def calculate_fuel(cargo_wt):
    total_wt = ship_wt + cargo_wt
    fuel = total_wt * 3
    return fuel

cargo_wt = 0

while True:
    cargo = input("good day space ranger, what to bring today? ")

    if cargo == "launch":
        break

    elif cargo == "satellite":
        print("added +1 satellite.")
        cargo_wt += 1000

    elif cargo == "rover":
        print("added +1 rover.")
        cargo_wt += 2500

    elif cargo == "supplies":
        print("added +1 supplies.")
        cargo_wt += 500

    else:
        print("get that thing out of my starship.")

    if cargo_wt > max_wt:
        print("this too heavy!")
        break

fuel = calculate_fuel(cargo_wt)

print("total cargo weight", cargo_wt, "kg")
print("estimated expended fuel", fuel, "gallons")
