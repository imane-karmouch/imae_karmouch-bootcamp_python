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
