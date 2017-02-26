class boy:
     def __init__(self,name_boy,attraction_boy,budget_for_girlfriend,intelligence_level_boy,minimum_attraction_required,boy_type):
          self.name_boy = name_boy
          self.attraction_boy = attraction_boy
          self.budget_for_girlfriend = budget_for_girlfriend

          'boy\'s intelligence level'
          self.intelligence_level_boy = intelligence_level_boy

          'minimum attraction'
          self.minimum_attraction_required = minimum_attraction_required
 
          'in starting we are going to assume that every boy is single'
          self.status_boy = 'single'

          'because in starting boy is single so his girlfriend name must be empty'
          self.name_girlfriend = ''
          self.joy_level_boy = 0
          self.boy_type = boy_type



     def suitable(self,required_budget,attraction_girl):
          
          
          if(self.budget_for_girlfriend >= required_budget) and (attraction_girl >= self.minimum_attraction_required) and self.status_boy == 'single':
               
                
               'If for a given girl boy is meeting all minimum criteria then he is permitted for having a relationship with girl otherwise not'
               return True
          
          else:
               
               'If boy is not meeting all the requirements he is not qualified or suitable '
               return False
                


        
