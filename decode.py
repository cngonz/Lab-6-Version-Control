
def decode(password):
     pass
     # Declares decoded string
     dco = ""
     # Counter for while loop
     c=0
     # Loops through each digit in the password string
     while c < len(eco):
         # Each digit gets shifted down 3 based on starting digit
         if password[c] == "0":
             dco += "7"
         elif password[c] == "1":
             dco += "8"
         elif password[c] == "2":
             dco += "9"
         elif password[c] == "3":
             dco += "0"
         elif password[c] == "4":
             dco += "1"
         elif password[c] == "5":
             dco += "2"
         elif password[c] == "6":
             dco += "3"
         elif password[c] == "7":
             dco += "4"
         elif password[c] == "8":
             dco += "5"
         elif password[c] == "9":
             dco += "6"
         c += 1
     # Returns new decoded password
     return dco
