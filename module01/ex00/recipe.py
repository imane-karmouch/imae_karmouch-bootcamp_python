
class recipe:
    name=" "
    cooking_lvl=0
    cooking_time=0
    ingredients=[]
    description=" "
    recipe_type=" "
    def __init__(self,n,level,time,ing,desc,typ):
      self.name=n
      self.cooking_lvl=level
      self.cooking_time=time
      self.ingredients=ing
      self.description=desc
      self.recipe_type=typ
      def __str__(self):
        txt=' '
        txt+=self.name+','+str(self.cooking_lvl)+','+str(cooking_time)+','+str(ingredients)+','+self.description+','+recipe_type
        return txt
