from django.http.response import HttpResponse
import requests
from keys import api_key
from django.shortcuts import render


def get_names(request):
    req = requests.get('http://api.data.mos.ru/v1/datasets/2009/rows?api_key=' + api_key)
    response = req.json()
    print(type(response))
    result = '''
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="description" content="Сайт ищет имена новорожденных"> 
<title>Портал Москвы</title>
</head>
<body>
<style>
  body { 
  background: url(https://img3.goodfon.ru/original/5972x3341/2/2e/city-day-raw-data-game.jpg) no-repeat;
  background-size: 100%;
  background-attachment: fixed;
  color:white;}
</style>
    <h1 align="center">Данные с портала открытых данных Москвы</h1>
    <h2><i>Данные о именах новорожденных:</i></h2>
    <table cellspacing="0" cellpadding="5" border="1" align="left">
        <tr>
            <th>ID</th>
            <th>Имя</th>
            <th>Количество человек</th>
            <th>Год</th>
            <th>Месяц</th>
        </tr>
        </body>
        </html>'''

    for row in response:
        number = row.get('Number', 'NaN')
        name = row['Cells']['Name']
        cnt = row['Cells']['NumberOfPersons']
        year = row['Cells']['Year']
        month = row['Cells']['Month']
        result += '''
        <tr >
            <td>{ID}</td>
            <td>{Name}</td>
            <td>{NumberOfPersons}</td>
            <td>{Year}</td>
            <td>{Month}</td>
        </tr>
    '''.format(ID=number, Name=name, NumberOfPersons=cnt, Year=year, Month=month)
    result += '</table>'
    return HttpResponse(result)


def start_page(request):
    return render(request, 'start/page.html', {})
