def checkRange(value,low,high):
    if value < low or value > high:
        return False
    return True

def battery_is_ok(temperature,soc,charge_rate):
    result=checkRange(temperature,0,45) and checkRange(soc,20,80) and checkRange(charge_rate,0,0.8)
    return result

