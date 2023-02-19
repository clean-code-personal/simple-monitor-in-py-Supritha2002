def checkRange(input,value,low,high,lang):  #checks status of battery attribute
    if value < low:
        attribute_status(input,'low',lang)
        return False
    if value > high:
        attribute_status(input,'high',lang)
        return False
    return True

#extension2 -support multiple languages to print user messages
def attribute_status(attribute,limit,lang):
    language={
    'german':{'Temperature':'Temperatur',
              'SOC':'Ladezustand',
              'Charge_rate':'Ladestrom',
              'low':'niedrig',
              'high':'hoch'},
    'hindi':{'Temperature': 'तापमान',
             'SOC':'चार्ज स्थिति',
             'Charge_rate': 'चार्ज दर',
             'low':'कम',
             'high':'उच्च'
             },
    'english':{'Temperature':'Temperature',
               'SOC' : 'State Of Charge'  ,
               'Charge_rate': 'Charge Rate',
               'low':'low',
               'high':'high'
              }
    }
    print(language[lang][attribute]," is ",language[lang][limit])
    
def battery_normal(result,lang):
    status_language= {'german' :'Batterie ist in normalem Zustand',
                      'hindi'  :'सामान्य स्थिति में बैटरी'              ,
                      'english':'Battery in normal condition'    
                     }
    if result==True:
        print(status_language[lang])

        
def convertoCelcius(temperature,unit):  #extension3 - accepts temperature in different unit
    return  temperature if unit == 'Celcius' else  (temperature - 32) * (5/9)

def battery_is_ok(temperature,tempunit,soc,charge_rate,lang): #checks battery condition
    temperature=convertoCelcius(temperature,tempunit)
    result=checkRange('Temperature',temperature,0,45,lang) and checkRange('SOC',soc,20,80,lang) and checkRange('Charge_rate',charge_rate,0,0.8,lang)
    battery_normal(result,lang)
    return result
