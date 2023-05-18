acronyms={'LOL':'laugh out loud',
          'TBH':'To be honest',
          'IDK':'I dont know'}
del acronyms['LOL']
print(acronyms)
print(acronyms['TBH'])
sentence='IDK'+" what"+" happened "+'TBH'
translation=acronyms.get('IDK')+" what happened "+acronyms.get('TBH')
print("Sentence:",sentence)
print("Translations:",translation)
