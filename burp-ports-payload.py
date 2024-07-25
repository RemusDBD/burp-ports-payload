# Python script to generate a list of ports from 1 to 65535
with open('ports.txt', 'w') as file:
    for port in range(1, 65536):
        file.write(f"{port}\n")
