
# coding: utf-8

# In[ ]:

import requests
import json

def get_cocktail():
    #gets json from cocktaildb api
    url = requests.get('http://www.thecocktaildb.com/api/json/v1/1/random.php')
    cocktail_json = url.json()
    urllib.request.urlretrieve(cocktail_json['drinks'][0]['strDrinkThumb'], 'image.jpg')
    #writes cocktail to file
    with open('cocktail.txt', 'w') as outfile:
        json.dump(cocktail_json, outfile)

def print_cocktail():
    try:    
        with open('cocktail.txt') as datafile:
            cocktail_json = json.load(datafile)
        ingredients = {}
        for count in range(1,15):
            if cocktail_json['drinks'][0]['strIngredient'+str(count)] is not None and cocktail_json['drinks'][0]['strIngredient'+str(count)] != "":
                # pulls together quant and ingredient as string 
                ingredients['Ingredient_'+str(count)] = cocktail_json['drinks'][0]['strMeasure'+str(count)].strip()+ " " + cocktail_json['drinks'][0]['strIngredient'+str(count)].strip() 
            else:
                break
        message = "Your daily cocktail is the " + cocktail_json['drinks'][0]['strDrink'] + '\n'
        #print all ingredients
        for ing in ingredients.values():
            message += ing + '\n'
        message += cocktail_json['drinks'][0]['strInstructions']
        return message
    except FileNotFoundException as err:
        return err
    

