import sys
if len(sys.argv)!=3:
  print("usage:python student.py<name><rollno>")
  sys.exit(1)
  #sys.argv[0]is always the program name
script_name = sys.argv[0]
name=sys.argv[1]

print("script Name:",script_name)
print("student Name:",name)


  
