import  MySQLdb
from datetime import datetime

def database_function(staff_id, visitor_name, purpose):
    dateunF=datetime.now()

    date = dateunF.strftime('%Y-%m-%d')

    time=dateunF.strftime('%H:%M:%S')

    db = MySQLdb.connect('localhost', 'root', 'root','roboception')
    cursor = db.cursor()
    sql="select * from staff"
    cursor.execute(sql)
    re = cursor.fetchall()
    cabin=0
    contact=""
    dept=""
    staff_info=[]
    for rows in re:
        if staff_id==rows[0]:
            if rows[5]==0:
                # print(rows[1] ," is absent")       #speak for absent
                staff_info.append(rows[1])
                return staff_info

            else:
                # ask for purpose
                # purpose ="i have an appointment"
                cursor.execute('insert into visitor (name,purpose,date,time,staff_id) values(%s, %s, %s, %s, %s)',(visitor_name,purpose,date,time,staff_id))
                db.commit()
                cabin=rows[4]
                contact=rows[2]
                dept=rows[3]
                staff_info.append(rows[1])
                staff_info.append(cabin)
                staff_info.append(dept)
                staff_info.append(contact)
                # print(rows[1],"  ",cabin,"  ",dept,"  ",contact)
                return staff_info
    return None
# print(database_function(11))