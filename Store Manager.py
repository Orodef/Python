prices = {
    "banana" : 4,
    "apple"  : 2,
    "orange" : 1.5,
    "pear"   : 3,
}
stock = {
    "banana" : 6,
    "apple"  : 0,
    "orange" : 32,
    "pear"   : 15,
}

for key in prices:
    print (key)
    print ("price: %s" % prices[key])
    print ("stock: %s" % stock[key])
    
income = 0
total = 0
for key in prices:
    income = stock[key] * prices[key]
    print (key)
    print ("The total income with the current stock and prices %s will be %s" % key, income)
    

# Need to introduce values first to use this part!!
def compute_bill(food):
    total = 0
    for items in food:
        if stock[items] > 0:
            total += prices[items]
            stock[items] = stock[items] - 1
    return total
