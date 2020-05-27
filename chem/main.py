import math
import ka_calculations
import kb_calculations
import titrations

while True:
      response = input("\n1: Calculations involving Ka (Weak Acid)\n"
                       "2: Calculations involving Kb (Weak Base)\n"
                       "3: Titrations\n"
                       "q: Quit\n")

      # Calculations involving Ka
      if response == '1':
            while True:
                  """User Interface"""
                  print("\nWhat do you need to find?\n"
                        "1: Ka\n"
                        "2: pH & [H3O]\n"
                        "3: Concentration & Mass\n"
                        "q: Return to Main Menu"
                        )
                  response = input()

                  if response == '1':
                        pH = input('What is the pH?\n')
                        st_conc = input('What is the concentration?\n')
                        ka_calculations.find_ka(pH, st_conc)

                  elif response == '2':
                        st_conc = input('What is the concentration?\n')
                        Ka1 = float(input("What is the base digits of Ka?\n"))
                        Ka2 = float(input("To the power of?\n"))
                        Ka = Ka1 * 10**Ka2
                        ka_calculations.find_pH(st_conc, Ka)

                  elif response == '3':
                        pH = float(input('What is the pH?\n'))
                        Ka1 = float(input("What are the base digits of Ka?\n"))
                        Ka2 = float(input("To the power of?\n"))
                        Ka = Ka1 * 10 ** Ka2
                        ka_calculations.find_st_conc(pH, Ka)

                  elif response == 'q':
                        break

                  else:
                        print("Please enter a valid instruction.")


      # Calculations involving Kb
      elif response == '2':
            while True:
                  """User Interface"""
                  print("\nWhat do you need to find?\n"
                        "1: pH & pOH + Concentrations\n"
                        "2: Weak Acid Kb\n"
                        "3: Weak Base Kb\n"
                        "4: Concentration & Mass\n"
                        "q: Return to Main Menu"
                        )
                  response = input()

                  if response == '1':
                        st_conc = float(input('What is the concentration?\n'))
                        Ka1 = float(input("What is the base digits of Ka?\n"))
                        Ka2 = float(input("To the power of?\n"))
                        Ka = Ka1 * 10 ** Ka2
                        kb_calculations.find_pH(st_conc, Ka)

                  elif response == '2':
                        st_conc = float(input('What is the concentration?\n'))
                        pH = float(input("What is the pH? (pH = 14.00 - pOH)\n"))
                        kb_calculations.find_weak_acid_kb(st_conc, pH)

                  elif response == '3':
                        st_conc = float(input('What is the concentration?\n'))
                        pH = float(input("What is the pH? (pH = 14.00 - pOH)\n"))
                        kb_calculations.find_weak_base_kb(st_conc, pH)

                  elif response == '4':
                        pH = float(input("What is the pH? (pOH will be calculated)\n"))
                        Ka1 = float(input("What is the base digits of Ka?\n"))
                        Ka2 = float(input("To the power of?\n"))
                        Ka = Ka1 * 10 ** Ka2
                        kb_calculations.find_st_conc(pH, Ka)

                  elif response == 'q':
                        break

      # Calculations involving titrations
      elif response == '3':
            titrations.titrate()

      elif response == 'q':
            break

