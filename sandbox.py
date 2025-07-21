import spacy

text = [
    "X is a big company in the tech industry.",
    "Apple is a leading tech company.",
    "John Doe is a software engineer at Google.",
    "The Eiffel Tower is in Paris.",
    "Microsoft acquired LinkedIn in 2016.",
    "Barack Obama was the 44th President of the United States.",
    "Amazon is headquartered in Seattle.",
    "The Great Wall of China is a famous landmark.",
    "Tesla's CEO is Elon Musk.",
    "The Louvre Museum is in Paris.",
    "NASA launched the Artemis program.",
    "Bill Gates co-founded Microsoft.",
    "The United Nations is an international organization.",
    "The Amazon rainforest is a vast ecosystem.",
    "The Mona Lisa is displayed at the Louvre.",
    "The Statue of Liberty is in New York City.",
    "Facebook rebranded to Meta.",
    "The Golden Gate Bridge is in San Francisco.",
    "The White House is the official residence of the President of the United States.",
]

nlp = spacy.load("en_core_web_md")

ner_labels = nlp.get_pipe("ner").labels

categories = ['ORG', 'PERSON', 'LOC']

docs = [nlp(t) for t in text]

for doc in docs:
    entities = []
    for ent in doc.ents:
        entities.append((ent.text, ent.label_, ent.start_char, ent.end_char))
        # if ent.label_ in categories:
        #     entities.append((ent.text, ent.label_, ent.start_char, ent.end_char))

    print("Entities:", entities)