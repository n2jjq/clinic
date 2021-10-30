from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from .utils import get_bussine_days, get_clinic_adress, get_clinic_department, get_clinic_name
from .models import Condition
from .forms import ConditionForm

import pandas as pd
import time
from bs4 import BeautifulSoup
import requests


def scraping(request):
    if request.method == 'POST':
        form = ConditionForm(request.POST)

        if form.is_valid():
            condition = form.save()
            
        base_url = 'https://fdoc.jp/clinic/list/index/rgid/13/?page='
        num = 1
        clinic_lists = []

        while num <= 1:
            url = base_url + str(num)
            print('##################################################')
            print(url)
            print('##################################################')
            num += 1

            time.sleep(3)
            response = requests.get(url)
            response.encoding = response.apparent_encoding
            bs = BeautifulSoup(response.text, 'html.parser')
            clinic_search_list = bs.select('ul.clinic-search-list')

            for search_list in clinic_search_list[0].select('li.list-SearchList_Item'):
                clinic_list = [get_clinic_name(search_list), get_clinic_adress(search_list), get_clinic_department(search_list)]
                for bussines_day in get_bussine_days(search_list):
                    clinic_list.append(bussines_day)
                clinic_lists.append(clinic_list)
        
        columns = []
        if condition.name:
            columns.append('名前')
        elif condition.address:
            columns.append('住所')
        elif condition.department:
            columns.append('診療所')
        elif condition.monday:
            columns.append('月')
        elif condition.tuesday:
            columns.append('火')
        elif condition.wednesday:
            columns.append('水')
        elif condition.thursday:
            columns.append('木')
        elif condition.friday:
            columns.append('金')
        elif condition.saturday:
            columns.append('土')
        elif condition.sunday:
            columns.append('日')
        elif condition.holiday:
            columns.append('祝')

        df = pd.DataFrame(clinic_lists, columns=['名前', '住所','診療科','月', '火' , '水', '木', '金', '土', '日', '祝'])
        df = df[columns]
        df.to_csv('./clinic.csv',encoding='utf_8_sig')
    else:
        form = ConditionForm()
    conditions = Condition.objects.filter()[:5]

    return render(request ,'test.html',{'conditions':conditions, "form":form})

