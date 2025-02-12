import mysql.connector 
    
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
    passwd = "", database = "pythondb") 
    
# in đối tượng connection ra màn hình 
print(myconn) 

# tạo đối tượng cursor 
cur = myconn.cursor() 

try: 
    # cập nhật name cho bảng Employee 
    cur.execute("update Employee set name = 'Đạt' where id = 10001") 
    myconn.commit() 
  
except: 
    myconn.rollback() 
  
myconn.close() 