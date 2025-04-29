import requests
url = 'http://localhost:5000/add'
data = {'num1': 10, 'num2':3}

response = requests.post(url, data=data)

if response.status_code == 200:
    result = response.text
    print(f'Result: {result}\n')
else:
    print('Error: ', response.text)