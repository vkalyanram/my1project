from django.http import HttpResponse
from django.shortcuts import render
import mysql.connector

# Create your views here.
def display(request):
    if request.method == 'POST':
        var= request.POST["var"]
        rows=my_sql(var)
     
        return render(request, 'display.html', {'name':rows})
    else:
        return render(request, 'about.html', {})    
def my_sql(id):
    connection = mysql.connector.connect(host='localhost',
                                             database='electronics',
                                             user='root',
                                             password='root')

    cursor = connection.cursor()
    sql_select_query = """select * from Laptop where Id = %s"""
    id=(id,)
    cursor.execute(sql_select_query,id)
    record = cursor.fetchall()
    if connection.is_connected():
            cursor.close()
            connection.close()
                     
    return record
    