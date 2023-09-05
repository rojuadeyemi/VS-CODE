first_name = "Ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
#print(full_name.title())
#print("{1} {0}".format(first_name, last_name))

amout = 0.0009

#print("%s %.2f"%(first_name, amout))
#print(f"{amout: .2%} {amout}") 

#Using unpack dictionary
person = {'name': 'Ade', 'age': 29}
#print("{name} is {age} years old".format(**person))

# Multiple line
name = "Ade"
profession = "Tech Expert"
affiliation = "Information Engineering Acad"
message = (f"Hi {name}. "
 f"You are a {profession}. "
 f"You were in {affiliation}.")
 
message

message1 = f"""Hi {name}. You are a {profession}. You were in {affiliation}."""

message1

import timeit
#Time complexity

a = f"{last_name} {first_name}"
b = "%s %s"%(last_name, first_name)
c = "{} {}".format(last_name, first_name)


d = (a, b, c)

for i in d:
	print(timeit.timeit("i", number=10000, globals=globals()))