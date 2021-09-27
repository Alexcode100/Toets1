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
SpecVraag4 = 'Bent u een dominee in het echt?'
SpecVraag5 = ''
SpecVraag6 = ''
#Dominee

#Vragen
input('---------------------------------------------------\nHallo! Begin hier met uw auditie voor de Talents action\nTyp \033[1mStart\033[0m om te beginnen!\n---> ')

Naam = input('Wat is uw voor en achternaam?\n---> ')

Geslacht = input('Bent u een Man/Vrouw?\n---> ')
Leeftijd = input('Wat is uw leeftijd?\n---> ')
Ervaring = input('Heeft u ervaring met acteren?\n---> ')

if Geslacht == "Man":
    Vraag1 = input(SpecVraag1)
    Vraag2 = input(SpecVraag2)
    Vraag3 = input(SpecVraag3)
    


