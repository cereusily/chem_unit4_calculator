def reducefraction(n, d):
    '''Reduces fractions. n is the numerator and d the denominator.'''
    def gcd(n, d):
        while d != 0:
            t = d
            d = n%d
            n = t
        return n
    assert d!=0, "integer division by zero"
    assert isinstance(d, int), "must be int"
    assert isinstance(n, int), "must be int"
    greatest=gcd(n,d)
    n/=greatest
    d/=greatest
    return n, d

def titrate():
    while True:
        print("\n1: Titrating for missing concentration/volume\n"
              "2: Finding how many protons are removed\n"
              "3: Calculating percentage purity\n"
              "4: Determining Molar Mass\n"
              "q: Quit"
              )
        answer = input()

        if answer == '1':
            while True:
                # finds missing conc or volume
                print("Type in 'missing' for value that is missing. Type 'q' anytime to quit.")

                a = input("How many moles for substance 1 (main substance)? ")
                if a == 'q':
                    break
                b = input("How many moles for substance 2 (missing substance)? ")
                if b == 'q':
                    break
                sub_1_vol = input("What is the volume of substance 1(mL): ")
                if sub_1_vol == 'q':
                    break
                sub_1_conc = input("What is the concentration of substance 1: ")
                if sub_1_conc == 'q':
                    break
                sub_2_vol = input("What is the volume of substance 2(mL): ")
                if sub_2_vol == 'q':
                    break
                sub_2_conc = input("What is the concentration of substance 2: ")
                if sub_2_conc == 'q':
                    break

                try:
                    mm1 = float(sub_1_conc) * float(sub_1_vol)
                    mm2 = mm1 * (float(b)/float(a))

                except:
                    print("Sorry, there was an unexpected error.")

                else:
                    if sub_2_conc == 'missing':
                        c = mm2 / float(sub_2_vol)
                        print(f"\nConcentration of substance 2 = {c}M\n")

                    elif sub_2_vol == 'missing':
                        c = mm2 / float(sub_2_conc)
                        print(f"\nVolume of substance 2 = {c}mL\n")

        elif answer == '2':
            while True:
                print("Type in values for calculations. Type 'q' anytime to quit.")

                sub_1_vol = input("What is the volume of substance 1: ")
                if sub_1_vol == 'q':
                    break
                sub_1_conc = input("What is the concentration of substance 1: ")
                if sub_1_conc == 'q':
                    break
                sub_2_vol = input("What is the volume of substance 2: ")
                if sub_2_vol == 'q':
                    break
                sub_2_conc = input("What is the concentration of substance 2: ")
                if sub_2_conc == 'q':
                    break

                try:
                    sub_1_used = round(float(sub_1_conc) * float(sub_1_vol))
                    sub_2_used = round(float(sub_2_conc) * float(sub_2_vol))
                except:
                    print("\nSorry, we came across an unexpected issue.\n")
                else:
                    sub_1, sub_2 = reducefraction(sub_1_used, sub_2_used)
                    print(f"\nThe reaction will on average require {sub_1} protons removed from substance 1.\n")

        elif answer == '3':
            while True:
                print("Type in values for calculation. Type in 'q' to quit anytime.")

                second_mass = input("What is the mass of the solute?: ")
                if second_mass == 'q':
                    break
                second_vol = input("What is the volume of the sample?(mL): ")
                if second_vol == 'q':
                    break
                second_dilute_vol = input("What is the dilution volume of the solute?(mL): ")
                if second_dilute_vol == 'q':
                    break
                second_mm = input("What is the molar mass of the solute?: ")
                if second_mm == 'q':
                    break

                main_conc = input("What is the concentration of the solvent?: ")
                if main_conc == 'q':
                    break
                main_vol = input("What is the volume of the solvent?(mL): ")
                if main_conc == 'q':
                    break

                try:
                    main_moles = float(main_conc) * float(main_vol)
                    second_actual = main_moles / float(second_dilute_vol)
                    second_expected = (float(second_mass)/(float(second_vol)/1000)) * (1/float(second_mm))
                except:
                    print("Sorry, we ran into an unexpected error.")
                else:
                    purity = (second_actual / second_expected)*10000
                    print(f"\nPurity is {purity}%\n")

        elif answer == '4':
            while True:
                print("Enter in values for calculation. Press 'q' to quit anytime.")
                unknown_mass = input("What is the mass of the unknown sample?: ")
                if unknown_mass == 'q':
                    break
                unknown_dilute_vol = input("What is the diluted volume of the unknown sample?(mL): ")
                if unknown_dilute_vol == 'q':
                    break
                unknown_vol = input("What is the volume of the unknown sample?(mL): ")
                if unknown_vol == 'q':
                    break

                main_conc = input("What is the concentration of the solvent?: ")
                if main_conc == 'q':
                    break
                main_vol = input("What is the volume of the solvent?(mL): ")
                if main_vol == 'q':
                    break

                main_used = float(main_conc) * float(main_vol)

                unknown_conc = main_used/float(unknown_vol)

                unknown_moles = unknown_conc * (float(unknown_dilute_vol)/1000)

                unknown_mm = float(unknown_mass) / unknown_moles

                print(f"\nThe molar mass of the substance is {unknown_mm}g/mol\n")

        elif answer == 'q':
            break
