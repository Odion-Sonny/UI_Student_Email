def email_gen(firstname, lastname, matric_no):
    firstname = firstname.lower()
    lastname = lastname.lower()
    domain = '@stu.ui.edu.ng'

    matric_no_list = matric_no[3:]
    
    matric_no_string =''.join(matric_no_list)
    
    email = ''.join((firstname[0],lastname,matric_no_string,domain))
    return email
def main():
    firstname = input('Please Enter Your First Name: ')
    lastname = input('Please Enter Your Last Name: ')
    matric_no = input('Please Enter Your Matriculation Number: ')
    print(f'Your Student Email Is: {email_gen(firstname, lastname, matric_no)}')    

main()
