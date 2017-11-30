def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if city == 'Charlotte':
        return 183
    elif city == 'Tampa':
        return 220
    elif city == 'Pittsburg':
        return 222
    else:
        return 475

def rental_car_cost(days):
    cost = 40*days
    if days >= 7:
        return cost - 50
    elif days >= 3:
        return cost - 20
    else:
        return cost

def trip_cost(city, days, spending_money):
    return hotel_cost(days)+plane_ride_cost(city)+rental_car_cost(days)+spending_money

print(trip_cost('Pittsburg', 15, 800))
