#form load - sets up filing status deduction group and collects user input
TaxableIncomeBeforeDeduction = input ("Please enter your taxable income before standard deduction with no punctuation signs (will be rounded to 2 decimal places if more then 2 are provided): ")
FilingStatus = input ("Please enter Single, Married Filing Jointly, or Head of Household, as your filing status: ")
FilingStatusDeductions = ("Single", "Married Filing Jointly", "Head Of Household", 12200, 24400, 18350)

#taxable income check - verifies that a valid amount is entered for the income amount
def income_check(TaxableIncome):
    try:
        TaxableIncome = float(TaxableIncome) #attempts to turn the taxable income into a float (i.e. number with decimal places) and sends to the except statement if a valid number is not entered or the field is left blank

        if float(TaxableIncome) <= 0 or float(TaxableIncome) >= 4000000: #checks to see if the number is greater then 0 but less then 4,000,000 and returns an error if the number is not
            return("You did not enter a taxable income above $0 or below $4,000,000.")
        else: #returns the boolean value TRUE if all of the prior checks are passed
            return(True) 
            
    except ValueError: #returns an error if the first "try" check is not passed
        return("you did not enter a valid amount as a taxable income.")

DataCheckIncome = income_check(TaxableIncomeBeforeDeduction) #returns true if the data is valid and returns an error message if not

#filing status check - verifies that one of 3 valid filing status is entered
def status_check(Status):
    Status = Status.title() #capitalized the first letter of each word and lowercases all other letters to account for user capitalization differences
    if Status == FilingStatusDeductions[0] or Status == FilingStatusDeductions[1] or Status == FilingStatusDeductions[2]: #checks to see that a filing status was entered and that the entered value is one of the three allowed options
        return(True) #returns the boolean value TRUE if the filing status entered is one of the three valid options
    else:
        return("You did not enter Single, Married Filing Jointly, or Head Of Household as a filing status.") #returns an error message if the user did not enter one of the three valid filing status options

DataCheckStatus = status_check(FilingStatus) #returns true if the data is valid and returns an error message if not

#standard deduction calculation - calculates the standard deduction amount based on the filing status selected
def deduction_calculation(Status):
    Status = Status.title()
    if Status == FilingStatusDeductions[0]:
        return(FilingStatusDeductions[3])
    elif Status == FilingStatusDeductions[1]:
        return(FilingStatusDeductions[4])
    else:
        return(FilingStatusDeductions[5])

#tax rate calculation - calculates the tax rate based on the filing status selected and the individual's gross income
def taxrate_calculation(IncomeBeforeDeduction):
    if FilingStatus == FilingStatusDeductions[0]:
        if float(IncomeBeforeDeduction) > 510300:
            return(0.37)
        elif float(IncomeBeforeDeduction) > 204100:
            return(0.35)
        elif float(IncomeBeforeDeduction) > 160725:
            return(0.32)
        elif float(IncomeBeforeDeduction) > 84200:
            return(0.24)
        elif float(IncomeBeforeDeduction) > 39475:
            return(0.22)
        elif float(IncomeBeforeDeduction) > 9700:
            return(0.12)
        else:
            return(0.10)
    elif FilingStatus == FilingStatusDeductions[1]:
        if float(IncomeBeforeDeduction) > 612350:
            return(0.37)
        elif float(IncomeBeforeDeduction) > 408200:
            return(0.35)
        elif float(IncomeBeforeDeduction) > 321450:
            return(0.32)
        elif float(IncomeBeforeDeduction) > 168400:
            return(0.24)
        elif float(IncomeBeforeDeduction) > 78950:
            return(0.22)
        elif float(IncomeBeforeDeduction) > 19400:
            return(0.12)
        else:
            return(0.10)
    else:
        if float(IncomeBeforeDeduction) > 510300:
            return(0.37)
        elif float(IncomeBeforeDeduction) > 204100:
            return(0.35)
        elif float(IncomeBeforeDeduction) > 160700:
            return(0.32)
        elif float(IncomeBeforeDeduction) > 84200:
            return(0.24)
        elif float(IncomeBeforeDeduction) > 52850:
            return(0.22)
        elif float(IncomeBeforeDeduction) > 13850:
            return(0.12)
        else:
            return(0.10)

#taxes after deduction calculation - calculates the taxable income after the deduction is subtracted
def taxafterdeduction_calculation(IncomeBeforeDeduction, DeductionAmount):
    if float(IncomeBeforeDeduction) - DeductionAmount < 0:
        return(0)
    else:
        return(float(IncomeBeforeDeduction) - DeductionAmount)

#taxes owed calculation - calculates the taxes owed using the rate computed above
def taxesowed_calculation(TaxableIncome, TaxRate):
    TaxesDue = TaxableIncome * TaxRate
    return(round(TaxesDue, 2))

#continue processing? - processes the calculations if and only if both data validation checks are passed; otherwise returns the error message that was passed from the validation check
def validation_check():
    if DataCheckIncome == True:
        if DataCheckStatus == True:
            DeductionAmount = (deduction_calculation(FilingStatus))
            DeductionAmountforPrint = '%.2f' % DeductionAmount
            TaxRate = (taxrate_calculation(TaxableIncomeBeforeDeduction))
            IncomeAfterDeduction = (taxafterdeduction_calculation(TaxableIncomeBeforeDeduction, DeductionAmount))
            TaxesOwed = taxesowed_calculation(IncomeAfterDeduction, TaxRate)
            TaxesOwedforPrint = '%.2f' % TaxesOwed
            return("Your standard deduction amount is $" + str(DeductionAmountforPrint)+ " and your taxes due is $" + str(TaxesOwedforPrint))
        else:
            return(status_check(FilingStatus))
    else:
        return(income_check(TaxableIncomeBeforeDeduction))

print(validation_check()) #prints the results, either the calculated taxes or the error message
