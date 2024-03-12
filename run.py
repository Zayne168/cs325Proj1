import module_1.verifier
import module_2.scrapper


#Zayne Bonner
#800756759
#This is the run.py file for my Project
#in the main I call the verify function from my verification module
#I then copy the verified array from the module and pass it into the scrapper
#the init files declare each module folder an actual module. I had troubles without them. no comments necessary on them.
#
#The SOLID principle utilized here is the Single Responsibility Principle
#First I seperated the two main responsibilities into seperate modules(verifying urls and scrapping)
#then I broke down the two sub-responsibilities of the scrapper into 2 functions within the module
#This allows me to adjust my modules and functions if I want a different desired output
#I can also decide what I want from my run.py better. If I only want processed or raw I can do just one set or the other by calling the corresponding function.
#I can also easily adjust the individual classes with them being independent.#


#I also utlilized OCP in my module_2. I seperated the scrapper module into seperate functions.
#Adding a new scrap format involves adding a new function definition without modifying anything previously made.



def main():
    module_1.verifier.Verify()
    for idx,e in enumerate(module_1.verifier.verified):
        verified.append(module_1.verifier.verified[idx])
    module_2.scrapper.MyScrapper.ScrapNeat(verified)
    module_2.scrapper.MyScrapper.ScrapRaw(verified)


verified=[]
main()
print("Output scrapped and exported to Data folder.")