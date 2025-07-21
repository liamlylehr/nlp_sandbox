from transformers import pipeline, AutoTokenizer, AutoModelForTokenClassification
import spacy
from collections import defaultdict


try:
    # Load models
    nlp = spacy.load("en_core_web_md")
    sentiment_pipeline = pipeline("sentiment-analysis", 
                                model="cardiffnlp/twitter-roberta-base-sentiment-latest")
except Exception as e:
    print(f"Error loading models: {e}")
    exit(1)

def analyze_entity_sentiment(text):
    doc = nlp(text)
    entities = [(ent.text, ent.label_, ent.start_char, ent.end_char) for ent in doc.ents]
    print("Entities:", entities)
    print("Sentences:", [sent.text for sent in doc.sents])
    print()

    results = defaultdict(list)

    for entity_text, entity_type, start, end in entities:
        # Find sentences containing the entity
        sentences = [sent.text for sent in doc.sents 
                    if start >= sent.start_char and end <= sent.end_char]
        
        for sentence in sentences:
            # Analyze sentiment of the sentence
            sentiment = sentiment_pipeline(sentence)[0]
            results[entity_text].append({
                'sentiment': sentiment['label'],
                'confidence': sentiment['score'],
                'context': sentence,
                'entity_type': entity_type
            })
    
    return results

text = "Mister Monkey buys happy Bananas for $1 billion. No more sad Monkeys!"
print()
results = analyze_entity_sentiment(text)

for entity, sentiments in results.items():
    print(f"Entity: {entity}")
    for sentiment in sentiments:
        print(f"  Sentiment: {sentiment['sentiment']}, Confidence: {sentiment['confidence']:.2f}, Context: {sentiment['context']}, Entity Type: {sentiment['entity_type']}")
    print()