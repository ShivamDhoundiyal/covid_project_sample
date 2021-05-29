from django.shortcuts import render
import requests
# API for  Worldwide Covid-19 Data
url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-key': "c340c9a827msh3b283cd6e1f77e0p1841acjsn83a7762aeca6",
    'x-rapidapi-host': "covid-193.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers).json()

# Create your views here.
def viewcases(request):
    mylist = []
    noofresults = int(response['results'])
    for x in range(0, noofresults):
        mylist.append(response['response'][x]['country'])
    mylist.sort()

    if request.method=="POST":
        selectedcountry = request.POST['selectedcountry']
        #print(selectedcountry)
        noofresults = int(response['results'])
        for x in range(0, noofresults):
            if selectedcountry==response['response'][x]['country']:
                new = response['response'][x]['cases']['new']
                active = response['response'][x]['cases']['active']
                critical = response['response'][x]['cases']['critical']
                recovered = response['response'][x]['cases']['recovered']
                total = response['response'][x]['cases']['total']
                deaths = int(total)- int(active)- int(recovered)
        context = {'selectedcountry': selectedcountry,'mylist' : mylist, 'new' : new, 'active' : active, 'critical' : critical, 'recovered' : recovered, 'deaths' : deaths, 'total' : total}
        return render (request, 'design.html', context)
     
    context = {'mylist' : mylist}
    return render(request,'design.html', context)
