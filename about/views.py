from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector


def fetch_table(username,password):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='webSite',
                                             user='root',
                                             password='root')
        cursor = connection.cursor()
        mySql_insert_query = """select * from users where (username=%s and password=%s)"""
        record = (username, password)
        cursor.execute(mySql_insert_query,record)
        r=cursor.fetchone()
    except mysql.connector.Error as error:
        pass      
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
        return r   
def validate(request):
    if request.method == 'POST':
        username= request.POST["user"]
        password = request.POST["pass"]
        row=fetch_table(username,password)
        if bool(row): 
            dict = {
              'username': row[1].capitalize(),
              'email':row[2],
              'valid':bool(row)        
                    }
            return render(request, 'validate.html', dict)
        else:
            dict= {
                'valid':bool(row)
            }
            return render(request, 'validate.html', dict)
    else:
        return render(request, 'about.html', {})    
'''    
def validate_checkbox(request):b
            hobbies = request.POST.getlist('hobby')
            return render(request, 'about_checkbox.html', {'hobbies':hobbies})   
        else:
            return render(request, 'about.html', {})              
'''    