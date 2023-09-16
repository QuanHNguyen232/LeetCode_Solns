class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        graph = defaultdict(list)
        in_degree = defaultdict(int)
        
        # init
        for i, recipe in enumerate(recipes):
            for ingredient in ingredients[i]:
                in_degree[recipe]+=1
                graph[ingredient].append(recipe)
        
        # add all the supplies to the supply queue
        supply_queue = deque(supplies)
        possible_recipes = []
       
        while supply_queue:
            supply = supply_queue.popleft()
            recipe_list = graph[supply]
            
            for recipe in recipe_list:
                in_degree[recipe] -= 1
                if in_degree[recipe] == 0:
                    supply_queue.append(recipe)
                    possible_recipes.append(recipe)
        
        return possible_recipes

# CodePath W7 sess1 soln
