#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    batch = []
    for i in recipe:
        for j in ingredients:
            if len(recipe) > len(ingredients):
                return 0  # missing ingredient
            if i == j and ingredients[j] < recipe[i]:
                return 0  # not enough ingredient
            if i == j and ingredients[j] > recipe[i] and len(recipe) == 1:
                return ingredients[j] // recipe[i]  # 0nly one recipe key
            if i == j:
                batch.append(ingredients[j] // recipe[i])
    for i in range(0, len(batch)-1):
        if batch[i] <= batch[i+1]:
            return batch[i]


if __name__ == '__main__':
        # Change the entries of these dictionaries to test
        # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 5}
    ingredients = {'milk': 132, 'butter': 48, 'flour': 51}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
