# file modes: "w", "r", "a", "x" ...

#example1
f= open("test.txt" , 'w') 
f.write("#this is my first line\n")
f.write("*this is the second line\n")

f.close

#example2

with open("test.txt", "a") as f:
   f.write("first line\n")
   f.write("second line\n")

f.close

#example3
try:
    with open("test1.txt", 'r') as f:
      f.readline
   
    f.close
except Exception as e:
    print(e)

#example4
try:
     with open("test1.txt", 'r') as f:
      f.readline
   
     f.close
except:
   print("please check the file name")
             

#print(dir(f))