import json

from django.shortcuts import render


def home(request):
    import requests
    # aplhapoint= 32PUKSXOZL0C4RQD
    # polygon.io= Yc5MSGv3chvIQNmQLtO64sVPkrDF3Yb2
    if request.method == 'POST':
        ticker = request.POST['ticker']
        # modify this for the search
        api_requests = requests.get("https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2024-01-09/2024-01-09"
                                    "?apiKey=Yc5MSGv3chvIQNmQLtO64sVPkrDF3Yb2")
        try:
            api = json.loads(api_requests.content)
        except Exception as e:
            api = "Error....."
        return render(request, 'home.html', {"api": api})

    else:
        return render(request, 'home.html', {'ticker': "Enter a Ticker Symbol above.."})


def add_stock(request):
    return render(request, 'add_stock.html', {})


def about(request):
    return render(request, 'about.html', {})
