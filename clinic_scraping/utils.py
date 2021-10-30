from bs4 import BeautifulSoup


def get_clinic_name(search_list):
    try:
        clinic_name = search_list.select('a.list-ClinicBox_TitleLink')
        clinic_name = clinic_name[0]
        clinic_name = clinic_name.text.strip()
        return clinic_name
    except:
        return None

def get_clinic_adress(search_list):
    try:
        clinic_address = search_list.select('span.address')
        clinic_address = clinic_address[0]
        clinic_address = clinic_address.text.strip()
        clinic_address = clinic_address.replace('(地図)', '')
        return clinic_address
    except:
        return None
    
def get_clinic_department(search_list):
    try:
        department = search_list.select('div.department')
        if len(department) == 2:
            department.pop(1)
        department = department[0]
        department = department.text.strip()
        return department
    except:
        return None

def get_bussine_days(search_list):
    business_days = [[], [], [], [], [], [], [], []]
    try:
        table = search_list.select_one('.business-day-table').select('tr')
        for tr in table:
                if tr.select_one('.label').text.strip():
                    clinic_time = tr.select_one('.label').text.strip()
                    tds = tr.select('td')
                    i = 0
                    for td in tds:
                        if td.text == '●':
                            business_days[i].append(clinic_time)
                            i += 1
                        else:
                            pass
        return business_days
    except Exception as e:
        return business_days

def get_adress_url(search_list):
    try:
        return search_list.select_one('.address').a.get('href')
    except:
        return None