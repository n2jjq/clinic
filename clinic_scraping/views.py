from django.http.response import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import response
from django.template.response import TemplateResponse
from .utils import get_bussine_days, get_clinic_adress, get_clinic_department, get_clinic_name, get_adress_url
from .models import Condition
from .forms import ConditionForm
from django.http import HttpResponse
from django.urls import reverse

import pandas as pd
import time
from bs4 import BeautifulSoup
import requests


def scraping(request):
    if request.method == 'POST':
        if 'create' in request.POST:
            form = ConditionForm(request.POST)
            if form.is_valid():
                condition = form.save()
        elif 'past' in request.POST:

            condition = Condition.objects.get(id=request.POST['id'])
            form = ConditionForm()
        base_url = 'https://fdoc.jp/clinic/list/index/rgid/13/?page='
        num = 1
        print(condition.page)
        clinic_lists = []
        while num <= condition.page:
            url = base_url + str(num)
            num += 1

            time.sleep(3)
            response = requests.get(url)
            response.encoding = response.apparent_encoding
            bs = BeautifulSoup(response.text, 'html.parser')
            clinic_search_list = bs.select('ul.clinic-search-list')

            for search_list in clinic_search_list[0].select('li.list-SearchList_Item'):
                clinic_list = [get_clinic_name(search_list), get_clinic_adress(search_list), get_adress_url(search_list), get_clinic_department(search_list)]
                for bussines_day in get_bussine_days(search_list):
                    clinic_list.append(bussines_day)
                clinic_lists.append(clinic_list)
        
        columns = []
        if condition.name:
            columns.append('名前')
        if condition.address:
            columns.append('住所')
        if condition.link:
            columns.append('リンク')
        if condition.department:
            columns.append('診療科')
        if condition.monday:
            columns.append('月')
        if condition.tuesday:
            columns.append('火')
        if condition.wednesday:
            columns.append('水')
        if condition.thursday:
            columns.append('木')
        if condition.friday:
            columns.append('金')
        if condition.saturday:
            columns.append('土')
        if condition.sunday:
            columns.append('日')
        if condition.holiday:
            columns.append('祝')

        df = pd.DataFrame(clinic_lists, columns=['名前', '住所','リンク','診療科','月', '火' , '水', '木', '金', '土', '日', '祝'])
        df = df[columns]
        df.to_csv('./static/csv/'+ str(condition.id) +'clinic.csv',encoding='utf_8_sig')
        condition_id = condition.id
        return HttpResponseRedirect(reverse('download', args=(condition_id, )))
    else:
        form = ConditionForm()
    conditions = Condition.objects.order_by('-id')[:5]

    return render(request ,'top.html',{'conditions':conditions, "form":form})

def download_csv(request, pk):
    if request.method == 'POST':
        if 'download' in request.POST:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment;' + 'filename=../static/csv' + str(pk) + 'clinic.csv'
            return response
        elif 'back' in request.POST:
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request ,'download_csv.html',{'pk':pk})