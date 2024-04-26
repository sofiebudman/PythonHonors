ASSESS_PERCENT = 0.6
PROPERTY_TAX_PERCENT = 0.0072

def askUser():
    value = int(input('Enter the value of your property: '))
    assessmentValue = ASSESS_PERCENT*value
    def calculate(assessmentValue):
        return PROPERTY_TAX_PERCENT*assessmentValue
    print(f'For a ${value:,.2f} property, the assessment value will be ${assessmentValue:,.2f} and the property tax will be ${calculate(assessmentValue):,.2f}')
    
    
askUser()
