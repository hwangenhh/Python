import mysql.connector 
    
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
    passwd = "", database = "QuanLyLopHoc") 
    
# in đối tượng connection ra màn hình 
print(myconn) 

# tạo đối tượng cursor 
cur = myconn.cursor() 
# in đối tượng cursor ra màn hình 
print(cur)

try: 
    dbs = cur.execute("show databases") 
except: 
    myconn.rollback() 
for x in cur: 
    print(x) 
myconn.close() 