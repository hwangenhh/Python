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
      
    # tìm nạp hàng đầu tiên từ đối tượng con trỏ   
    result = cur.fetchone() 
    print(result); 
      
    # tìm nạp hàng tiếp theo từ đối tượng con trỏ   
    result = cur.fetchone() 
    print(result); 
  
except: 
    myconn.rollback() 
  
myconn.close() 