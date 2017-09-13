import random

# make three lists, one of verbs, one of adjectives # and one of nouns

verbs = ['Leverage', 'Sync', 'Target',
         'Gamify', 'Offline', 'Crowd-sourced',
         '24/7', 'Lean-in', '30,000 foot']

adjectives = ['A/B Tested', 'Freemium',
              'Hyperlocal', 'Siloed', 'B-to-B',
              'Oriented', 'Cloud-based',
              'API-based']

nouns = ['Early Adopter', 'Low-hanging Fruit',
         'Pipeline', 'Splash Page', 'Productivity',
         'Process', 'Tipping Point', 'Paradigm']

# choose one verb, adjective and noun from each list

verb = random.choice(verbs)
adjective = random.choice(adjectives)
noun = random.choice(nouns)

# now build the phrase by "adding" the words together

phrase = verb + ' ' + adjective + ' ' + noun

# output the phrase

print(phrase)
