# Get Chicken recipes
from bs4 import BeautifulSoup
import requests
import pandas as pd

recipes_page = "https://www.allrecipes.com/recipes/201/meat-and-poultry/chicken/"

response = requests.get(recipes_page)
recipes_data = response.text
soup = BeautifulSoup(recipes_data, "html.parser")

all_recipe_names = [title.getText().strip() for title in soup.findAll('h3',class_= 'card__title elementFont__resetHeading')]
all_recipe_links = [a['href'] for a in soup.findAll('a',class_='card__titleLink manual-link-behavior elementFont__titleLink margin-8-bottom')]
all_recipe_desc = [title.getText().strip() for title in soup.findAll('div',class_= 'card__summary elementFont__details--paragraphWithin margin-8-tb')]

outfile = {
    'recipe name': all_recipe_names,
    'recipe description': all_recipe_desc,
    'recipe link': all_recipe_links
}
dataframe = pd.DataFrame(outfile)
dataframe.to_csv('chicken_recipe_list.csv')