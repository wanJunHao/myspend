from django.shortcuts import render
# from django.http import HttpResponse
from rest_framework.decorators import api_view
from django.core.paginator import Paginator

import MySQLdb


@api_view(["GET"])
def index(request):
    '''
    '''
    if request.method == 'GET':
        return render(request, 'app_1/index.html')


@api_view(["GET", "POST"])
def spend(request, method):
    '''
    '''
    conn = getConn()
    c = conn.cursor(cursorclass=MySQLdb.cursors.DictCursor)
    if request.method == 'GET':
        if method == 'our':
            sql = '''select * from spend'''

    elif request.method == 'POST':
        if method == 'our':
            jsonData = request.data
            sql = '''
            select * from spend where DATE_FORMAT(in_date, '%Y-%m-%d') >= '{0}' and DATE_FORMAT(in_date, '%Y-%m-%d') <= '{1}'
            '''.format(jsonData['start'], jsonData['end'])

    print(sql)
    c.execute(sql)
    data = c.fetchall()

    # 分页
    paginator = Paginator(data, 14)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    count = 0
    for i in data:
        count += i['money']
    context = {
        "contacts": contacts,
        "count": count
    }
    return render(request, 'app_1/spend.html', context)


def getConn():
    '''
    '''
    conn = MySQLdb.connect(host='localhost', port=3306, user='root', password='123.com', db='myspend', charset='utf8')
    return conn
