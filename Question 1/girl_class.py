class girl:
    def __init__(self,name_girl,attraction_girl,required_budget,brain_level_girl):
        'girl_class\' constructor'
        self.name_girl = name_girl
        self.required_budget = required_budget

        self.attraction_girl = attraction_girl

        'in starting she is single'
        self.status_girl = 'single'
        self.brain_level_girl = brain_level_girl
        'because she is single so there is no boyfriend name'
        self.name_boyfriend = ''

    'checking weather is permitted or not'
    def suitable(self,budget_for_girlfriend):
        if(self.required_budget <= budget_for_girlfriend ) and self.status_girl == 'single':
            return True
        else:
            return False
