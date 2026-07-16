from PyPDF2 import PdfReader
reader = PdfReader("sample.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text()+"\n"
print(text)

import chromadb
client = chromadb.Client()
collection = client.create_collection("notes")
collection.add(
    documents=[
        "Python is easy to learn.",
        "Machine Learning uses data.",
        "Football is a sport."
    ],
    ids=["1", "2", "3"]
)
result = collection.query(
    query_texts=["Python"],
    n_results=2
)
print(result["documents"][0])