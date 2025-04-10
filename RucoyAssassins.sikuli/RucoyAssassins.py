running = True;
side = 0;
monster = True;
redFlower = Pattern("florDireita.png").similar(0.85);
backIcon = Pattern("volta.png").similar(0.69);
loot1 = Pattern("loot.png").similar(0.85);
reco = Pattern("reco.png").similar(0.79);
greenPlant = Pattern("1697254269982.png").exact();
grayJar = Pattern("1697254475754.png").similar(0.90);

redMob1 = "AssasAmar1.png";
redMob2 = "AssasAmar2.png";
redMob3 = "AssasAmar3.png";
yellowMob1 = "1697253209369.png";
yellowMob2 = "1697253185407.png";
yellowMob3 = "1697253238418.png";
r1 = Region(673,304,183,190);
regR1 = Region(786,293,479,213);
regL1 = Region(255,293,475,212);
rLeft = Region(257,120,469,593);
rRight = Region(797,120,467,549);
def loot():
    if exists (loot1):
        type ("J");
        
def back():
    if exists (backIcon):
        type ("V");

def reconnect():
    if exists (reco):
        click (reco);

def findMonster():
    reconnect();
    global monster;
    monster = True;
    while monster:
        monster = False;
        if r1.exists (yellowMob1):
            type ("S");
            wait (8);
            loot();
            back();
            monster = True;
        if r1.exists (yellowMob2):
            type ("D");
            wait (8);
            loot();
            back();
            monster = True;
        if r1.exists (yellowMob3):
            type ("A");
            wait (8);
            loot();
            back();
            monster = True;
        if r1.exists (redMob1):
            type ("S");
            wait (7);
            loot();
            back();
            monster = True;
        if r1.exists (redMob2):
            type ("D");
            wait (7);
            loot();
            back();
            monster = True;
        if r1.exists (redMob3):
            type ("A");
            wait (7);
            loot();
            back();
            monster = True;

def walkRight():
    reconnect();
    global side;
    global monster;
    if (side == 0):
        findMonster();
        if (monster == False):
            if rRight.exists (grayJar):
                lado = 1;
            if regR1.exists (redFlower):
                try:
                    regR1.click (redFlower);
                    back();
                    reconnect();
                    wait (6);
                except:
                    type ("D");
            else:
                reconnect();
                click (Location(1232, 395));
                wait (7);

def walkLeft():
    reconnect();
    global side;
    global monster;
    if (side == 1):
        findMonster();
        if (monster == False):
            if rLeft.exists (greenPlant):
                lado = 0;
            if regL1.exists (redFlower):
                try:
                    regL1.click (redFlower);
                    back();
                    reconnect();
                    wait (6);
                except:
                    type ("A");
            else:
                reconnect();
                click (Location(389, 403));
                wait (7);
               
def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F2, KeyModifier.CTRL, runHotkey)

while running:
    findMonster();
    walkRight();
    walkLeft();
