balance = 10500
camera_on = True

def steal(balance, amount):
    camera_on = False
    if (amount < balance):
        balance = balance - amount
    
    return amount
    camera_on = True

proceeds = steal(balance, 1250)
print('Criminal: you stole', proceeds)
