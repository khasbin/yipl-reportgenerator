from django.views import generic
from django.db.models.query import QuerySet
from django.shortcuts import render
from reportapp.models import Year, Country, Product, Sales
from django.db.models import Sum,Aggregate, Avg

# Create your views here.
import requests

def lists(request):
    url= "https://raw.githubusercontent.com/younginnovations/internship-challenges/master/programming/petroleum-report/data.json"
    r = requests.get(url).json()

    dates = []
    types = []
    sale = []
    country = []

    for i in range(len(r)):
        dates.append(r[i]['year'])
        types.append(r[i]['petroleum_product'])
        sale.append(r[i]['sale'])
        country.append(r[i]['country'])
    for i in range(len(dates)):
        ins1 = Product.objects.get_or_create(
        name = types[i]
        )
        ins2 = Year.objects.get_or_create(
               date = (dates[i]) 
        )
        ins3 = Country.objects.get_or_create(
            cname = country[i]
        )
    for i in range(len(r)):
        a = Product.objects.get(name = types[i])
        b = Year.objects.get(date = dates[i])
        c = Country.objects.get(cname = country[i])
        try:
            ins4 = Sales.objects.get_or_create(sales = int(sale[i]),typess =  a,year = b,countries = c)
        except:
            pass
    #calculating the total sale of each pertoleum product


    D_sum = Sales.objects.filter(typess__name = "Diesel").aggregate(Sum('sales'))
    K_sum = Sales.objects.filter(typess__name = "Kerosene").aggregate(Sum('sales'))
    A_sum = Sales.objects.filter(typess__name = "Aviation Turbine Fuel").aggregate(Sum('sales'))
    L_sum = Sales.objects.filter(typess__name = "Light Diesel Oil").aggregate(Sum('sales'))
    F_sum = Sales.objects.filter(typess__name = "Furnace Oil").aggregate(Sum('sales'))
    LPG_sum = Sales.objects.filter(typess__name = "LPG in MT").aggregate(Sum('sales'))
    M_sum = Sales.objects.filter(typess__name = "Mineral Turpentine Oil").aggregate(Sum('sales'))
    P_sum = Sales.objects.filter(typess__name = "Petrol").aggregate(Sum('sales'))



    queryset = Product.objects.all()


    queryset_1 = [P_sum,D_sum, K_sum,A_sum,L_sum,F_sum,LPG_sum,M_sum]


    q = zip(queryset, queryset_1)

    

    # Top 3 countries having the highest and the lowest sale 
    e = []
    cx = Country.objects.all()
    for i in cx:
        e.append([(Sales.objects.filter(countries__cname = i).aggregate(Sum('sales'))),i])
    
    x = sorted(e,key = lambda y:y[0]['sales__sum'], reverse=True)
    y  = sorted(e, key = lambda y:y[0]['sales__sum'])

    top_3_sales = []
    bottom_3_sales = []
    top_3_countries = []
    bottom_3_countries = []
    for i in range(3):
        top_3_sales.append(x[i][0])
        top_3_countries.append(x[i][1])
    
    for i in range(3):
        bottom_3_sales.append(y[i][0])
        bottom_3_countries.append(y[i][1])
    
    top_3 = zip(top_3_countries, top_3_sales)

    bottom_3 = zip(bottom_3_countries,bottom_3_sales)

   #Table to show the average sale of all pertoleum products in the interval of four years

    years_interval = [(2007,2010),(2011,2014)]
    p_name = Product.objects.all()
    avg_sale = []
    for i in p_name:
        for y in years_interval:
            avg_sale.append([(Sales.objects.filter(year__date__gte = y[0],year__date__lte = y[1], typess__name = i, sales__gt = 0).aggregate(Avg('sales'))),y,i])


    context = {    
        'q':q, 
        'top_3': top_3,
        'bottom_3':bottom_3,
        'avg_sale':avg_sale,
    }
    return render(request,"landing_page.html", context)


class ProductList(generic.ListView):
    template_name = "index.html"
    queryset = Sales.objects.all()
    context_object_name = "qset"
    

             