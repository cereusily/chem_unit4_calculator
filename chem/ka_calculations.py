import math

# KA
def find_ka(pH, st_conc):
      """Calculates for Ka"""
      try:
            hydronium = round(10 ** (-float(pH)), 5)
            A = round(10 ** (-float(pH)), 5)
            HA = float(st_conc) - hydronium
            Ka = (hydronium * A) / HA
      except ZeroDivisionError:
            print("The solution is a strong acid. Value is undefined.")
      else:
            """Format"""
            final = "{:e}".format(Ka)
            print(f"Ka = {final}")
            return final


def find_pH(st_conc, Ka):
      """Calculates for pH"""
      HA = float(st_conc)
      Ka = Ka

      hydronium = math.sqrt((HA)*(Ka))

      final1 = "{:e}".format(hydronium)
      print(f"[H3O] = {final1}")

      pH = -math.log(hydronium, 10)
      print(f"pH = {pH}")

def find_st_conc(pH, Ka):
      hydronium = 10**-pH
      A = 10**-pH

      st_conc = (hydronium*A)/Ka

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