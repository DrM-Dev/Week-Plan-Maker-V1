#Week_Plan_Maker_V1 by  Dr.M-Dev:
from prettytable import PrettyTable

print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')

def info():
    print('''      
    .::       ::::::::::::::::       ::.       
    !5B#&B.     :#&&&&&&&&&&&&&&#.     .B&#B5!    
  ^B@@@@@#      :@@@@@@@@@@@@@@@&.      #@@@@@G:  
  B@@@@@@#!!!!!~7@@@@@@@@@@@@@@@&7~!!!!!#@@@@@@G  
 :&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&: 
 :&@7:^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^:7@&: 
 :&@~                                        ~@&: 
 :&@~     :::::::    .::::::.    :::::::     ~@&: 
 :&@~    :&@@@@@B.   J@@@@@@?   .#@@@@@#.    ~@&: 
 :&@~    :&@@@@@#.   J@@@@@@?   .#@@@@@&.    ~@&: 
 :&@~    :&@@@@@#.   J@@@@@@?   .#@@@@@&.    ~@&: 
 :&@~                                        ~@&: 
 :&@~     :::::::    .::::::.    :::::::     ~@&: 
 :&@~    :&@@@@@B.   J@@@@@@?   .#@@@@@#.    ~@&: 
 :&@~    :&@@@@@#.   J@@@@@@?   .#@@@@@&.    ~@&: 
 :&@~    :&@@@@@#.   J@@@@@@?   .#@@@@@&.    ~@&: 
 :&@~     ~~~~~~^    :~~~~~~:    ^~~~~~^     ~@&: 
  B@5.                                      :G@B  
  :G@#J^::::::::::::::::::::::::::::::::::~Y&@G:  
    !5####################################&#5!    
       ''')

    print("******** WELCOME TO Week_Plan_Maker_V1  -   By: Dr.m DEV *********")
    print("This code will allow you to make a simple week planner using ASCII text-art ")

#==========================================================================================================
#______________________________________________________________Values:
table_obj = PrettyTable()
#------------------------
RUNNING = True
#------------------------
END_state = False
#------------------------Day Plans:
Days = { "sunday":[], "monday":[], "tuesday":[], "wednesday":[], "thursday":[], "friday":[], "saturday":[] }

def display():
    global END_state
    END_state = True
    #++++++++++
    global table_obj
    print("\n" * 50)
    print("Your schedule is done!")
    print(table_obj)


# #----------------------------------ESTABLISHING Planner
def establishing_planner():
    global Days

    table_obj.add_column("Time", ["Sunrise", "Morning", "Noon", "Afternoon", "sunset", "Evening", "Night time"])
    # ------FIXING DAYS: #--------MY FASTED FIXE EVER :)
    for day in Days:
        while len(Days[day]) < 7:
            Days[day].append("-EMPTY-")
    #------DAYS:
    table_obj.add_column("Sunday", Days["sunday"])
    table_obj.add_column("Monday", Days["monday"])
    table_obj.add_column("Tuesday", Days["tuesday"])
    table_obj.add_column("Wednesday", Days["wednesday"])
    table_obj.add_column("Thursday", Days["thursday"])
    table_obj.add_column("Friday", Days["friday"])
    table_obj.add_column("Saturday", Days["saturday"])

    display()

#____________________________________________Adding plans to said day:
def adding_plans(selected_day):
    global END_state
    global Days
    #----------
    Adding = True

    #---------------------------------------
    while Adding and END_state == False:
        # ---------------------------------------
        print(f"\n+++++++✅{selected_day} WAS SELECTED✅+++++++\n")
        Plan = input(f"\nAdd a new plan for {selected_day}, what would you like to add? \n[*]to select another day type \"change\"\n[*]if you are done planning type \"Done\"\nyour input:").lower()

        if Plan == "change":
            selecting_day(Plan)
        elif Plan == "done":
            Adding = False
            selecting_day(Plan)
        else:
            Days[selected_day].append(Plan)
            #++++++++++++++++
            print(f"\n ✅DONE! a plan was added to {selected_day}✅ \n")


#____________________________________________Selecting a day:
def selecting_day(state):
    global END_state
    Still_Selecting = True

    while Still_Selecting and END_state == False:
        if state == "change":
            choice = input("\nstart planning for which day, please type a day [Example: Sunday, Monday, ect...], \n[*]if you are done planning type \"Done\"\nyour input:").lower()
        # -----------
            if choice == "sunday" or choice == "monday" or choice == "tuesday" or choice == "wednesday" or choice == "thursday" or choice == "friday" or choice == "saturday":
                adding_plans(choice)
            # -----------
            else:
                print("<!> INVALID DAY NAME, please try again :( <!>")
        # -----------
        elif state == "done":
            Still_Selecting = False
            establishing_planner()



#______________________________________________________________Code Start:
def start_code():
    print("\n" * 50)
    global RUNNING
    RUNNING = True
    #=============Main Code:
    while RUNNING:
        info()
        #--------------
        choice = input('\nWanna start planning your week type "Start", "Restart" to restart the program, and "Off" to turn it off\nyour input:').lower()

        # -------Restart
        if choice == "restart":
            start_code()

        # -------Off
        elif choice == "off":
            RUNNING = False

        #----------------------------------Start
        elif choice == "start":
            RUNNING = False
            selecting_day("change")


        else:
            print("\n<!> INVALID INPUT, please chose one of the options \"start, restart, off\" <!>\n")

#-------------------------------------------------------------------start code:
start_code()
