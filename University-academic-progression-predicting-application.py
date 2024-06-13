# I declare that my work contains no examples of misconduct, such as plagiarism, orcollusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID:20221055/ w1953623
# Name: Kapparage Nishadi
#Date: 14/12/2022


#creating variables
progress = 0
retriever = 0
count = 0
trailer = 0
excluded = 0
all_inputs=[]


def crdit_range(credit_val):    #Define a function for the range of credit values and put validations 
    while True:
        try:
            credit = int(input(credit_val)) #Input credit values
        except ValueError:
            print("Integer required")
            continue
        try:
            if credit not in range(0,121) or credit % 20 !=0: #Checking whether the credit values are in the range or is divisible by 20.If not,out of range.
                print("Out of range")
                continue
        except:
            break
        break
    return credit 



while True:
        pass_credit = crdit_range("\nPlease enter your credits at pass: ")
        defer_credit = crdit_range("Please enter your credit at difer: ")
        fail_credit = crdit_range("Please enter your credit at fail: ")

        if pass_credit + defer_credit + fail_credit == 120: #If else statment for Progression Outcomes
            if pass_credit == 120:
                outcome = "Progress"
                progress += 1
                count += 1
                
            elif pass_credit == 100 : 
                outcome = "progress (module trailer)"
                trailer += 1
                count += 1
                
            elif fail_credit==120 or fail_credit==100 or fail_credit== 80: 
                outcome = "Exclude"
                excluded += 1
                count +=1
                
            else:                            #as there are many credit levels in retriever
                outcome = "Module retriever" 
                retriever += 1
                count += 1
                
            print(outcome)
        else:
            print("Total incorrect")
            continue

        while True:
            Option = input("\nWould you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results: ")
            if Option == "y":
                break
            elif Option == 'q':
                break
            else:
                print("Invalid option. Please enter either 'y' or 'q' ",'\n')
                continue

        all_inputs.append(outcome + ' - ' + str(pass_credit) + ", " + str(defer_credit) + ", " + str(fail_credit) + '\n') #append data to the input seperatly 

        if Option == 'q':
            break
        else:
            continue        

#Printing Histogram
print()
print("--------------------------------------------------------------------------------------------------------------------------------------")
print("Histogram")
print("Progress" ,progress,' :',progress*'*')
print("Trailer" ,trailer, ' :',trailer*'*')
print("Retriever" ,retriever, ':',retriever*'*')
print("Exclude",excluded,' :', excluded*'*')
print()
print(count,"Outcomes in total.")
print("--------------------------------------------------------------------------------------------------------------------------------------")
        

#part2
for i in range (len(all_inputs)):     #printing items in list using for loop          
    print (all_inputs[i])

print("--------------------------------------------------------------------------------------------------------------------------------------")
#part3   
file = open("Progression_outcomes.txt","w")#store written values in to a 'file',add all inputs list to the file
file.writelines(all_inputs)                     
file.close()


file = open('Progression_outcomes.txt','r')
content = file.read() #'content' saves what it reads and print it
print (content)
file.close
