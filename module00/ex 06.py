
dic= {"key 1":"value 1",
      "key b":"value b"}
#print the keys:
for key in dic:
    print (dic.key)
#print the values:
for value in dic.values():
    print (dic.value)
#print keys and values
for key, value in dic.items():
    print(key,value)

cookbook={
        "sandwich":{"ingredients" : ["ham","bread","tomatoes","cheese"],
                    "time of cooking" : "10 min",  
                    "type":"lunch meal"},   
        "cake":{"ingredients":["floor","eggs","sugar"],
                "time":"60 min",
                "type":"desert"},
        "salad":{"ingredients":["avocado","arogula","tomatoes","spinach"],
                 "time":"20min",
                 "type":"lunch"},
}
def print_recipe(recipename):
  print("recipe for a",recipename)
  print("Ingredients list:",cookbook[recipename]["ingredients"])
  print("to be eaten for",cookbook[recipename]["type"])
  print("take",cookbook[recipename]["time of cooking"],"of cooking")
  
 def delrecipe(recipename):
  if recipename in cookbook:
    del cookbook[recipename]
    
 def addrecipe(recipename,ingredients,time_of_cooking,type):
  
  
    
    
    
    
    
    
    
