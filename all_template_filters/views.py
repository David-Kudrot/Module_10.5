from django.shortcuts import render
from datetime import datetime, date


# Create your views here.

def home(request):
    context = {
        'name' : 'MLA Fata Kestor',
        'description' : 'Nithub Chakrabarty',
        'dialogue' : 'Sala Marbo Ekhane Lash Poribi Sosane',
        'tips' : 'Sala Code KOR r nahole PAGLAMO char',
        'array' : ['ek ake ek', 'ek dugune dui', 'tin ake tin', 'char ake char', 'pach ake pach', 'choi ake choi', 'sat ake sar', 'att ake att', 'noi ake noi', 'dos ake dos', 'chup chap bosh'],
        'numbers' : [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115],
        'date' : date(2023, 11, 28),
        'fruitList' : ['Apple', 'Orange', 'Banana', 'Pineapple', 'Date'],
        'datetimenow' : datetime.now(),
     }
    return render(request, 'home.html', {'data' : context})