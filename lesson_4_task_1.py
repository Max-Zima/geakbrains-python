from sys import argv

script_name, worked_hour, rate, benefit = argv

wages = (int(worked_hour) * int(rate) + int(benefit))
print(f"Ваша заработная плата составила: {wages}")
