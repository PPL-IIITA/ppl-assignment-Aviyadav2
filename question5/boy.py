class boy:
     def __init__(self,name_boy,attraction_boy,budget_for_girlfriend,intelligence,minimum_attraction_required,type_boy):
          self.name_boy = name_boy
          self.attraction_boy = attraction_boy
          self.budget_for_girlfriend = budget_for_girlfriend
          self.girlfriend_name = ''
          self.happiness = 0
          self.type_boy = type_boy
          self.minimum_attraction_required = minimum_attraction_required
          self.intelligence = intelligence
          self.r_s = 'single'

     def set_hn(self,happiness):
          self.happiness = happiness
     def set_gf(self,girlfriend_name):
          self.girlfriend_name = girlfriend_name

     def change_bud_for_gf(self,budget_for_girlfriend):
          self.budget_for_girlfrind = budget_for_girlfriend

     def chk_elg(self,maintenance_budget_girl,attraction_girl):
           if(self.budget_for_girlfriend >= maintenance_budget_girl) and(attraction_girl >= self.minimum_attraction_required):
                return True
           else:
               return False
