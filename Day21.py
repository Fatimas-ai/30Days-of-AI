documents=[
    "python is a programming language",
    "pandas is used for data analysis",
    "Numpy is used for numerical computing"
]
question="data analysis"
for doc in documents:
    if "data analysis" in doc:
        print(doc)

documents = [
    "AI helps machines learn.",
    "Python is a programming language.",
    "Pandas is used for data analysis."
]
query = "Python"
for doc in documents:
    if query.lower() in doc.lower():
        print("Found:", doc)     



#Document QnA assistant
documents = [
    "Python is a programming language used for AI and web development.",
    "Pandas is a Python library used for data analysis.",
    "NumPy is used for numerical calculations.",
    "Machine Learning helps computers learn from data.",
    "Artificial Intelligence is a technology that makes machines intelligent."
]
question=input("ask your question:")
found=False
for doc in documents:
    if question.lower() in doc.lower():
        print("answer:")
        print(doc)
        found=True
if not found:
    print("sorry")        
