import os
os.system('cls')
def evaluate_password(password):
    # Boolean flag variables corresponding to each rule (criteria)
    Gate1 = False  # Gate1 = rule 1
    Gate2 = False  # Gate2 = rule2
    Gate3 = False  # Gate3 = rule3

    # Criteria checks
    '''
    # ToDo:
    # Code for at least three rule (criteria) evaluate a given password for its security strength.
    # For each criteria, check the desired condition and save the status in the corresponding boolean flag variable. 
    # You can use Python's built-in functions and modules for help. 
    '''
    non_compliant_message = ''
    #Rules Are : password must be 8 characters or more, has capital lettters, and has numbers as well.
    if len(password) >= 8:
        Gate1 = True
    if any(char.isupper() for char in password):
        Gate2 = True
    if any(char.isdigit() for char in password):
        Gate3 = True

    if not Gate1:
        non_compliant_message += "Your Password Must Contain At Least 8 characters.\n"
    if not Gate2:
        non_compliant_message += "Your Password Must Contain Capital Letter(s).\n"
    if not Gate3:
        non_compliant_message += "Your Password Must Contain a Number or More.\n"

    if Gate1 and Gate2 and Gate3:
        return "Compliant. Your Password Is Unbreakable!"

    return non_compliant_message

'''
# Do not change the code below
'''
# User input
password = input("Enter your password: ")
print(evaluate_password(password))
