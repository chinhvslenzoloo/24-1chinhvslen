#daalgawar 1,
def greedy_coin_change(amount):
    coins = [25, 10, 5, 1]  
    coin_count = {}         

    for coin in coins:
        count = amount // coin  
        if count > 0:
            coin_count[coin] = count 
            amount -= coin * count      

    return coin_count


amount = 67
result = greedy_coin_change(amount)
print(result)