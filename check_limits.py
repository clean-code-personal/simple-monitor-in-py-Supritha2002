def checkRange(input,value,low,high):
    if value < low:
        attribute_status(input,'low')
        return False
    if value > high:
        attribute_status(input,'high')
        return False
    return True
def attribute_status(attribute,limit):
    german_lang={'Temperature':'Temperatur','SOC':'Ladezustand','Charge_rate':'Ladestrom','low':'niedrig','high':'hoch'}
    hindi_lang={'Temperature': 'तापमान','SOC':'चार्ज स्थिति','Charge_rate': 'चार्ज दर'}
    print(german_lang[attribute]," is ",german_lang[limit])
    
def battery_normal(result):
    german_status="Batterie ist in normalem Zustand"
    english_status="Battery in normal condition"
    if result==True:
        print(german_status)
def convertoCelcius(temperature,unit):
    return  temperature if unit == 'Celcius' else  (temperature - 32) * (5/9)

def battery_is_ok(temperature,tempunit,soc,charge_rate):
    temperature=convertoCelcius(temperature,tempunit)
    result=checkRange('Temperature',temperature,0,45) and checkRange('SOC',soc,20,80) and checkRange('Charge_rate',charge_rate,0,0.8)
    battery_normal(result)
    return result
