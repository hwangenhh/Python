import mysql.connector 
    
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
    passwd = "", database = "pythondb") 
    
# in đối tượng connection ra màn hình 
print(myconn) 

# tạo đối tượng cursor 
cur = myconn.cursor() 
try: 
    # select dữ liệu từ database 
    cur.execute("SELECT name, id, salary FROM Employee") 
      
    # tìm nạp các hàng từ đối tượng con trỏ   
    result = cur.fetchall() 
  
    print("Name    ID    Salary") 
      
    for row in result: 
        print("%s    %d    %d"%(row[0],row[1],row[2])) 
  
except: 
    myconn.rollback() 