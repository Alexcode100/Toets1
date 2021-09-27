#Alexander den Otter  -  99067410
import os
import sys
#Rollen:

#Kolonel van Geelen
#Mevrouw de Wit
#Dominee Groenewoud
#Rosa Roodhart
#Professor Pimpel
#Mevrouw Blaauw van Draet
#Anders: Je mag helaas niet op auditie.

#Vragen

#Kolonel
SpecVraag1 = 'Kunt u goed acteren met wapens? (ja/nee)\n---> '
SpecVraag2 = 'Heeft u in de militaire dienst gezeten? (ja/nee)\n---> '
SpecVraag3 = 'Heeft u een snor? (ja/nee)\n---> '
#Kolonel

#Dominee
SpecVraag4 = 'Bent u een dominee in het echt? (ja/nee)\n---> '
SpecVraag5 = 'Woont u in een dorp? (ja/nee)\n---> '
SpecVraag6 = 'Heeft u een baard? (ja/nee)\n---> '
#Dominee

#Professor
SpecVraag7 = 'Bent u een archeoloog? (ja/nee)\n---> '
SpecVraag8 = 'Bent u goed in geschiedenis? (ja/nee)\n---> '
SpecVraag9 = 'Heeft u haar? (ja/nee)\n---> '
#Professor

#MW. De Wit
SpecVraag10 = 'Heeft u ervaring met koken? (ja/nee)\n---> '
SpecVraag11 = 'Heeft u voor iemand gewerkt? (ja/nee)\n---> '
SpecVraag12 = 'Heeft u lang haar? (ja/nee)\n---> '
#MW. De Wit

#Rosa
SpecVraag13 ='Vind u zichzelf knap? (ja/nee)\n---> '
SpecVraag14 ='Heeft u ervaring met het zijn van een filmster? (ja/nee)\n---> '
SpecVraag15 ='Hoelang bent u?(Antwoord in CM)\n---> '
#Rosa

#M.W Blaauw
SpecVraag16 = 'Gaat u vaak naar feesten? (ja/nee)\n---> '
SpecVraag17 = 'Draagt u wel eens buitinissige kleding? (ja/nee)\n---> '
SpecVraag18 = 'Hoeveel weegt u? (Antwoord in kg)'
#M.W Blaauw

#Vragen
os.system('cls')
input('---------------------------------------------------\nHallo! Begin hier met uw auditie voor de Talents action\nTyp \033[1mStart\033[0m om te beginnen!\n---> ')
os.system('cls')
Naam = input('--------------------------\nWat is uw voor en achternaam?\n---> ')
os.system('cls')

Geslacht = input('Bent u een Man/Vrouw?\n---> ')
Leeftijd = int(input('Wat is uw leeftijd? (Leeftijd in jaren)\n---> '))
Ervaring = input('Heeft u ervaring met acteren? (ja/nee)\n---> ')
os.system('cls')

if Geslacht == "Man":
    Vraag1 = input(SpecVraag1)
    Vraag2 = input(SpecVraag2)
    Vraag3 = input(SpecVraag3)
    Vraag4 = input(SpecVraag4)
    Vraag5 = input(SpecVraag5)
    Vraag6 = input(SpecVraag6)
    Vraag7 = input(SpecVraag7)
    Vraag8 = input(SpecVraag8)
    Vraag9 = input(SpecVraag9)
else:
    Vraag10 = input(SpecVraag10)
    Vraag11 = input(SpecVraag11)
    Vraag12 = input(SpecVraag12)
    Vraag13 = input(SpecVraag13)
    Vraag14 = input(SpecVraag14)
    Vraag15 = input(SpecVraag15)
    Vraag16 = input(SpecVraag16)
    Vraag17 = input(SpecVraag17)
    Vraag18 = input(SpecVraag18)

if Geslacht == "Man" and Leeftijd >=18 and Ervaring == "ja" and Vraag1 == "ja" and Vraag2 == "ja" and Vraag3 == "ja":
    print('Gefeliciteerd! '+ str(Naam)+ 'U kunt auditie doen voor Kolonel van Geelen!')

elif Geslacht == "Man" and Vraag4 == "ja" and Vraag5 == "ja" and Vraag6 == "ja":
    print('Gefeliciteerd! '+ str(Naam)+ ' U kunt auditie doen voor Dominee Groenewoud!')

elif Geslacht == "Man" and Vraag7 == "ja" and Vraag8 == "ja" and Vraag9 == "ja":
    print('Gefeliciteerd! '+ str(Naam)+ ' U kunt auditie doen voor Professor Pimpel')

elif Geslacht == "Vrouw" and Vraag10 == "ja" and Vraag11 == "ja" and Vraag12 == "ja":
    print ('Gefeliciteerd! '+ str(Naam)+ ' U kunt auditie doen voor Mevrouw de Wit!')

elif Geslacht == "Vrouw" and Vraag13 == "ja" and Vraag14 == "ja" and Vraag15 >=175:
    print('Gefeliciteerd !'+ str(Naam)+ ' U kunt auditie doen voor Rosa Roodhart!')

elif Geslacht == "Vrouw" and Vraag16 == "ja" and Vraag17 == "ja" and Vraag18 <=120:
    print('Gefeliciteed! '+ str(Naam)+ ' U kunt auditie doen voor Mevrouw Blaauw van Draet!')

else:
    print('Helaas! '+ str(Naam)+ ' U kunt geen auditie doen bij ons!')





