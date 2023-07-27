from django.shortcuts import render

# Create your views here.


def index(request):
    import requests

    query = '1lb brisket and fries'
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(
        api_url, headers={'X-Api-Key': 'A1qsEkAtwiq+CL0qbNx7lQ==eISJgtw09bWcy9Gz'})
    if response.status_code == requests.codes.ok:
        print(response.text)
    else:
        print("Error:", response.status_code, response.text)
    return render(request, 'index.html')
