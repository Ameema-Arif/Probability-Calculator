import copy
import random

class Hat:
    def __init__(self, **balls):
        self.balls = balls
        self.contents = []

        for color, number in self.balls.items():
            for ball in range(number):
                self.contents.append(color)

    def draw(self, drawballs):
        randomBalls = []
        randball = ""
        
        if drawballs > len(self.contents):
            return self.contents

        else:
            for count in range(drawballs):
                randball = random.choice(self.contents)
                randomBalls.append(randball)
                self.contents.remove(randball)
                
            return randomBalls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    balls = copy.copy(hat.contents)
    successful_exp = 0

    if num_balls_drawn > len(balls):
        probability = float(1)

    else:   
        for i in range(num_experiments):
            drawn_balls = random.sample(balls, num_balls_drawn)
            count = 0
            for color, number in expected_balls.items():
                if drawn_balls.count(color) >= number:
                    count += 1
                else:
                    count -= 1

            if count == len(expected_balls):
                successful_exp += 1

        probability = successful_exp / num_experiments

    return probability
        


                
                

        
            

