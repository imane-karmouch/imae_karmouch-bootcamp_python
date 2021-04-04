from recipe import recipe
class book:
  name=' '
  last_update=0
  creation_date=0
  recipes_list={"starter":[],
                "lunch":[],
                "dessert":[],
               }
  def __init__(self,n,u,d,recipes):
    self.name=n
    self.last_update=u
    self.creation_date=d
    self.recipes_list=resipes
    def __str__(self):
      txt=''
      txt+=self.name+','+str(self.last_update)+','+str(self.creation_date)+','+self.recipes_list
      return txt
    
    
    
  def get_recipe_by_name(self, name):
    """Print a recipe with the name `name` and return the instance"""
    pass
    
   
  def get_recipes_by_types(self, recipe_type):
    """Get all recipe names for a given recipe_type """
    pass
    
    
  

  def add_recipe(self, recipe):
    """Add a recipe to the book and update last_update"""
    pass
   
    
