from tkinter import *

#Code block for Story1
def Story1(win):
  #Calling Toplevel class from tkinter and defining input parameter names
  def final(tl: Toplevel, name, sports, City, playername, drinkname, snacks):
    #Story text for the game after input's have been obtained from player.
    text = f'''
       One day me and my friend {name} decided to play a {sports} game in {City}.
       But we were not able to play.So, we went to watch the game and our favourite player {playername}.
       We drank {drinkname} and also ate some {snacks} 
       We really enjoyed it! We are looking forward to go again and enjoy '''

    tl.geometry(newGeometry='500x550')
    #Defining format rules for the story text
    Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)
    Label(tl, text=text,wraplength=tl.winfo_width()).place(x=0, y=330)
  #Calling for new screen to display questions for the player, and to display the story with players answers.  
  NewScreen = Toplevel(win, bg='light blue')
  NewScreen.title("A Memorable Day")
  NewScreen.geometry('500x500')
  #Setting text locations for player input questions
  Label(NewScreen, text=' A Memorable Day').place(x=100, y=0)
  Label(NewScreen, text='Name:').place(x=0, y=35)
  Label(NewScreen, text='Enter a sport:').place(x=0, y=70)
  Label(NewScreen, text='Enter a city:').place(x=0, y=110)
  Label(NewScreen, text='Enter the name of a player:').place(x=0, y=150)
  Label(NewScreen, text='Enter the name of a drink:').place(x=0, y=190)
  Label(NewScreen, text='Enter the name of a snack:').place(x=0, y=230)
  #Player input locations for Name, Enter a game, Enter a city, Enter the name of a plater, Enter the name of a drink, Enter the name of a snack
  Name = Entry(NewScreen, width=17)
  Name.place(x=250, y=35)
  game = Entry(NewScreen, width=17)
  game.place(x=250, y=70)
  city = Entry(NewScreen, width=17)
  city.place(x=250, y=105)
  player = Entry(NewScreen, width=17)
  player.place(x=250, y=150)
  drink = Entry(NewScreen, width=17)
  drink.place(x=250, y=190)
  snack = Entry(NewScreen, width=17)
  snack.place(x=250, y=220)
  #Submit button location rules and calling for player inputted answers to fill in the story text
  SubmitButton = Button(NewScreen, text="Submit", background="White", font=('Times', 12), command=lambda:final(NewScreen, Name.get(), game.get(), city.get(), player.get(), drink.get(), snack.get()))
  SubmitButton.place(x=150, y=270)

  NewScreen.mainloop()
#Code block for Story2
def Story2(win):
    #Story text for the game after input's have been obtained from player.
    def final(tl: Toplevel, profession, noun, feeling, emotion,verb):
            text = f'''
            When I was a child, I wanted to become a {profession}
          but as I grew up I got into the {noun} and decided to become an
          engineer. Then I went into a job that I was not {feeling} at.
          After getting {emotion} I decided to do what I love.
          Despite getting lower{verb} than I used to get in my previous job.I am very
          feeling '''

            tl.geometry(newGeometry='500x550')
            #Defining format rules for the story text
            Label(tl, text='Story:',  wraplength=tl.winfo_width()).place(x=160, y=310)
            Label(tl, text=text,wraplength=tl.winfo_width()).place(x=0, y=330)
    #Calling for new screen to display questions for the player, and to display the story with players answers.
    NewScreen = Toplevel(win, bg='Grey')
    NewScreen.title("Ambitions")
    NewScreen.geometry('500x500')
    #Setting text locations for player input questions
    Label(NewScreen, text='Ambitions').place(x=150, y=0)
    Label(NewScreen, text='Enter a profession:').place(x=0, y=35)
    Label(NewScreen, text='Enter a noun:').place(x=0, y=70)
    Label(NewScreen, text='Enter a feeling:').place(x=0, y=110)
    Label(NewScreen, text='Enter a emotion:').place(x=0, y=150)
    Label(NewScreen, text='Enter a verb:').place(x=0, y=190)
    #Player input locations for Name, Enter a game, Enter a city, Enter the name of a plater, Enter the name of a drink, Enter the name of a snack
    Profession = Entry(NewScreen, width=17)
    Profession.place(x=250, y=35)
    Noun = Entry(NewScreen, width=17)
    Noun.place(x=250, y=70)
    Feeling = Entry(NewScreen, width=17)
    Feeling.place(x=250, y=105)
    Emotion= Entry(NewScreen, width=17)
    Emotion.place(x=250, y=150)
    Verb = Entry(NewScreen, width=17)
    Verb.place(x=250, y=190)
    #Submit button location rules and calling for player inputted answers to fill in the story text
    SubmitButton = Button(NewScreen, text="Submit", background="white", font=('Times', 12), command=lambda:final(NewScreen, Profession.get(), Noun.get(), Feeling.get(), Emotion.get(), Verb.get()))
    SubmitButton.place(x=150, y=270)
  
#format rules for initial select a story screen including, Title, size, Background color, text labels, and button connect to corresponding story.
Screen = Tk()
Screen.title("Mad Libs Mini-Game")
Screen.geometry('400x400')
Screen.config(bg="green",)
Label(Screen, text='Mad Libs Mini-Game', bg='light green').place(x=100, y=20)
Label(Screen, text='Select a story', bg='light green').place(x=120, y=60)
Story1Button = Button(Screen, text='A memorable day', font=("Times New Roman", 13,),command=lambda: Story1(Screen),bg='Light Green')
Story1Button.place(x=120, y=90)
Story2Button = Button(Screen, text='Ambitions', font=("Times New Roman", 13),command=lambda: Story2(Screen), bg='Light Green')
Story2Button.place(x=120, y=150)

Screen.update()
Screen.mainloop()
