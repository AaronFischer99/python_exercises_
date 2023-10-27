
def is_two(x):
    if x == 2 or x == "2":
        return True
    else: 
        return False
    

    

def is_vowel(vowel):
    vowels = "aeiouAEIOU"
    if vowel in vowels:
        return True
    else:
        return False
    
    
    
    
def is_vowel(vowel):
    vowels = "aeiou" or "aeiuo".upper()
    if vowel in vowels:
        return True
    else:
        return False



    

def is_consonant(consonant):
    vowels = "aeiouAEIOU"
    if consonant in vowels:
        return "Vowel"
    else:
        return "Consanant"
        print("Consonant")
    

    
    
def cap_if_consonant(x):
    vowels = 'aeiouAEIUO'   #Setting the standard
    for element in vowels:  #Setting the variable involved in the 'if' condition
        if x[0] not in vowels: #Setting the condition of the 'if' condition
             return x[0].capitalize()  #Return the outcome of the 'if' condition
        else:
            return x
        
        

def calculate_tip(x, y):
    bill_total = x
    tip_percentage = y
    tip = bill_total * tip_percentage
    return (f"${tip}")




def apply_discount(x, y):
    original_price = x
    discount_percentage = y
    total = original_price - (original_price * discount_percentage)
    return (f"${total}")




def handle_commas(x):
    no_commas = int(x.replace("," , ""))  
    return no_commas  




def get_letter_grade(grade):
    if grade >= 100:
        print('Please enter a grade between 0-100')
    elif grade >= 90 :
        print(f'{grade} is an A')
    elif grade >= 80:
        print(f'{grade} is a B')
    elif grade >= 70:
        print(f'{grade} is a C')
    elif grade >= 60:
        print(f'{grade} is a D')
    elif grade <= 59 and grade >=0:
        print(f'{grade} is an F')
    else: 
        print('No negative numbers')
        

        

def remove_vowels(string):
    vowels = ('a', 'e', 'i', 'o', 'u')
    for x in string.lower():
        if x in vowels:
            string = string.replace(x,"")
    return string





def normalize_name(text):
    new_string = (text.strip("0123456789 ").lower().replace(" ", "_"))
    output = ""
    if new_string.isidentifier() == True:
        print(new_string, 'is a valid identifier')
        for i in new_string:
            if i not in "!@#$%^&*()+=-[]{}\/|?.<>,`~":
                output += i
    else: 
        print(new_string, 'is NOT a valid identifier')
    return print(output)

normalize_name("me+you")
normalize_name(" John Wick ") 




list=[10,20,30,40,50]
new_list=[] 
j=0
for i in range(0,len(list)):
    j+=list[i]
    new_list.append(j) 
     
print(new_list)



from datetime import datetime

m1 = '2:35 PM'
m1 = datetime.strptime(m1, '%I:%M %p')
out_time = datetime.strftime(m1, "%H:%M")  #if commented out will return daya nd month as well
print(out_time)