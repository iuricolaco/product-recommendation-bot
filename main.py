!pip install openai
import openai
import pandas as pd

# Configurar a chave da API do OpenAI
openai.api_key = "API-KEY"

# Definir uma lista de produtos predefinida
products = pd.DataFrame({
    'ProductID': [1, 2, 3, 4],
    'ProductName': ['Laptop', 'Smartphone', 'Headphones', 'Smartwatch'],
    'Category': ['Electronics', 'Electronics', 'Accessories', 'Wearables'],
    'Price': [1000, 700, 150, 300]
})

# Exibir a tabela de produtos
products

# Função para criar o prompt a ser enviado para a API
def create_prompt(user_preferences):
    prompt = (
        "You are a shopping assistant. Based on the following list of products, "
        "and considering the user's preferences, recommend the best product:\n\n"
        "Products:\n" +
        products.to_string(index=False) +
        "\n\nUser Preferences: " + user_preferences +
        "\n\nYour response should include the product name and why it's a good fit."
    )
    return prompt

# Função para obter a recomendação usando a API do ChatGPT
def get_recommendation(user_preferences):
    prompt = create_prompt(user_preferences)
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    )

    recommendation = response['choices'][0]['message']['content'].strip()
    return recommendation

# Definir as preferências do usuário
user_preferences = "I need a high-performance device for work and entertainment."

# Obter a recomendação do chatbot
recommendation = get_recommendation(user_preferences)

# Exibir a recomendação
print("Recommendation:", recommendation)
