## THE SMART ATM WITHDRAWAL SIMULATOR

#1. Set a fixed variable representing a bank balannce, for example: balance = 500
balance = 500
#2. Ask the user how much money they want to with draw. (Remember to cast it to an integer or float)
withdrawal_amount = float(input("Enter withdrawal amount: R"))
#3. If the request is less than or equal to the balance, deduct the amount and print: "Withdrawal successful! Remaining balance: RX

if withdrawal_amount <= balance:
    balance = balance - withdrawal_amount
    print(f"Withdrawal successful! Remaining balance : R{balance:.2f}")
#4. But what if they try to withdraw a negative amount or zero? Add an elif statement checking if the request is less than or
#equal to 0. If so print: "Invalid amount". You must withdraw more than "R0"
elif withdrawal_amount <= 0:
    print("Invalid amount. You must withdraw more than R0")
#5. Otherwise (else), print "Declined. Insufficient funds"
else:
    print("Declined. Insufficient Funds")