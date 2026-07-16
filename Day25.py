def add(a,b):
    return a+b
print (add(20,30))

def search(query):
    return f"results for:{query}"
print(search("Artificial Intelligence"))

weather={
    "karachi":"sunny",
    "lahore":"rainy",
    "fsd":"cloudy"
}
city=input("enter city:")
print(weather.get(city,"city not found"))




def calculator(a, b):
    return a + b
def weather(city):
    data = {
        "Karachi": "Sunny",
        "Lahore": "Rainy",
        "Islamabad": "Cloudy"
    }
    return data.get(city, "Weather not available")
def search(topic):
    return f"Searching information about {topic}..."
print("=== AI Assistant Agent ===")
print("1. Calculator")
print("2. Weather")
print("3. Search")
choice = input("Choose an option (1/2/3): ")
if choice == "1":
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print("Result:", calculator(a, b))
elif choice == "2":
    city = input("Enter city: ")
    print("Weather:", weather(city))
elif choice == "3":
    topic = input("Enter topic: ")
    print(search(topic))
else:
    print("Invalid choice")