Student={
    "Name":"Anish kumar",
    "age":19,
    "School name":"Sanskriti Internation School",
        "District":"Siwan",
        "police station":"Darwli",
        "Roll no":3,       
    "subject":{
        "Phy":98,
        "Chem":89,
        "Maths":99,
         

    }
    
}
print(list(Student.values()))
print(list(Student.items()))
print((Student.get("key")))