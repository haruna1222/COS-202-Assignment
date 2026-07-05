print("=" * 55)
print("        BASIC MATH CALCULATOR")
print("=" * 55)

running = True

while running:

    print("\nAVAILABLE OPERATIONS")
    print("[+] Addition")
    print("[-] Subtraction")
    print("[*] Multiplication")
    print("[/] Division")
    print("[\\] Floor Division")
    print("[^] Exponent")
    print("[%] Modulus")
    print("[C] Clear")
    print("[OFF] Quit")

    operator = input("\nSelect Operation: ").upper()

    match operator:

        case "OFF":
            print("\nThank you for using the calculator.")
            running = False

        case "C":
            print("\nCalculator has been cleared.")

        case "+" | "-" | "*" | "/" | "\\" | "^" | "%":

            num_a = float(input("Input First Number: "))
            num_b = float(input("Input Second Number: "))

            match operator:

                case "+":
                    answer = num_a + num_b

                case "-":
                    answer = num_a - num_b

                case "*":
                    answer = num_a * num_b

                case "/":
                    if num_b == 0:
                        print("Cannot divide by zero.")
                        continue
                    answer = num_a / num_b

                case "\\":
                    if num_b == 0:
                        print("Cannot divide by zero.")
                        continue
                    answer = num_a // num_b

                case "^":
                    answer = num_a ** num_b

                case "%":
                    if num_b == 0:
                        print("Cannot divide by zero.")
                        continue
                    answer = num_a % num_b

            print("\nFinal Answer =", answer)

        case _:
            print("\nInvalid Selection.")