
student = {}

studentName = input("Enter your Student's name")    
student["Name"] = studentName 

print(student) 

studentAge = input("Enter your student's Age:")
student["Age"] = studentAge 

studentGrade = input ("Enter students grade:") 
student["Grade"] = studentGrade   

hobbies = [] 
hobby = input("Enter your students hobby; Type done when done:") 
hobbies.append(hobby) 

while hobby != "done": 
    hobby = input ("Enter your studnets hobby; Type 'done': ").lower()
    hobbies.append(hobby) 

student["Hobbies"] = hobbies 


print(student)