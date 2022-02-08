'''
author =
'''
TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

seznam_uzivatelu = {'bob': '123', 'ann': 'pass123', 'mike': 'password123', 'liz': 'pass123'}

jmeno_uzivatele = input('Zadej své jméno:')
heslo_uzivatele = input('Zadej své heslo:')

print("-"*80)

if seznam_uzivatelu.get(jmeno_uzivatele) == heslo_uzivatele:
    print(f'Vítej, {jmeno_uzivatele}.')
    print(f'Máme 3 různé texty k analýze.')
    print("-" * 80)
    vyber_textu = input('Vyber si číslo mezi 1 a 3:')
    if not vyber_textu.isnumeric() or int(vyber_textu) not in range(1, 4):
        print(f'Nevybral jsi číslo mezi 1 a 3. Ukončuji program.')
    else:
        print("-" * 80)

        # Rozdělím text na jednotlivá slova a odstraním znaky .:;,

        vycistena_slova = []

        for slovo in list(TEXTS[int(vyber_textu) - 1].split()):
            vycistena_slova.append(slovo.strip(".:;,"))

        # počet slov

        pocet_slov = len(vycistena_slova)

        print(f"Počet slov (včetně čísel a kombinací písmen a čísel) v textu celkem je: {pocet_slov}")

        # počet slov začínajících velkým písmenem

        pocet_slov_zac_velkym_pismenem = 0

        for slovo in vycistena_slova:
            if slovo.istitle():
                pocet_slov_zac_velkym_pismenem += 1

        print(f"Počet slov začínajících velkým písmenem (čísla ve slovech ignorujeme) je: {pocet_slov_zac_velkym_pismenem}")

        # počet slov psaných velkými písmeny

        pocet_slov_psanych_velkymi_pismeny = 0

        for slovo in vycistena_slova:
            if slovo.isupper():
                pocet_slov_psanych_velkymi_pismeny += 1

        print(f"Počet slov psaných velkými písmeny (čísla ve slovech ignorujeme) je: {pocet_slov_psanych_velkymi_pismeny}")

        # počet slov psaných malými písmeny

        pocet_slov_psanych_malymi_pismeny = 0

        for slovo in vycistena_slova:
            if slovo.islower():
                pocet_slov_psanych_malymi_pismeny += 1

        print(f"Počet slov psaných malými písmeny (čísla ve slovech ignorujeme) je: {pocet_slov_psanych_malymi_pismeny}")

        # počet čísel (ne cifer)

        pocet_cisel = 0

        for slovo in vycistena_slova:
            if slovo.isdigit():
                pocet_cisel += 1

        print(f"Počet čísel (ne cifer) je: {pocet_cisel}")

        # sumu všech čísel (ne cifer) v textu

        suma_cisel = 0

        for slovo in vycistena_slova:
            if slovo.isdigit():
                suma_cisel += int(slovo)

        print(f"Suma čísel (ne cifer) je: {suma_cisel}")

        # sloupcový graf, který bude reprezentovat četnost různých délek slov v textu

        delky_slov = dict()

        for slovo in vycistena_slova:
            if len(slovo) not in delky_slov:
                delky_slov[len(slovo)] = 1
            else:
                delky_slov[len(slovo)] += 1

        print("-" * 80)
        print(f"Délka| Případy           | Počet")
        print("-" * 80)

        for delka in sorted(delky_slov):
            print(f"{delka:>4} | {'*' * delky_slov[delka]:<17} | {delky_slov[delka]}")


else:
    print(f'Neregistrovaný uživatel, ukončuji program.')