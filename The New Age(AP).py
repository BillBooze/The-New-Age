Player="You are a Terran hailing from the planet of Primis. Your one dream in life has been to explore the galaxy, and after scrounging enough currency for the past three years, you finally had enough to pay for a pilot."
Coronam="The Coronam Sector is considered the trade hub of the galaxy. Home to the crown jewel of the Terran Empire, Premio, a planet spanning city. And it's trash planet Deformem, where Premio's refuse is dumped. While the sector is officially explored, there are still many secrets yet undiscovered."
Yabani="The newly discovered Yabani sector is a smugglers dream. With little law enforcement and barely explored planets, this is the perfect place to lay low. Home to Vaha, a lush jungle planet that has barely been touched by the Terran empire. And Oncu, the only planet in the sector that has law enforcement."
Premio="As long as you stay on the upper levels of Premio you are in one of the safest places in the galaxy. But travel further down at your own risk, laws are meaningless on lower levels, and no. Make sure to keep a lookout for pickpockets, muggers, and species looking to harvest your body parts. Despite being the trade hub of the empire, Premio is teetering on the edge of political collapse. The two parties of the planet the Sinistram and the Iustum are vying for domination of the planet and the thus the entire Terran Empire."
Deformem="Deformem's only purpose is to hold Premio's trash. With only .1% of its surface not covered in trash, it is one of the most toxic places in the galaxy. All those that land on this planent are advised to remain on the .1%, for there are rumors that all those that travel beyond are eaten by the mutated natives of the planet. Despite this there are those who hunt through the trash looking for scrap, and treasures accidentaly thrown away."
Vaha="The jungle planet of Vaha may seem like a lush paradise on the surface. But to the experinced explorer they know that it is filled to the brim with poisonous and man-eating plants, venomous amphibians and reptiles, and a lizard people native to the world that don't appreciate outsiders."
Hapis="Upon it's discovery Hapis was noted for it's large reserves of Ypah, a radioactive metal essential to Celeratias drives. The Terraran Military thus decided to convert it into a prison that houses the worst criminals in the galaxy. Due to the dangerous labor the criminals are forced to do, the life expectancy on the planet is less than 2 months."
Axol="Arguably one of the best pilots in the galaxy, Axol has broken many records for traveling from sector to sector. Despite his skill, he is known for taking risky routes, and performing almost suicidal maneuvers."
Pental="A seasoned pilot who once flew politicians from planet to planet, Pental may perhaps be the safest pilot in the galaxy. Though fallen from grace, his piloting skills are still legendary"
Ryby="An aquaticus from the planet Morska Riasa, Ryby is a genius when it comes to ships, it's even rumored he can communicate with the ship he is fixing. But due to his species being seen as inferior, Ryby is often heavily discriminated against."
Bob="Your childhood best friend, although he isn't the greatest mechanic, he is fearless. He has been by your side through thick and thin and doesn't plan to change that now."
characterList=()
p=5
print"Welcome to the New Age."
print""
print Player
print""
while p==5:
    p=5
    print"Who would you like as your pilot?"
    print""
    print Axol
    print''
    print"Or" 
    print''
    print Pental
    print''
    print"Axol or Pental?"
    choice=str(raw_input())
    if choice.lower()=="axol":
        print"Is this who you choose as your pilot? Yes or no?"
        choice=str(raw_input())
        if choice.lower()=="yes":
            print""
            print"You have chosen Axol as your pilot."
            print""
            while p==5:
                print"Axol: All right kid I'll bite, just a few things though. When we are on my ship I call the shots, also no complaining about my flying. Got it?" 
                print''
                print"Yes or No?"
                choice=str(raw_input())
                if choice.lower()=="yes":
                    print"Axol: All right, one thing who is gonna be our mechanic?"
                    while p==5:
                        print"Who would you like as your mechanic?"
                        print''
                        print Ryby
                        print''
                        print"Or"
                        print''
                        print Bob
                        print''
                        print"Ryby or Bob?"
                        choice=str(raw_input())
                        print''
                        if choice.lower()=="ryby":
                            print"Is this who you choose as your mechanic? Yes or No"
                            print''
                            if choice.lower()=='yes':
                                print"Ryby: You wanna hire me kid? I'm not welcome in most places."
                                print''
                                print"Player: Yes I want to hire you."
                                print''
                                print"Ryby: Dang kid, I guess I misjudged you."
                                print''
                                print"Axol: You hired an aquaticus? Good on you kid, they never get work."
        else:
            print""
            p=5
    if choice.lower()=="pental":
        print"Is this who you choose as your pilot? Yes or no?"
        choice=str(raw_input())
        if choice.lower()=="yes":
            print""
            print"You have chosen Pental as your pilot."
            
        else:
            print ""
            p=5