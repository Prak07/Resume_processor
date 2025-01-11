import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "Prakhar Agrawal is applying for the position. Contact him at john.doe@example.com."

# Process text
doc = nlp(text)

# Extract names
names = [ent.text for ent in doc.ents if ent.label_ == "PERSON"]
print(names)  # Output: ['John Doe']
