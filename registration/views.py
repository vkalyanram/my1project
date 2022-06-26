from django.shortcuts import render
from django.http import HttpResponse
import mysql.connector

def insert_into_table(username,password,email):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='webSite',
                                             user='root',
                                             password='root')
        cursor = connection.cursor()
        mySql_insert_query = """INSERT INTO users (username, password, email, create_datetime) 
                                VALUES (%s, %s, %s, now()) """
        record = (username, password, email)
        cursor.execute(mySql_insert_query,record)
        connection.commit()
        flag=bool(cursor.rowcount)
    except mysql.connector.Error as error:
        connection.rollback()
        flag=False
        #print(error)
          

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            
    return flag        
def registration(request):
    return render(request, 'registration.html',{})
def registration(request):
    if request.method == 'POST':
        username= request.POST["un"]
        email= request.POST["email"]
        password = request.POST["password"]
        status=insert_into_table(username,password,email)
        return render(request, 'registred.html', {'un':username.capitalize(),'status':status})   
    else:
        return render(request, 'registration.html', {})    
