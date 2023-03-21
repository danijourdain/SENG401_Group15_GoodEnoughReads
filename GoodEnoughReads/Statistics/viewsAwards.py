from django.shortcuts import render, redirect
from . import Awards
import PIL

def awards(request):

    #Hardcoded email for now
    # email = "a@gmail.com"
    email = request.session['email']
    awd = Awards.Awards(email)
    Userlevel = awd.getUserLevel()
    UserXP = awd.getUserXP()
    ReqXP = awd.getReqXP(Userlevel + 1)
    
    Image = "gersiteapp/static/gersiteapp/img/Awards/"

    if UserXP > ReqXP:
        # pass
        Userlevel = awd.updateUserLevel()

    if(Userlevel < 6):
        NextReqXP = awd.getReqXP(Userlevel + 1)
        LevelUp = NextReqXP - UserXP
    else: 
        LevelUp = 0

    if Userlevel == 0:
        Image += "BeginnerReaderAward"
    elif Userlevel == 1:
        Image += "ElementaryReaderAward"
    elif Userlevel == 2:
        Image += "IntermediateReaderAward"
    elif Userlevel == 3:
        Image += "AdvancedReaderAward"
    elif Userlevel == 4:
        Image += "AvidReaderAward"
    elif Userlevel == 5:
        Image += "ProReaderAward"

    Image += ".png"

    print(Image)
    Image1 = PIL.Image.open(Image)
    Image1.save("gersiteapp/static/gersiteapp/img/Awards/Award_image.png")
    
    return render(request, 'Awards/awards.html', {"Current_XP": UserXP, 
                                                  "LevelUp_XP": LevelUp})

# <img src= "{% static '{{Award_image}}' %}" alt = "My Award" style = "display: block; margin-left: auto; margin-right: auto; width: 50%;">
