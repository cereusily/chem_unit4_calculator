import math

"""global variables"""
Kw = 1.0 * 10**-14

def find_pH(st_conc, Ka):
    Ka = float(Ka)
    Kb1 = Kw / Ka
    Kb = math.sqrt(st_conc * Kb1)

    # Formats Kb value, Kb value == [OH]
    Kb_format = "{:e}".format(Kb)
    print(f"Kb Value = {Kb_format}\n")

    # Finds pOH & pH
    pOH = -math.log(Kb, 10)
    pH = 14.00 - pOH

    conc_H = 10**-pH
    conc_OH = 10**-pOH

    conc_H = "{:e}".format(conc_H)
    conc_OH = "{:e}".format(conc_OH)


    print(f"pH = {pH}\n"
          f"pOH = {pOH}\n"
          f"[H] = {conc_H}\n"
          f"[OH] = {conc_OH}")

def find_weak_acid_kb(st_conc, pH):
    try:
        hydronium = round(10 ** (-float(pH)), 5)
        A = round(10 ** (-float(pH)), 5)
        HA = float(st_conc) - hydronium
        Ka = (hydronium * A) / HA
        Kb = Kw / Ka

    except ZeroDivisionError:
        print("The solution is a strong acid. Value is undefined.")
    else:
        """Format"""
        final = "{:e}".format(Kb)
        print(f"Ka = {final}")

def find_weak_base_kb(st_conc, pH):
    pOH = 14.00 - pH
    conc_OH = 10**-pOH

    Kb = (conc_OH**2/(st_conc-conc_OH))

    Kb = "{:e}".format(Kb)
    print(f"Kb = {Kb}")

def find_st_conc(pH, Ka):
    hydroxide = 10 ** -(14.00-pH)
    B = 10 ** -(14.00-pH)

    Kb = Kw / Ka

    st_conc = (hydroxide*B) / Kb

    final1 = "{:e}".format(st_conc)
    print(f"Starting Concentration = {final1}M\n")

    additional = input("Do you require mass of molecules in solution? (y/n)\n")

    if additional == 'y':
        molar_mass = float(input("What is the grams/moles? Give the grams: "))
        volume = float(input("How much of the solution is presented? (In litres): "))

        result = st_conc * volume * molar_mass

        print(f"\nMass of molecules present: {result}g")
    else:
        pass
