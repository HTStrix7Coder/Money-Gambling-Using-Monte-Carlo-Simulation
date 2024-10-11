import random
import matplotlib.pyplot as plt
import time
#1.create a rollDice Function to determine wether the user wins or not
#2.create a simple bettor to and import the random winners and losers into it
#3.checking results
#4.create a doubler better where everytime we lose we double our betting amount
#5.comparing and analyzing both simpler bettor and doubler bettor
#6.Both Statergies lose the same amount but gains are different
#7.for a short time frame life expectency simple bettor is better but for a long time frame doubler bettor is better
#8.calculating the bustand profits for the bettors
#9.using Multiple bettor for using monte carlo simulator
lower_bust = 31.235
higher_profit = 63.208
samplesize = 1000
startingfunds = 10000
wagersize = 10
wagercount = 10000
da_busts = 0.0
da_profits = 0.0
#the simple bettor will win in short term but in a long term they will lose
def rollDice():
    roll = random.randint(1, 100)
    if roll == 100:
        return False
    elif roll <= 50:
        return False
    elif 100 > roll > 50:
        return True

#50/50 odds Statergy
#every time you lose or win we are increasing the wager size
def dAlembert(funds, initial_wager, wager_count):
    global da_busts
    global da_profits
    value = funds
    wager = initial_wager
    current_wager = 1
    previous_wager = 'win'
    previous_wager_amount = initial_wager
    while current_wager <= wager_count:
        if previous_wager == 'win':
            if wager==initial_wager:
                pass
            else:
                wager-=initial_wager
            print('Current Wager:',wager,'Value:',value)
            if rollDice():
                value+=wager
                print('we won,current value:',value)
                previous_wager_amount=wager
            else:
                value-=wager
                previous_wager='loss'
                print('we lost,current value',value)
                previous_wager_amount=wager

                if value <=0:
                    da_busts+=1
                    break
        elif previous_wager == 'loss':
            wager=previous_wager_amount + initial_wager
            if(value-wager)<=0:
                wager=value
            print('lost the last wager,current wager:',wager,'value',value)
            if rollDice():
                value+=wager
                print('we won current value:',value)
                previous_wager_amount=wager
                previous_wager='Win'
            else:
                value-=wager
                print('we won current value:',value)
                previous_Wager_amount=wager
                
                if value<=0:
                    da_busts+=1
                    break
        current_wager+=1
    if value > funds:
        da_profits+=1
#dAlembert(startingfunds,wagersize,wagercount)
time.sleep(555555)             
def multiple_bettor(funds, initial_wager, wager_count):
    global multiple_busts
    global multiple_profits
    value=funds
    wager=initial_wager
    wX=[]
    vY=[]
    current_wager=1
    previous_wager='Win'
    previous_wager_amount = initial_wager
    while current_wager <= wager_count:
        if previous_wager == 'Win':
            if rollDice():
                value += wager
                wX.append(current_wager)
                vY.append(value)
            else:
                value -= wager
                previous_wager = 'Loss'
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)
                if value <= 0:
                    multiple_busts += 1
                    break
        elif previous_wager == 'Loss':
            #print 'we lost the last one so we will be smart and double'
            if rollDice():
                wager = previous_wager_amount * random_multiple
                if(value-wager)<0:
                    wager=value
                    #wagering only what we left not going into the negative
                value += wager
                wager = initial_wager
                previous_wager = 'Win'
                wX.append(current_wager)
                vY.append(value)
            else:
                wager = previous_wager_amount * random_multiple
                if(value-wager)<0:
                    wager=value
                value -= wager
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)
                if value <= 0:
                    multiple_busts += 1
                    break
                previous_wager = 'Loss'

        current_wager += 1

    #plt.plot(wX, vY,color)# cyan color for doubler bettor
    if value > funds:
        multiple_profits+=1
    
def simple_better(funds, initial_wager, wager_count,color):
    global simple_busts
    global simple_profits
    value = funds
    wager = initial_wager
    wX = []  # wager values
    vY = []  # funds
    current_wager = 1
    while current_wager <= wager_count:
        if rollDice():
            value += wager
            wX.append(current_wager)  # wager Count
            vY.append(value)  # appending the funds
        else:
            value -= wager
            wX.append(current_wager)
            vY.append(value)

        current_wager += 1
    if value <= 0:
        value = 'Broke'
        simple_busts += 1
    plt.plot(wX, vY,color)  # plotting the graph
    if value != 'Broke' and value > funds:
        simple_profits += 1

def doubler_better(funds, initial_wager, wager_count,color):
    value = funds
    wager = initial_wager
    global doubler_busts
    global doubler_profits
    wX = []  # wager values
    vY = []  # funds
    current_wager = 1
    previous_wager = 'Win'
    previous_wager_amount = initial_wager
    while current_wager <= wager_count:
        if previous_wager == 'Win':
            if rollDice():
                value += wager
                wX.append(current_wager)
                vY.append(value)
            else:
                value -= wager
                previous_wager = 'Loss'
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)
                if value <= 0:
                    doubler_busts += 1
                    break
        elif previous_wager == 'Loss':
            #print 'we lost the last one so we will be smart and double'
            if rollDice():
                wager = previous_wager_amount * 2
                if(value-wager)<0:
                    wager=value
                    #wagering only what we left not going into the negative
                value += wager
                wager = initial_wager
                previous_wager = 'Win'
                wX.append(current_wager)
                vY.append(value)
            else:
                wager = previous_wager_amount * 2
                if(value-wager)<0:
                    wager=value
                value -= wager
                previous_wager_amount = wager
                wX.append(current_wager)
                vY.append(value)
                if value <= 0:
                    doubler_busts += 1
                    break
                previous_wager = 'Loss'

        current_wager += 1

    plt.plot(wX, vY,color)# cyan color for doubler bettor
    if value > funds:
        doubler_profits+=1

x = 0
while True:
    multiple_busts = 0.0
    multiple_profits = 0.0
    multiplesampsize = 100000
    currentSample=1
    random_multiple=random.uniform(0.1,10.0)
    while currentSample <= multiplesampsize:
        simple_better(startingfunds, wagersize, wagercount,'c')
        doubler_better(startingfunds, wagersize, wagercount,'k')
        #multiple_bettor(startingfunds, wagersize, wagercount)
        currentSample+=1
    if ((multiple_busts/multiplesampsize)*100.00 < lower_bust) and ((multiple_profits/multiplesampsize)*100.00 > higher_profit):
        print('#####################')
        print('Found a winner:',random_multiple)
        print('Lower bust to beat',lower_bust)
        print('Higher profit rate to beat:',higher_profit)
        print('bust rate;',(multiple_busts/multiplesampsize)*100.00)
        print('Profit rate:',(multiple_profits/multiplesampsize)*100.00)
        print('#######################')
print("Results after 100 simulations:")
print("Simple Bettor Busts:", simple_busts)
print("Simple Bettor Profits:", simple_profits)
print("Doubler Bettor Busts:", doubler_busts)
print("Doubler Bettor Profits:", doubler_profits)
print("D'Alembert Busts:", da_busts)
print("D'Alembert Profits:", da_profits)
