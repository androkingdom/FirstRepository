def IsRepeted(ListOfGuessCode:list ) -> list:
    SetOfCode = set(ListOfGuessCode)
    if len(SetOfCode) < len(ListOfGuessCode) :
        return True
    

IsRepeted()