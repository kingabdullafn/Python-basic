def hotel_cost(night):
    return 1500*night
    
def plane_ride_cost(city):
    if "Bangladesh"==city:
        return 1000000000000000000
    elif "Riyadh" == city:
        return 1500
    elif "Twin towers" == city:
        return 911

def rental_car_cost(days):
    if days>=7 :
        return 40*days - 50
    elif days>=3 :
         return 40*days - 20
    else:
        return 40*days
        
def trip_cost(city,  days, spending_money ):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city)+spending_money
    
print("Cost of car rental: ", rental_car_cost(6))
print("Cost of plane ride:", plane_ride_cost("Bangledesh"))
print("Cost of the hotel room", hotel_cost(7))
print("Total cost of the trip", trip_cost ("Bangladesh",7,500))
