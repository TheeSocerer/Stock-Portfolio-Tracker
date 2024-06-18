import json

from django.shortcuts import render, redirect

from quotes.models import Stock
from django.contrib import messages
from .forms import StockForm


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
    import requests
    if request.method == 'POST':
        form = StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, ("Stock has been added"))
            return redirect('add_stock')
    else:
        # aplhapoint= 32PUKSXOZL0C4RQD
        # polygon.io= Yc5MSGv3chvIQNmQLtO64sVPkrDF3Yb2
        if request.method == 'POST':
            ticker = request.POST['ticker']
            # modify this for the search
            for ticker_item in ticker:
                #convert it to a string funtion
                api_requests = requests.get("https://api.polygon.io/v2/aggs/ticker/AAPL/range/1/day/2024-01-09/2024-01-09"
                                            "?apiKey=Yc5MSGv3chvIQNmQLtO64sVPkrDF3Yb2")
            try:
                api = json.loads(api_requests.content)
            except Exception as e:
                api = "Error....."

        ticker = Stock.objects.all()
        return render(request, 'add_stock.html', {'ticker': ticker})


def delete(request, stock_id):
    item = Stock.objects.get(pk=stock_id)
    item.delete()
    messages.success(request, ("Stock has been deleted"))
    return redirect('add_stock')


def about(request):
    return render(request, 'about.html', {})
