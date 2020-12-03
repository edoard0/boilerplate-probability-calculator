import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self,**kwargs):
        self.contents=[]
        for color,number in kwargs.items():
            for i in range(number):
                self.contents.append(str(color))
    
    def get_contents(self):
        return self.contents
    
    def draw(self,n):
      if n>len(self.contents):
        return self.contents
            
      self.sample=[]
    
      for i in range(n):
        single_draw=random.choice(self.contents)
        self.sample.append(single_draw)
        index=self.contents.index(single_draw)
        self.contents.pop(index)
    
      return self.sample



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
        
    probability_counter=0  
    
    for experiment in range(num_experiments):
        
        hat_=copy.deepcopy(hat)
        sample_list=hat_.draw(num_balls_drawn)
        
        sample_dict = {color: sample_list.count(color) for color in set(sample_list)}
        
        match=True
        
        for color,value in expected_balls.items():
            if (color in sample_dict) and (expected_balls[color]<=sample_dict[color]):
                continue
            else:
                match=False
                
        if match:
            probability_counter+=1  
    
    
    return probability_counter/num_experiments

