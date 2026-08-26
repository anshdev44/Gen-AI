from langchain_experimental.text_splitter import SemanticChunker
from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()



text = """
Python was created by Guido van Rossum and first released in 1991. 
The language was designed with an emphasis on readability and simplicity. 
Python uses indentation to define blocks of code, which makes its syntax visually different from languages such as C++ and Java. 
Today, Python is widely used in web development, automation, data analysis, and artificial intelligence. 
Machine learning libraries such as TensorFlow, PyTorch, and scikit-learn have contributed significantly to Python's popularity in AI research. 
Neural networks can process enormous amounts of numerical data and learn complex patterns from examples. 
Large language models use neural networks to predict and generate sequences of tokens based on patterns learned during training.

The history of the Roman Empire is completely unrelated to programming languages. 
Rome grew from a small city into one of the largest empires in the ancient world. 
Roman roads connected distant provinces and allowed armies, merchants, and information to travel efficiently. 
The Roman military was highly organized and played an important role in the expansion of the empire. 
Emperors such as Augustus, Trajan, and Hadrian shaped different periods of Roman history.

Basketball is another completely different subject. 
The sport was invented by James Naismith in 1891 as an indoor activity for students during the winter. 
A basketball team attempts to score points by throwing the ball through the opponent's hoop. 
Modern basketball depends heavily on tactics such as pick-and-rolls, spacing, fast breaks, and defensive switches. 
Professional teams also use statistical analysis to evaluate players and optimize their strategies.

Interestingly, statistics are also extremely important in machine learning. 
A model can use historical data to estimate probabilities and discover relationships between variables. 
However, correlation does not necessarily imply causation, and a model trained on biased data can produce unreliable predictions. 
This is why data preprocessing, evaluation metrics, validation techniques, and careful interpretation are important when developing machine learning systems.
"""

embeddings = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-2",
)
text_splitter=SemanticChunker(
    embeddings=embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=0.5
)


chunks=text_splitter.split_text(text)

for i,chunk in enumerate(chunks):
    print('chunk number if ',i)
    print(chunk)
    print('\n\n\n\n\n\n')