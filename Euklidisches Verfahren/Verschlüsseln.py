M = int(input("Definiere die zu verschlüsselnden Zahlen M. Wähle M nicht zu groß! (M < n): "))
def primzahltest(primzahltestzahl):
    if primzahltestzahl <= 1:
        return False
    if primzahltestzahl <= 3:
        return True

    i = 2
    while i * i <= primzahltestzahl:
        if primzahltestzahl % i == 0:
            return False
        i += 1
    return True


p = int(input("Gib p ein (beliebige Primzahl; p =! q): "))
q = int(input("Gib q ein (beliebige Primzahl; q =! p): "))

print("M = ", M)

print("p =", p)
print("q =", q)

if q == p:
    print("p und q dürfen nicht gleich sein!")
    exit()
else:
    if primzahltest(p) and primzahltest(q):
        print(f"Die Zahlen p ({p}) und q ({q}) sind nicht identisch und beides Primzahlen. Sehr gut!")
    else:
        print("Beide Zahlen müssen Primzahlen sein!")
        exit()

n = p * q

print("n =", n)

if n <= M:
    print("n muss größer als M sein!")
    exit()
else:
    print("Sehr gut: n > M")

phi_n = (p - 1) * (q - 1)

print("phi_n =", phi_n)

# Primfaktorzerlegung phi_n

def primfaktorzerlegung(primfaktorlegungszahl):
    primfaktoren = []
    divisor = 2

    while primfaktorlegungszahl > 1:
        while primfaktorlegungszahl % divisor == 0:
            primfaktoren += [divisor]
            primfaktorlegungszahl //= divisor
        divisor += 1

    return primfaktoren

primfaktorzerlegung_phi_n = primfaktorzerlegung(phi_n)

print("Primfaktorzerlegung von phi_n: ", primfaktorzerlegung_phi_n)

def finde_primzahlen(start, ende, max_beispiele):
    primzahlen = []
    for zahl in range(start, ende):
        if primzahltest(zahl):
            if zahl not in primfaktorzerlegung_phi_n:
                primzahlen.append(zahl)
            if len(primzahlen) == max_beispiele:
                break
    return primzahlen

max_beispiele = 50
mögliche_e_schritt_1 = finde_primzahlen(2, phi_n, max_beispiele)
print("Mögliche Werte für e:", mögliche_e_schritt_1)

if not mögliche_e_schritt_1:
    print("Keine möglichen Werte für e gefunden.")
else:
    mögliche_e_schritt_1_2_3 = mögliche_e_schritt_1.copy()

    mögliche_e_schritt_1_2_3 = [zahl for zahl in mögliche_e_schritt_1_2_3 if zahl not in primfaktorzerlegung_phi_n]

    if not mögliche_e_schritt_1_2_3:
        print("Keine möglichen Werte für e nach Schritt 1_2_3 gefunden. Suche nach weiteren.")
        weitere_mögliche_e = finde_primzahlen(phi_n + 1, phi_n * 2, max_beispiele)
        print("Zusätzliche mögliche Werte für e:", weitere_mögliche_e)


e = int(input("Wähle eine Zahl für e aus den obigen Optionen: "))

if e in mögliche_e_schritt_1_2_3:
    print("e wurde richtig gewählt.")
else:
    print("e wurde falsch gewählt.")
    exit()

print("e = ",e)

# Bestimmen von d: 0 < d < phi_n; d ist das multiplikative Inverse von e (mod phi_n)

def erweiterter_euklid(a, b):
    if b == 0:
        return a, 1, 0
    else:
        ggT, x, y = erweiterter_euklid(b, a % b)
        return ggT, y, x - (a // b) * y

def multiplikatives_inverse(e, phi_n):
    ggT, inv, _ = erweiterter_euklid(e, phi_n)
    if ggT != 1:
        raise ValueError("Das multiplikative Inverse existiert nicht, da {} und {} nicht teilerfremd sind.".format(e, phi_n))
    else:
        return inv % phi_n


try:
    inverse = multiplikatives_inverse(e, phi_n)
    print("Das multiplikative Inverse von {} modulo {} ist: {}".format(e, phi_n, inverse))
except ValueError as e:
    print(e)

d = inverse

print()
print()

print("Die zu verschlüsselnde Zahl M =", M)
print("Die 1. Primzahl q =", q)
print("Die 2. Primzahl p =", p)
print("Der 1. Teil beider Schlüssel n =", n)
print("Die Eulersche-Phi-Funktion von n, phi_n =", phi_n)
print("Die ausgewählte Zahl für den öffentlichen Schlüssel e =", e)
print("Der ausgerechnete private Schlüssel d =", d)

print()
print()

C = (M ** e) % n
M_2 = (C ** d) % n

print("Chiffrierte Nachricht:", C)
print("Dechiffrierte Nachricht:", M_2)
print("Ehemalige Nachricht:", M)

print()

if M_2 == M:
    print("Das Script hat erfolgreich funktioniert.")
else:
    print("Fehler...")

