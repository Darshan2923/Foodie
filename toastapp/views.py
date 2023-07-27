from django.shortcuts import render

# Create your views here.


def index(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': "A1qsEkAtwiq+CL0qbNx7lQ==eISJgtw09bWcy9Gz"})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = 'opps!there was an error'
            print(e)
        return render(request, 'index.html', {'api': api})
    else:
        return render(request, 'index.html', {'query': 'Enter a valid query'})
