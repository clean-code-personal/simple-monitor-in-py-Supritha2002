def checkRange(value,low,high):
    if value < low or value < high:
        print("Attribute ",value ," is not in range")
        return False
    return True

def battery_is_ok(temperature,soc,charge_rate):
    result=checkRange(temperature,0,45) and checkRange(soc,20,80) and checkRange(charge_rate,0,0.8)
    if result ==True:
        print("Battery is in normal condition")
    return result

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
