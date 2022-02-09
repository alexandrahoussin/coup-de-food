from pydoc import classname
import dash
from dash import dcc, html, callback_context
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.graph_objs as go
from app import app
from collections import Counter

#------------------- Items -----------------------------------
# food_dict = {'Chicken or Turkey' : 'chicken', 'Duck': 'duck', 'Pork':'pork', 'Lamb':'lamb',
#              'Beef or Venison': 'beef', 'Salad or Green Vegetables': 'green', 
#              'Root Vegetables or Squashes': 'root', 'Mushrooms': 'mush', 'Tomato-based dishes':'tomato',
#              'Chili or Spicy food':'spicy', 'White Fish':'white_fish', 'Meaty or Oily Fish':'oily',
#              'Shellfish, Crab or Lobster':'shellfish', "Goat's Cheese or feta":'feta',
#              'Manchego or Parmesan':'parmesan', 'Cheddar or Gruyere':'cheddar',
#              'Blue Cheese':'blue', 'Brie or Camembert':'brie', 'Fruit-based Dessert':'fruits',
#              'Chocolate or Caramel':'choco', 'Cakes or Cream':'cakes'}

food_dict = ['Chicken and Turkey', 'Duck', 'Pork', 'Lamb',
             'Beef and Venison', 'Salads and green vegetables', 
             'Root Vegetables and Squashes', 'Mushrooms', 'Tomato based dishes',
             'Spicy dishes', 'White fish', 'Meaty and Oily Fish',
             'Shellfish, Crab and Lobster', 'Goat cheese and feta',
             'Manchego and parmesan', 'Cheddar & gruyere',
             'Blue cheeses', 'Brie and Camembert', 'Fruit-based desserts',
             'Chocolate and Caramel', 'Cakes and cream']

flavors = ['Woody', 'Light and flavored','Fruity and sour','Classic and tannic', 'Spicy and intense', 
           'Flowery and vegetal', 'Tropical', 'Vanilla and complex']

# images_dict = {'chicken' : '../assets/food/chicken.jpg', 'duck': '../assets/food/chicken.jpg', 'pork':'../assets/food/chicken.jpg',
#                'lamb':'../assets/food/chicken.jpg','beef': '../assets/food/chicken.jpg', 
#                'green': '../assets/food/chicken.jpg', 'root': '../assets/food/chicken.jpg', 
#                'mush': '../assets/food/chicken.jpg', 'tomato':'../assets/food/chicken.jpg',
#              'spicy':'../assets/food/chicken.jpg', 'white_fish':'../assets/food/chicken.jpg', 
#              'oily':'../assets/food/chicken.jpg',
#              'shellfish':'../assets/food/chicken.jpg', "feta":'../assets/food/chicken.jpg',
#              'parmesan':'../assets/food/chicken.jpg', 'cheddar':'../assets/food/chicken.jpg',
#              'blue':'../assets/food/chicken.jpg', 'brie':'../assets/food/chicken.jpg', 
#              'fruits':'../assets/food/chicken.jpg',
#              'choco':'../assets/food/chicken.jpg', 'cakes':'../assets/food/chicken.jpg'}

images_dict = {'Chicken and Turkey' : '../assets/food/chicken.jpg', 'Duck': '../assets/food/duck.jpg', 'Pork':'../assets/food/pork.jpg',
               'Lamb':'../assets/food/lamb.jpg','Beef and Venison': '../assets/food/beef.jpg', 
               'Salads and green vegetables': '../assets/food/salad.jpg', 'Root Vegetables and Squashes': '../assets/food/rootvegetable.jpg', 
               'Mushrooms': '../assets/food/mushroom.jpg', 'Tomato based dishes':'../assets/food/tomato.jpg',
             'Spicy dishes':'../assets/food/spicy.png', 'White fish':'../assets/food/whitefish.jpeg', 
             'Meaty and Oily Fish':'../assets/food/oilyfish.jpg',
             'Shellfish, Crab and Lobster':'../assets/food/homar.jpg', 'Goat cheese and feta':'../assets/food/goatcheese.jpg',
             'Manchego and parmesan':'../assets/food/Parmesan.jpg', 'Cheddar & gruyere':'../assets/food/gruyere.jpg',
             'Blue cheeses':'../assets/food/bluecheese.jpg', 'Brie and Camembert':'../assets/food/brie.jpg', 
             'Fruit-based desserts':'../assets/food/fruit.jpg',
             'Chocolate and Caramel':'../assets/food/choco.jpg', 'Cakes and cream':'../assets/food/cake.jpg'}

df_food = pd.read_csv('food.csv', index_col = 0)
df_wine = pd.read_csv('wines.csv', index_col = 0)



def match(food, result):
    return html.Div([
                html.P("It's a Match !", className='match'),
                html.Div([
                    html.Div([html.Img(src=images_dict[food], className = 'food-img-result')], className='food-result'),
                    html.Div([html.P(f"{result}", className='wine-text-result')], className='wine-result'),
                    ], className='match-result'),
                ], className= 'Result')

def no_match(food, wine1, wine2, taste, x):
    return html.Div([
        html.P('This is not the perfect love...', className='oups'),
        html.P(f'With {food} I recommend {wine1} or {wine2}.', className='oups'),
        html.P(f"But if you like {taste} you can drink {x.most_common(10)[0][0]} or {x.most_common(10)[1][0]} !", className='oups'),
        ], className= 'error-result')

#------------------- Layout -----------------------------------
layout = html.Div([
    dbc.Row([
        html.Div([
            html.H2('Find the perfect match between food and wine'),
            ], className='reco-title'),
        
        ], className='reco-row1'),
    
    dbc.Row([
        dbc.Col([
            html.Div([
                html.Img(src='../assets/couple.jpg', className='reco-img'),
                ], className="img-cont")
            ], width=3, className='reco-img-col'),
        
        dbc.Col([
            html.Div([
                html.Div([
                html.H4("Tell me what you eat and love and I'll tell you what to drink.")
                ], className='filter-title'),
            
                html.Div([
                    html.Div([
                        html.P('Today, I want to eat :', className='filter-label'),
                        dcc.Dropdown(
                            id='eat-dropdown',
                            options = [
                                {'label': x, 'value': x} for x in food_dict
                                # {'label': x, 'value': z} for x, z in food_dict.items()
                            ],
                            placeholder= 'Food, Food, Food !'
                            ),
                        ], className='eat'),
                    
                    html.Div([
                        html.P('What kind of wine I love:', className='filter-label'),
                        dcc.Dropdown(
                            id='taste-dropdown',
                            options = [
                                {'label': x, 'value': x} for x in flavors
                            ],
                            placeholder= 'Love, Love, Love !'
                            ),
                        ], className='taste'),
                    
                    ], className="filter-cont"),
                
                html.Div([
                    dbc.Button('MATCH !', id='match-btn'),
                    ], className= 'btn-div'),
                
                
                ], className = 'reco-col-content'),
            
            html.Div(id='result', className="result-cont"),
            
            ],className='reco-col'),
        
        ],className= 'reco-row2'),
    
    
], className = 'reco-content')

#------------------- Callbacks -----------------------------------
@app.callback(
    Output('result', 'children'),
    State('eat-dropdown', 'value'),
    State('taste-dropdown', 'value'),
    Input('match-btn', 'n_clicks'),
)
def get_result(food, taste, btn):
    # if eat:
    #     value = eat
    #     for k, v in food_dict.items():
    #         if v == value :
    #             result = k
     
    if btn: 
        if food and taste:
            # value = food
            # result =''
            # for k, v in food_dict.items():
            #     if v == value :
            #         result = k          
            
            # 1 : je renseigne ce que je mange
            step1 = df_food[df_food['Food'] == food][:2]
            
            # 2. je stocke les vins adéquats
            wine1 = step1.iloc[0,0]
            if len(step1) > 1 : 
                wine2 = step1.iloc[1,0]
                
            # 3. je renseigne mes goûts
            list_count = []
            for index, row, in df_wine.iterrows():
                if taste == 'Woody':
                    if ('wood' in row['tokens']) | ('oak' in row['tokens']) | ('cedar' in row['tokens']):
                        list_count.append(row['variety2'])
                elif taste == 'Light and flavored':
                    if ('red fruit' in row['tokens']) | ('cherry' in row['tokens']) | ('strawberry' in row['tokens']):
                        list_count.append(row['variety2'])
                elif taste == 'Fruity and sour':
                    if ('fruit' in row['tokens']) | ('acidity' in row['tokens']) | ('dry' in row['tokens']):
                        list_count.append(row['variety2'])
                elif taste == 'Classic and tannic':
                    if ('pepper' in row['tokens']) | ('tannin' in row['tokens']) | ('tobacco' in row['tokens']):
                        list_count.append(row['variety2'])
                elif taste == 'Spicy and intense':
                    if ('spice' in row['tokens']) | ('spicy' in row['tokens']) | ('leather' in row['tokens']):
                        list_count.append(row['variety2'])
                elif taste == 'Flowery and vegetal':
                    if ('flower' in row['tokens']) | ('vegetal' in row['tokens']):
                        list_count.append(row['variety2'])
                elif taste == 'Tropical':
                    if ('tropical' in row['tokens']) | ('passionfruit' in row['tokens']) | ('peach' in row['tokens']):
                        list_count.append(row['variety2'])
                elif taste == 'Vanilla and complex':
                    if ('vanilla' in row['tokens']) | ('oak' in row['tokens']) | ('almond' in row['tokens']):
                        list_count.append(row['variety2'])
            
            x = Counter(list_count)
            # 4. j'affiche le résultat
            wine = ''
            for i in range(10) : 
                if x.most_common(10)[i][0] == wine1 :
                    wine = x.most_common(10)[i][0]
            if not wine:
                for i in range(10) : 
                    if x.most_common(10)[i][0] == wine2:
                        wine = x.most_common(10)[i][0]
            if wine : 
                return match(food, wine)
            else:
                return no_match(food, wine1, wine2, taste, x)
        else:
            return html.Div([html.P("Please enter a dish and your tastes !"),], className='error-result')
            
            
            
        
    # faire des fonctions qui affiche le résultat en dehors du callback 
    
    # if btn:
    #     value = eat
    #     for k, v in food_dict.items():
    #         if v == value :
                
    #             return f"Le résultat est {k}"


        
