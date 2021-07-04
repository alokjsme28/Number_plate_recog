#!/usr/bin/python3

print("content-type: text/html")
print()

import cgi

z = cgi.FieldStorage()
cmd = z.getvalue("x")

print(cmd)

if cmd == 'MK-35-32' :
	print('''<pre>
	Registration Name : PRITAM TONPE 
	License No : 95784421097
        Model : VOLKSWAGEN POLO
        Registration Date : 1/12/2011
        Registering Authority : PUNE , INDIA
        Vehicle Class : MCWG
        Fuel Type : DIESEL
        Engine No : KWQ1G1761914
        Chassis No : HMSAVJHHQBDWE
        Insurance Upto : 5/13/2025
        Fitness Upto : 7/10/2033
	</pre>''')

elif cmd == 'KL01CA2555' :
	print('''<pre>
	Registration Name : K.S. IYER 
        License No : 841673763819
        Make / Model : SUZUKI / CIAZ
        Registration Date : 7/12/2017
        Registering Authority : COIMBATORE, INDIA
        Vehicle Class : MCWG
        Fuel Type : PETROL
        Engine No : KUSADW7122X21
        Chassis No : ASBAKDHBSKDAKKE
        Insurance Upto : 9/11/2026
        Fitness Upto : 11/11/2024
	</pre>''')

else :
	print("Sorry, but no records found.")
