import random
import traits 
identities = {}
possibility = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

rudeness = ["very kind", "rather kind", "kind", "somewhat kind", "neutral kindness", "somewhat rude", "rude", "rather rude", "very rude"]
seriousness = ["very relaxed", "rather relaxed", "relaxed", "somewhat relaxed", "neutral seriousness", "somewhat serious", "serious", "rather serious", "very serious"]

running = True
while running:
    request = input('request: ')
    if request == 'create':
        name = ""
        while len(name) != 6:
            name = name + random.choice(possibility)

        rudenessValue = random.randint(0, len(rudeness))
        seriousnessValue = random.randint(0, len(seriousness))
        positiveTraits = [random.choice(traits.positive), random.choice(traits.positive), random.choice(traits.positive), random.choice(traits.positive)]
        negativeTraits = [random.choice(traits.negative), random.choice(traits.negative), random.choice(traits.negative), random.choice(traits.negative)]
        neutralTraits = [random.choice(traits.neutral), random.choice(traits.neutral), random.choice(traits.neutral), random.choice(traits.neutral)]
        
        identities[name] = {'rudeness': rudenessValue, 'seriousness': seriousnessValue, 'positive': positiveTraits, 'negative': negativeTraits, 'neutral': neutralTraits, 'parents': ["Generated 1", "Generated 2"]}

        print(f"created {name}, data: {identities[name]}")

    elif request == "quit":
        running = False

    elif request == "breed":
        parent1 = input("first parent: ")
        parent2 = input("second parent: ")

        if parent1 == parent2:
            print("cannot self breed")
            continue 

        name = ""
        while len(name) != 6:
            name = name + random.choice(possibility)

        if identities[parent1]["rudeness"] < identities[parent2]["rudeness"]:
            rudenessValue = random.randint(identities[parent1]["rudeness"],identities[parent2]["rudeness"])
        elif identities[parent1]["rudeness"] > identities[parent2]["rudeness"]:
            rudenessValue = random.randint(identities[parent2]["rudeness"],identities[parent1]["rudeness"])

        if identities[parent1]["seriousness"] < identities[parent2]["seriousness"]:
            seriousnessValue = random.randint(identities[parent1]["seriousness"],identities[parent2]["seriousness"])
        elif identities[parent1]["seriousness"] > identities[parent2]["seriousness"]:
            seriousnessValue = random.randint(identities[parent2]["seriousness"],identities[parent1]["seriousness"])
        

        #rudenessValue = random.randint(identities[parent1]["rudeness"],identities[parent2]["rudeness"])
        #seriousnessValue = random.randint(identities[parent1]["seriousness"], identities[parent2]["seriousness"])

        majorityParent = random.randint(1, 2)

        if majorityParent == 1:
            positiveTraits = [random.choice(identities[parent1]["positive"]), random.choice(identities[parent1]["positive"]), random.choice(identities[parent2]["positive"]), random.choice(traits.positive)]
            negativeTraits = [random.choice(identities[parent1]["negative"]), random.choice(identities[parent1]["negative"]), random.choice(identities[parent2]["negative"]), random.choice(traits.negative)]
            neutralTraits = [random.choice(identities[parent1]["neutral"]), random.choice(identities[parent1]["neutral"]), random.choice(identities[parent2]["neutral"]), random.choice(traits.neutral)]
        elif majorityParent == 2:
            positiveTraits = [random.choice(identities[parent2]["positive"]), random.choice(identities[parent2]["positive"]), random.choice(identities[parent1]["positive"]), random.choice(traits.positive)]
            negativeTraits = [random.choice(identities[parent2]["negative"]), random.choice(identities[parent2]["negative"]), random.choice(identities[parent1]["negative"]), random.choice(traits.negative)]
            neutralTraits = [random.choice(identities[parent2]["neutral"]), random.choice(identities[parent2]["neutral"]), random.choice(identities[parent1]["neutral"]), random.choice(traits.neutral)]

        identities[name] = {'rudeness': rudenessValue, 'seriousness': seriousnessValue, 'positive': positiveTraits, 'negative': negativeTraits, 'neutral': neutralTraits, 'parents': [parent1, parent2]}
        
        print(f"created {name}, data: {identities[name]}")
            
            

print(identities)
        
