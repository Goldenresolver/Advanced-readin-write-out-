# Jason Polanco
#11/12/19
# A interactive program to calculate the cost of glasswork, metal, and 
# stripping for rectanglar windows

#define main
def main():
    #Declare and intialize variables
    fName=""
    lName=""
    uAge=0
    uLength=0
    uWidth=0

    outfile=""
    # variable used for read in the file
    infile= open("windowinfo.txt","r")

    #total glass is the cost per sqinch* by  area of window
    totalGlass=0.0
    
    #total  metalis the cost per sqinch* by  perimeter of window
    totalMetal=0.0
     #These constants represent the discounts 10% and 15% respectively 
    DISCOUNT1= 0.1

    DISCOUNT2=0.15
   # total window is the sum of the area and the perimeter
    totalWindow=0.0
    
    finalTotatl=0
    # reading the file line by line and declaring the readline to a variable
    line1= infile.readline()
    # reading the file line by line and declaring the readline to a variable
    line2=infile.readline()
   

    #After reading in line by line, split the "readline()" then
    # declare it to its respective variable in the same order as the read in file
    # in order to index it, that way we can convert it to a float
    glass1,glassinch=line1.split(",")
    
    alum1,alumsqinch=line2.split(",")
  #in order to index it, that way we can convert it to a float


    # convert the variable to float in order perform calculations
    glassinch= float(glassinch)
    alumsqinch = float(alumsqinch)

#weclome our user to the program with an intro
    print("WELCOME TO THE WONDERFUL WORLD OF WINDOWS!!")

# Use a try&except to prevent user from entering invalid inputs
#This will keep the program running and prevent it from crashing.
    try:
        #prompt the user  for length and width
        uLength= int(input("\nLength of the window(inches): "))

        uWidth= int(input("\nWidth of the window (inches):  "))


    except ValueError:
         print("Please enter a valid number")
         main()
         
   # Create variable for calculations which will include the variables stated above

   # One calculation for area and perimeter
    uArea = (uLength*uWidth)
    uPerimeter= (2*uLength)+(2*uWidth)
    #calculation for area * cost per sq inch
  # This is the price for the material * by the cost of the material
  # round to get 2 decimals
  
    totalGlass= round(uArea*glassinch,2)
    totalMetal= round(alumsqinch*uPerimeter,2)

    #Display the total area and perimeter to user
    #Display the total cost for the material to user
    print("\nTotal area:", uArea)
    print("\nTotal Perimeter:", uPerimeter)
    print("\nTotal totalGlass:","$%.2f"% totalGlass)
    print("\nTotal totalMetal:", "$%.2f"%totalMetal)

    # Calculation for the total price og both the glass and the metal
    totalArea_GlassMetel = round(totalGlass + totalMetal,2)
    print("\nTotal area for both materials:","$%.2f"% totalArea_GlassMetel)
    
    #If totalArea_GlassMetel is 1000-1499, calculate this
    # This calculation will calcuate the discounts either
    #10% or 15%
    #These discounts will be use in conditional statments
    finalDiscounted1 = totalArea_GlassMetel * DISCOUNT1

    #If area is 1500+, calculate this
    finalDiscounted2 = totalArea_GlassMetel * DISCOUNT2

    

    #This calculation is the total price for both glass and metal
    # subtracted from their respective discount
    CompleteTotal1 =totalArea_GlassMetel - finalDiscounted1
    CompleteTotal2 =totalArea_GlassMetel - finalDiscounted2
    

  
# Use a try&except to prevent user from entering invalid inputs
#This will keep the program running and prevent it from crashing.
    try:
        #Prompt user for first and last name
        fName = input("\nPlease enter your first name: ")
        
        lName = input("\nPlease enter your last name: ")
        # create a variable that contains the first letter of the last name
        # and the first 3 letters for the first name, and the age
        # do this by indexing and concatetion and set it = to a variable
        userName = lName[0]+fName[0:3]+str(uAge)
        #prompt user for name
        uAge=int(input("\nPlease enter your age: "))

    except ValueError:
        print("Please enter a valid response")

    


    # USe conditional statements using the total area for both
    #glass and metal to apply either the 10% discount or the 15% discount
    if totalArea_GlassMetel >1000 and totalArea_GlassMetel <=1499 :

        #display to user the discount
        print("\nYou will recieve a 10% discount!")

        # apply the 10% calculation as stated above
        CompleteTotal1 =totalArea_GlassMetel - finalDiscounted1
        #display total bill with discount applied
        print("$%.2f"%CompleteTotal1)

    elif totalArea_GlassMetel >= 1500:

        #display to user the discount
          print("\nYou will recieve a 15% discount!")

           # apply the 15% calculation as stated above
          CompleteTotal2 =totalArea_GlassMetel - finalDiscounted2

         #display total bill with discount applied
          print("$%.2f"%CompleteTotal2 )
         
        
        
   # use if user does not qualify of discount
    else:
        print("\nYou do not qualify for the discount")
        #display to user price without discount
        print("$%.2f"%totalArea_GlassMetel)
        

   # close the  read in file here because we had to incclude promts, calculations and
   # conditonal statments
    infile.close()
    # Open a new write out file, call it what you like
    # remember to use "w" to write
    outfile= open("windowtotal.txt","w")
    

   
   # Write out to the file using the variable used to open
   # Similar to above, welcome user using intro
   #When using .write only one arugment can be used, such as string or integer
   # must concatnate and convert to respective data type
    outfile.write("WELCOME TO THE WONDERFUL WORLD OF WINDOWS!!".center(80))

    # display username along with its respective variable
    #Write out prompts, such as prompts for user name and age
    outfile.write("\tUserName:"+ userName)

    outfile.write("\n\nPlease enter your name: "+fName+lName)   
    outfile.write("\nPlease enter your age:"+ str(uAge))
    

     #Write out prompts, such as prompts for lenghth
    #display length
    outfile.write("\n\nLength of the window(inches):"+str(uLength))

    #Write out prompts, such as prompts for width
    #display width
    outfile.write("\nWidth of the window(inches): "+str(uWidth))

   #Write out prompts, such as prompts for user name
    #display username
    outfile.write("\n\nName:"+fName+lName)

#Write out prompts, such as prompts for length
    #display cost of length
    outfile.write("\t\t\tUserName:"+ userName)
    print("\n***********************************************",file=outfile)

#Write out prompts, such as total cost of glass
    #display cost of cost of glass
    outfile.write("Total cost of glass: ".ljust(35)+"\t"+"$"+ str(totalGlass))

#Write out prompts, such as prompts for area,
    #display cost area
    outfile.write("\n\tArea:"+str(uArea))
    
    #Write out prompts, such as prompts for metal stripping,
    #display cost of metal stripping
    outfile.write("\nTotal cost of metal stripping: ".ljust(35)+"\t"+"$"+str(totalMetal))

    #Write out prompts, such as prompts for perimeter,
    #display perimeter
    outfile.write("\n\tPerimeter: "+str(uPerimeter))

 #Write out prompts, such as total cost of window,
    #display total cost of window
    outfile.write("\nTotal cost of window:".ljust(35))

     # USe conditional statements using the total area for both
    #glass and metal to apply either the 10% discount or the 15% discount
     #In order the write out file updated accordingly
    if totalArea_GlassMetel >1000 and totalArea_GlassMetel <=1499:
        outfile.write("\n\nYou earned a 10% Discount:".ljust(35)+"\t"+"$"+str(finalDiscounted1))
        outfile.write("\n**********************************************")
        outfile.write("\nFinal cost of window:"+"\t"+"\t"+"\t"+"$"+str(CompleteTotal1))

    elif totalArea_GlassMetel >= 1500:
        outfile.write("\n\nYou earned a 15% Discount:".ljust(35)+"\t"+"$"+str(finalDiscounted2))
        outfile.write("\n**********************************************")
        outfile.write("\nFinal cost of window:"+"\t"+"\t"+"\t"+"$"+str(CompleteTotal2))

    else:
        outfile.write(("\nYou do not qualify for the discount").ljust(35)+"$"+str(totalArea_GlassMetel))


    



    


  # close the write out file
    outfile.close()
    main()


 
main()    

