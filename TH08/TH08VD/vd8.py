import mysql.connector 
    
# tạo đối tượng connection 
myconn = mysql.connector.connect(host = "localhost", user = "root",  
    passwd = "", database = "pythondb") 
    
# in đối tượng connection ra màn hình 
print(myconn) 

# tạo đối tượng cursor 
cur = myconn.cursor() 
# in đối tượng cursor ra màn hình 
print(cur)

try: 
    # thêm cột branch name vào bảng Employee 
    cur.execute("alter table Employee add branch_name varchar(20) not null") 
except: 
    myconn.rollback() 
  
myconn.close() 
