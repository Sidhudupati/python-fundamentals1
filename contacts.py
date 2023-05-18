contacts={'number':3,
          'students':
          [
          {'name':'Sidhu','email':'sdupati@gmail.com'},
          {'name':'Bhanu','email':'bhanu@gmail.com'},
          {'name':'Hari','email':'hari@gmail.com'}
          ]
         }
print("Student email")
for student in contacts['students']:
    print(student['email'])