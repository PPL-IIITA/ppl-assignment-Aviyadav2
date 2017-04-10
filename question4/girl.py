class girl:
     def __init__(self,name_girl,attraction_girl,maintence_budget_girl,intelligence,type_girl):
          self.name_girl = name_girl
          self.boyfriend_name = ''
          self.happiness = 0
          self.type_girl = type_girl
          self.attraction_girl = attraction_girl
          self.maintence_budget_girl = maintence_budget_girl
          self.intelligence = intelligence
          self.r_s = 'single'

     def set_hn(self,happiness):
          self.happiness = happiness

     def set_bf(self,boyfriend):
          self.boyfriend_name = boyfriend

     def change_main_bud(self,mainte):
          self.maintence_budget_girl = budget

     def chk_elg(self,budget_for_girlfriend):
          if(self.maintence_budget_girl <= budget_for_girlfriend):
               return True
          else:
               return False
