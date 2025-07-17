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
