def checkRange(input,value,low,high):
    if value < low:
        print("Attribute ", input," is low")
        return False
    if value > high:
        print("Attribute ", input," is high")
        return False
    return True

def battery_is_ok(temperature,soc,charge_rate):
    result=checkRange('Temperature',temperature,0,45) and checkRange('SOC',soc,20,80) and checkRange('Charge_Rate',charge_rate,0,0.8)
    if result ==True:
        print("Battery is in normal condition")
    return result
