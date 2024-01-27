C = int(input("Gib die verschlüsselte Nachricht C ein: "))
d = int(input("Gib den privaten Schlüssel d ein: "))
n = int(input("Gib den 2. Schlüsselteil n ein: "))

M = (C ** d) % n

print("Die entschlüsselte Nachricht M ist:", M)


