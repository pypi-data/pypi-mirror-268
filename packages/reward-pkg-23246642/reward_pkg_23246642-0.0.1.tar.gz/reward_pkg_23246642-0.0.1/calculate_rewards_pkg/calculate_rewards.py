class Rewards:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        
def calculate_reward(item):
    reward = 0
    if item.category == "Clothing":
        reward = 10 
    elif item.category == "Furniture":
        reward = 15
    elif item.category == "Kitchenware":
        reward = 5
    else:
        reward = 2
    return reward

def calculate_total_reward(items):
    total_reward = 0
    for item in items:
        total_reward = total_reward + calculate_reward(item)
    return total_reward

def get_reward_for_items(items):
    return calculate_total_reward(items)
