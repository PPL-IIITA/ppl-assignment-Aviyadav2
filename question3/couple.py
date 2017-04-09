class couple:
     def __init__(self,boy,girl):
          self.happiness  = 0
          self.girl = girl
          self.boy = boy
          self.gift = []
          self.comp_status = 0

     def set_comp(self):
          x = self.boy.budget_for_girlfriend - self.girl.maintence_budget_girl
          y = abs(self.boy.attraction_boy - self.girl.attraction_girl)
          z = abs(self.boy.intelligence - self.girl.intelligence)
          self.compatibility_status = x+y+z

     def set_hn(self):
          self.happiness  = self.boy.happiness+self.girl.happiness
