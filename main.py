def deposit():
    while True:
        amount = input("Vad skulle du vilja sätta in? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Beloppet måste vara större än 0.")
        else: