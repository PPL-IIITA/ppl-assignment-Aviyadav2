class couple:
     def __init__(self,name_girl,name_boy):
          self.name_boy = name_boy
          self.name_girl = name_girl
          self.joy_level = 0
          self.gft = []
          self.compatibility_level_couple = 0
          


     def count_happiness(self):
          self.joy_level = self.name_girl.joy_level_girl + self.name_boy.joy_level_boy

     def calculate_compatibility(self):
          budget_compatibility = self.name_boy.budget_for_girlfriend - self.name_girl.required_budget

          brain_compatibility  = abs(self.name_boy.intelligence_level_boy - self.name_girl.brain_level_girl)

          attraction_compatibility = abs(self.name_boy.attraction_boy - self.name_girl.attraction_girl)

          self.compatibility_level_couple = attraction_compatibility + brain_compatibility + budget_compatibility
