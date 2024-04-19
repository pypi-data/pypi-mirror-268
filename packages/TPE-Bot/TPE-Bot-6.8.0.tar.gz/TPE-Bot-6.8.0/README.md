# TPEBot

TPEduBot is a Python library for personalised chatbot building.

## Installation
Install packages through configuration file
```bash
pip install -r requirements.txt
```

Use the package manager to install TPEBot.

```bash
pip install git+https://github.com/esterggh/TPEBot_V6.git
```

## Usage

```python
import buildABot
from buildABot import Manager

# create an object
chatbot = Manager()

# call methods from object
chatbot.createIntents()

# QAHelper prompt
Produce 3 entries of common questions and answers for the subject: Writing in APA Styles in JSON format enclosed in a array. Focus on the following main topics: Reference List, In-text Citations and Elements of an APA Paper. Generated common question should be stored as the value of the key "Question 1". JSON should include the following keys: Main Topic, Sub Topic, Name, Question 1, Answer.
```


## Contributing
This is a private repo hence no external commitments are allowed.

## License
This chatbot package are under Temasek Polytechnic License. <br>
Please approach our principle inventor of TPEBot: <br>
Dr Zhang Huiyu <br>
School of Informatics & IT, Temasek Polytechnic <br>
zhang_huiyu@tp.edu.sg 

