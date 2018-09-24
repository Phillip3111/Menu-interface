
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.!?'
MAX_KEY_SIZE = len(SYMBOLS)


while True:
    user_choice=input("Your options for this program: \n\tEncrypt \n\tDecrypt \n\tQuit \n\tPASSWORD \n")

    if user_choice in 'uJKNNKRKUVJGDGUV':           #This is the sercret option
        print("*"*50)
        print("*"*22,"Y THO","*"*21)
        print("*"*50)
        break
        
    if user_choice in ['Quit','quit','q','Q']:      #This stops the program if the uer wishes
        print("*"*52)
        print("Thank you for using Phillip's Translator!")
        print("*"*52)
        break
    
    def getMode():                                  #this determines what to do(encrypt/decrypt)                         
        while True:             
            mode=user_choice
            mode=mode.lower()
            if (mode in ['encrypt','e','decrypt','d']):
                return mode               
            else:
                print("Try again\nEnter 'encrypt','e','decrypt', or 'd'")
                
            

    def getMessage():                               #gets the message from the user
            print("Enter the message you want changed: ")
            return input()

    def getKey():                                   #determines how to change the message
        key = 0
        while True:
            print ("Enter the key number (1-%s)"%(MAX_KEY_SIZE))
            key = int(input())
            if (key >= 1 and key <= MAX_KEY_SIZE):  #checks to see if the key entered is valid (between 
                return key

    def getTranslation(mode, message, key):   #actually encrypts/decrypts the message
        if mode[0] == 'd':
            key= -key
        translated = ''
        for symbol in message:
            symbolIndex = SYMBOLS.find(symbol)
            if symbolIndex == -1:
        
                translated += symbol
            else:
                symbolIndex += key
            
                if symbolIndex >= len(SYMBOLS):		
                    symbolIndex -= len(SYMBOLS)		
                elif symbolIndex < 0:		
                    symbolIndex += len(SYMBOLS)
	    
                translated += SYMBOLS[symbolIndex]
        return translated

    mode = getMode()
    message = getMessage()
    key = getKey()
    print("Your translated message is: ")
    print(getTranslation(mode, message, key))
    print()

                    
              
    
