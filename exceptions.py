acronyms = {'LOL':'laugh out loud',
            'TBH':'To be honest',
            'FYI':'For your information'}
try:
    defi=acronyms['BTW']
    print("Meaning is:",defi)
except:
    print("Meaning does not exist")
finally:
    print("All the acronyms are:")
    for acronym in acronyms:
        print(acronym)
print("The program continues...")                
