class Rewards:
    def __init__(self):
        pass
        
    def calculate_reward(self, category):
        reward = 0
        if category == "Clothing":
            reward = 10 
        elif category == "Furniture":
            reward = 15
        elif category == "Kitchenware":
            reward = 5
        else:
            reward = 2
        return reward
    
    def calculate_total_reward(self, items):
        total_reward = 0
        for item in items:
            total_reward += self.calculate_reward(item.category) 
        return total_reward
    
    def get_reward_for_items(self, items):
        return self.calculate_total_reward(items) 

class Reward:
    def __init__(self, name, category):
        self.name = name
        self.category = category
