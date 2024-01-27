C = int(input("Gib die verschlüsselte Nachricht C ein: "))
d = int(input("Gib den privaten Schlüssel d ein: "))
n = int(input("Gib den 2. Schlüsselteil n ein: "))

M = pow(C, d, n)
#pow = pow(basis, exponent, mod | unter Berücksichtigung der Modularen Arithmetik)

print("Die entschlüsselte Nachricht M ist:", M)
