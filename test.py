import google.generativeai as genai
genai.configure(api_key='AIzaSyAAIIuln6f_QG-4OlnVLdztmuQ6u0XUsrU')
model = genai.GenerativeModel('gemini-pro')
while True:
    query = input("You: ")
    response = model.generate_content(query)
    print(f"A.I: {response.text[:200]}")
