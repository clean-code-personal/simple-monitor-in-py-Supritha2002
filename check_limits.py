from check_limits_battery_status import *
def checkRange(input,value,low,high):
    if value < low:
        attribute_status(input,'low')
        return False
    if value > high:
        attribute_status(input,'high')
        return False
    return True
def battery_is_ok(temperature,soc,charge_rate):
    result=checkRange('Temperature',temperature,0,45) and checkRange('SOC',soc,20,80) and checkRange('Charge_rate',charge_rate,0,0.8)
    battery_normal(result)
    return result
