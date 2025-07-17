# nlp_sandbox

Set up python venv (virtual env) with library requirements.
Virtual environment not entirely necessary but highly recommended with size of files.

```bash
$ python -m venv venv
$ source ./venv/bin/activate
(venv) pip install -r requirements.txt

# if above doesn't work, install each library separately
(venv) $ python -m pip install spacy
(venv) $ python -m spacy download en_core_web_sm
```
Can also download en_core_web_md or en_core_web_lg (small, medium, large)
<h2>Sample:</h2>

```python
# Input designated in main.py
text = "Monkey buys happy Bananas for $1 billion."
```

Run with 'python main.py' command </br>

```bash
# Output on cmd
Entities: [('Bananas', 'GPE', 18, 25), ('$1 billion', 'MONEY', 30, 40)]
Sentences: ['Monkey buys happy Bananas for $1 billion.']

Entity: Bananas
  Sentiment: neutral, Confidence: 0.51, Context: Monkey buys happy Bananas for $1 billion., Entity Type: GPE

Entity: $1 billion
  Sentiment: neutral, Confidence: 0.51, Context: Monkey buys happy Bananas for $1 billion., Entity Type: MONEY
```
