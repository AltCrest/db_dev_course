import pandas as pd
import requests
import json


#   Make a function
def get_cat_facts(_amount):
    #   1. SETUP Connection string
    #   CHECK DOCUMENTATION
    conn_str = f'https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount={_amount}'

    #   2. Call the API
    response = requests.get(conn_str)

    #   3. Parse the results
    response = json.loads(response.content)
    l_cat_fact = []
    for _fact in response:
        l_cat_fact.append(_fact['text'])

    # print(response['status']) # Access the values
    # print(response['text'])
    df = pd.DataFrame(l_cat_fact, columns=['Text'])
    df['new_col'] = "cat fact"

    cat_fact_df = df[df['new_col'] == 'cat fact']
    df = df[df['new_col'] == 'cat fact']

    # print(df.head())
    # df = df.loc[2, :]
    
    # one_value = df.iloc[2, 0]
    # one_row = df.iloc[0, :]
    return df
    
str_cat_facts = get_cat_facts(5)
for fact in str_cat_facts:
    print(fact + "\n")
