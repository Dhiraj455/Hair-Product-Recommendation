import json
from flask import Flask, request, jsonify
# Cors should be installed to allow cross-origin requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return "Welcome to Hairvise Quiz App!"


# Define route to accept user input and return recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    # Get user input from the json
    hair_loss = request.form.get('HairLoss')
    duration = request.form.get('Duration')
    shedding = request.form.get('Shedding')
    dandruff = request.form.get('Dandruff')
    type_ = request.form.get('Type')
    itchy_scalp = request.form.get('ItchyScalp')
    hair_greying = request.form.get('HairGreying')
    treatment = request.form.get('Treatment')
    regular_usage = request.form.get('RegularUsage')

    # Get user input from the body
    # data = request.get_json()
    # print(data)
    # hair_loss = data['HairLoss']
    # duration = data['Duration']
    # shedding = data['Shedding']
    # dandruff = data['Dandruff']
    # type_ = data['Type']
    # itchy_scalp = data['ItchyScalp']
    # hair_greying = data['HairGreying']
    # treatment = data['Treatment']
    # regular_usage = data['RegularUsage']
    
    # Define recommendation logics
    recommendation_logics = [
        {
            "condition": hair_loss == 'Yes',
            "recommendations": [
                {"conditions": [('Duration', 'Less than 3 months'), ('Shedding', 'Rarely')],
                 "products": ["Rosemary oil and shampoo"]},
                {"conditions": [('Duration', 'Less than 3 months'), ('Shedding', 'Occasionally')],
                 "products": ["Rosemary oil and shampoo"]},
                {"conditions": [('Duration', 'Less than 3 months'), ('Shedding', 'Frequently')],
                 "products": ["Biotin gummies"]},
                {"conditions": [('Duration', '3 to 6 months'), ('Shedding', 'Rarely')],
                 "products": ["Biotin gummies"]},
                {"conditions": [('Duration', '3 to 6 months'), ('Shedding', 'Occasionally')],
                 "products": ["Biotin gummies"]},
                {"conditions": [('Duration', '3 to 6 months'), ('Shedding', 'Frequently')],
                 "products": ["Biotin gummies and Hair growth serum"]},
                {"conditions": [('Duration', 'More than 6 months'), ('Shedding', 'Rarely')],
                 "products": ["Biotin gummies"]},
                {"conditions": [('Duration', 'More than 6 months'), ('Shedding', 'Occasionally')],
                 "products": ["Biotin gummies and Hair growth serum"]},
                {"conditions": [('Duration', 'More than 6 months'), ('Shedding', 'Frequently')],
                 "products": ["Biotin gummies and Hair growth serum"]},
            ]
        },
        {
           "condition": hair_loss == 'No',
            "recommendations": [
                {"conditions": [('Duration', 'None'), ('Shedding', 'None')],
                 "products": [""]}
            ]
        },
        {
            "condition": dandruff == 'Yes',
            "recommendations": [
                {"conditions": [('Type', 'Powdery'), ('ItchyScalp', 'Rarely or never')],
                 "products": ["Tea Tree Oil Shampoo"]},
                {"conditions": [('Type', 'Powdery'), ('ItchyScalp', 'Frequently')],
                 "products": ["Nizoral A-D anti dandruff shampoo"]},
                {"conditions": [('Type', 'Flaky'), ('ItchyScalp', 'Rarely or never')],
                 "products": ["T/Gel Therapeutic shampoo"]},
                {"conditions": [('Type', 'Flaky'), ('ItchyScalp', 'Frequently')],
                 "products": ["Ketoconazole anti dandruff shampoo"]},
                
            ]
        },
        {
           "condition": dandruff == 'No',
            "recommendations": [
                {"conditions": [('Type', 'None'), ('ItchyScalp', 'None')],
                 "products": [""]}
            ] 
        },
        {
            "condition": hair_greying == 'Yes',
            "recommendations": [
                {"conditions": [('Treatment', 'Colour or henna'), ('RegularUsage', 'Yes')],
                 "products": ["Pro V colour shampoo"]},
                {"conditions": [('Treatment', 'Colour or henna'), ('RegularUsage', 'No')],
                 "products": ["Pure black sesame oil"]},
                {"conditions": [('Treatment', 'Keratin treatment'), ('RegularUsage', 'Yes')],
                 "products": ["Keratin smooth deep mask"]},
                {"conditions": [('Treatment', 'Keratin treatment'), ('RegularUsage', 'No')],
                 "products": ["Argan oil"]},
                
            ]
        },
        {
            "condition": hair_greying == 'No',
            "recommendations": [
                {"conditions": [('Treatment', 'None'), ('RegularUsage', 'None')],
                 "products": [""]}
            ]
        }
    ]
    
    # Apply recommendation logic based on user input
    recommended_products = []
    for logic in recommendation_logics:
        if logic["condition"]:
            for recommendation in logic["recommendations"]:
                conditions_met = True
                for condition in recommendation["conditions"]:
                    if request.form.get(condition[0]) != condition[1]:
                        conditions_met = False
                        break
                if conditions_met:
                    recommended_products.extend(recommendation["products"])
    
    # Return recommended products as JSON response
    return jsonify({'recommended_products': recommended_products})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
