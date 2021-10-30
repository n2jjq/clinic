from django.shortcuts import render, redirect
from django.template.response import TemplateResponse
from .utils import get_bussine_days, get_clinic_adress, get_clinic_department, get_clinic_name

import pandas as pd
import time
from bs4 import BeautifulSoup
import requests


def scraping(request):
    if request.method == 'POST':

        base_url = 'https://fdoc.jp/clinic/list/index/rgid/13/?page='
        num = 1
        clinic_lists = []

        while num <= 5:
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


        df = pd.DataFrame(clinic_lists, columns=['名前', '住所','診療科','月', '火' , '水', '木', '金', '土', '日', '祝'])
        df.to_csv('./clinic.csv',encoding='utf_8_sig')
        
        return render(request,'test.html')
    else:
        return render(request ,'test.html')

