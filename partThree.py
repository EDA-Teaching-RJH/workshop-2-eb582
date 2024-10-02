def main():
    pounds = pounds_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to charge? "))
    charge = pounds * percent
    print(f"Tip Charge {percent:.2f}%" , f" Total £{charge:.1f}")


def pounds_to_float(d):
    return float(d.replace("£"," ").strip())

def percent_to_float(p):
    return float(p.replace("%"," ").strip()) / 100

main()
