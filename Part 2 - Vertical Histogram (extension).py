# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.


# Any code taken from other sources is referenced within my code solution.


# Student ID: 20210800 
 
# Date: 07/12/2021


#Part1 Mainversi
print("Staff Version with Histogram\n")

count=0
progress=0
trailer=0
retriver=0
exclude=0




while True:
    try:
        volume_of_credit1 = int(input("Please Enter your credit at pass"))
    except ValueError:
        print("Please Enter valid integer value")
        continue
    if volume_of_credit1%20!=0:
        print('Out of range')
        continue
    elif volume_of_credit1>121:
        continue
    try:
        volume_of_credit2=int(input("Please Enter your credit at defer"))
    except ValueError:
        print("Please Enter valid integer value")
        continue                                                                        #validation and exception handling
    if volume_of_credit2%20!=0:
        print('Out of range')
        continue
    elif volume_of_credit1>121:
        continue

    try:
        volume_of_credit3 = int(input("Please Enter your credit at fail"))
    except ValueError:
        print("Please Enter valid integer value")
        continue
    if volume_of_credit3%20!=0:
        print('Out of range')
    elif volume_of_credit3>121:
        print('out of range')
        continue
    
    total=volume_of_credit1+volume_of_credit2+volume_of_credit3
    if total!=120:
        print('Total incorrect')                                                    #Validate total  credit
        continue


    if volume_of_credit1==120 and total==120:
        print( "Progress")
        count+=1
        progress+=1
    elif volume_of_credit1==100 and total==120:                                         #Outcomes of user input
        print('Progress(module trailer)')
        count+=1
        trailer+=1
    elif volume_of_credit1<=80 and volume_of_credit3<=60:
        print( 'Do not progress-module retriever')
        count+=1
        retriver+=1
    elif volume_of_credit1<=40 and volume_of_credit3>=80:
        print('Exclude')  
        count+=1
        exclude+=1

     
    print('Would you like to enter another set of data?')
    user_input1=input("Enter 'y' for yes or 'q' to quit and view results: " )            
    if user_input1=='y':
        continue
    elif user_input1=='q':
        print(' _  '*15)
        print('Horizontal Histogram')
        print('Progress',progress,':',progress*"*")
        print('Trailer',trailer,':','*'*trailer)
        print('Retriver',retriver,':',retriver*"*")                                       #Histogram
        print('Exclude',exclude,':',exclude*"*")
        print(count,'in total')
        print('  _ '*15)

        
    print(      "Vertical Histograme"      )
    histogram=["Progress,Trailing,Retriever,Excluded"]
    print(' '.join(histogram))
    for x in range(max(progress, trailer, retriver, exclude)):                          #Vertical Histogram
        print("   {0}       {1}       {2}        {3}".format(                           
                '*' if x < progress else ' ',
                '*' if x < trailer else ' ',                                            #Reference(https://www.w3schools.com/python/ref_string_join.,https://www.w3schools.com/python/ref_func_format.asp)
                '*' if x < retriver else ' ',
                '*' if x < exclude else ' '
                 ))
    break
        
         
