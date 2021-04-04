
dic= {"key 1":"value 1",
      "key b":"value b"}
#print the keys:
for key in dic:
    print (key)
#print the values:
for key in dic:
    print (dic[key])
#print keys and values
for key in dic.items():
    print(key,dic[key])

cookbook={
        "sandwich":{"ingredients" : ["ham","bread","tomatoes","cheese"],
                    "time" : "10 min",  
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
  print("take",cookbook[recipename]["time"],"of cooking")
  
def delrecipe(recipename):
  if recipename in cookbook:
    del cookbook[recipename]
    
def addrecipe(recipename,i,c,t):
      new_recipe={"ingredients":[],
                  "time":" ",
                  "type":" "},
      nex_recipe["ingredients"].append(i)
      new_recipe["time"]=recipe["time"]+c
      new_recipe["type"]=recipe["type"]+t
      cookbook[recipename]=nex_recipe
      
def prt():
      print(cookbook.items())
      print("1: Add a recipe","2: Delete a recipe ","3: Print a recipe","4: Print the cookbook","5: Quit",sep='\n')
      option = int(input())
      if option == 1:
            new=input("your recipe name")
            i=input()
            c=input()
            t=input()
            new=addrecipe(recipename,i,c,t)
      elif option==2:
            recipename=input("the recipe you want to delete")
            delrecipe(recipename)
      elif option==3:
            recipename=input("print the recipe")
            print_recipe(recipename)
      elif option==4:
            prt()
      elif option==5:
            print("Cookbook closed.")

        
      

      
       

      

      
  
  
    
    
    
    
    
    
    
