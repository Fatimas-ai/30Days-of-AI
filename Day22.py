import os
os.environ["HF_HUB_DOWNLOAD_TIMEOUT"] = "600"
import chromadb
client=chromadb.Client()
collection=client.create_collection(name="books")
collection.add(
    documents=[
        "python is programming language",
        "machine learning uses data",
        "football is a sport"
    ],
    ids=["1","2","3"]
)
results=collection.query(
    query_texts=["how to learn coding?"],
    n_results=2
)
print(results)



import os
os.environ["HF_HUB_DOWNLOAD_TIMEOUT"] = "600"
import chromadb
# Create client
client = chromadb.Client()
# Create collection
collection = client.create_collection("notes")
# Add 10 documents
docs = [
    "Python is a programming language.",
    "Machine Learning uses algorithms.",
    "Deep Learning uses neural networks.",
    "RAG combines retrieval and generation.",
    "Vector databases store embeddings.",
    "LangChain helps build LLM apps.",
    "Prompt engineering improves AI responses.",
    "Pandas is used for data analysis.",
    "NumPy performs numerical computing.",
    "APIs allow applications to communicate."
]

ids = [str(i) for i in range(1, 11)]
collection.add(
    documents=docs,
    ids=ids
)
# Search
result = collection.query(
    query_texts=["How do vector databases work?"],
    n_results=3
)
print("Top 3 Results:")
for doc in result["documents"][0]:
    print("-", doc)



import chromadb
client=chromadb.Client()
movies=client.create_collection(name="movies")
movies.add(
    documents=[
        "A group of astronauts explores a distant galaxy.",
        "A superhero saves the city from villains.",
        "A detective solves a mysterious murder case.",
        "An emotional love story between two artists.",
        "A thrilling journey through outer space.",
        "A comedy about college life.",
        "A robot becomes friends with a young boy.",
        "Aliens invade Earth and humans fight back.",
        "A family goes on an exciting jungle adventure.",
        "A fantasy kingdom battles an evil wizard."
    ],
    ids=[
        "1","2","3","4","5",
        "6","7","8","9","10"
    ]
)
result=movies.query(
    query_texts=["space adventure"],
    n_results=3
)
print("top 3 results:")
for movie in result["documents"][0]:
    print(movie)



import chromadb
client = chromadb.Client()
recipes = client.create_collection("recipes")
recipes.add(
    documents=[
        "Oatmeal with banana and almonds.",
        "Chicken Biryani with spices.",
        "Vegetable salad with olive oil.",
        "Scrambled eggs with toast.",
        "Fresh fruit smoothie.",
        "Grilled fish with vegetables.",
        "Chocolate cake recipe.",
        "Protein pancakes with honey.",
        "Rice and beans.",
        "Greek yogurt with berries."
    ],
    ids=[
        "1","2","3","4","5",
        "6","7","8","9","10"
    ]
)
result = recipes.query(
    query_texts=["healthy breakfast"],
    n_results=3
)
print("Best Recipes:\n")
for recipe in result["documents"][0]:
    print(recipe)
    print(recipes.get())


import chromadb
client=chromadb.Client()
library=client.create_collection("library")
library.add(
    documents=[
        "Python Programming for Beginners",
        "Advanced Python Programming",
        "Machine Learning with Python",
        "Deep Learning Fundamentals",
        "Artificial Intelligence Basics",
        "Data Science using Python",
        "Java Programming Complete Guide",
        "C++ Programming Handbook",
        "Web Development with HTML CSS",
        "JavaScript for Beginners",
        "SQL Database Essentials",
        "Python Projects for Students",
        "Learning Pandas and NumPy",
        "Natural Language Processing with Python",
        "Python Interview Questions"
    ],
    ids=[
        "1","2","3","4","5",
        "6","7","8","9","10",
        "11","12","13","14","15"
    ]
)
print("15 books added")
result=library.query(
    query_texts=["python for beginners"],
    n_results=5
)
print("top 5 results")
for book in result["documents"][0]:
    print(book)
library.update(
    ids=["1"],
    documents=["python programming from zero to hero"]
)
print("books updated")
