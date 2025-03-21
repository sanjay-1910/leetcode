class Solution:
    def can_make_a_recipe(self, i, recipes, final, supplies_dic, ingredients, visited):
        if recipes[i] in visited:
            return False  # Cycle detected
        visited.add(recipes[i])
        
        for ing in ingredients[i]:
            if ing in supplies_dic.keys():
                continue
            elif ing in recipes:
                if self.can_make_a_recipe(recipes.index(ing), recipes, final, supplies_dic, ingredients, visited):
                    continue
                else:
                    return False
            else:
                return False
        
        visited.remove(recipes[i])
        return True

    def findAllRecipes(self, recipes, ingredients, supplies):
        final = []
        supplies_dic = {sup: 0 for sup in supplies}
        
        for i in range(len(recipes)):
            visited = set()
            if self.can_make_a_recipe(i, recipes, final, supplies_dic, ingredients, visited):
                final.append(recipes[i])
                supplies_dic[recipes[i]] = 1
        
        return final
