running = True;
lado = 0;
temMob = True;
florVerm = Pattern("florDireita.png").similar(0.85);
volta = Pattern("volta.png").similar(0.69);
loot1 = Pattern("loot.png").similar(0.85);
reco = Pattern("reco.png").similar(0.79);
cercaVerde = Pattern("1697254269982.png").exact();
vasoCinza = Pattern("1697254475754.png").similar(0.90);

AssasAmar1 = "AssasAmar1.png";
AssasAmar2 = "AssasAmar2.png";
AssasAmar3 = "AssasAmar3.png";
AssasVerm1 = "1697253209369.png";
AssasVerm2 = "1697253185407.png";
AssasVerm3 = "1697253238418.png";
r1 = Region(673,304,183,190);
regR1 = Region(786,293,479,213);
regL1 = Region(255,293,475,212);
rLeft = Region(257,120,469,593);
rRight = Region(797,120,467,549);
def loot():
    if exists (loot1):
        type ("J");
        
def back():
    if exists (volta):
        type ("V");

def reconnect():
    if exists (reco):
        click (reco);

def procuraMob():
    reconnect();
    global temMob;
    temMob = True;
    while temMob:
        temMob = False;
        if r1.exists (AssasAmar1):
            type ("S");
            wait (8);
            loot();
            back();
            temMob = True;
        if r1.exists (AssasAmar2):
            type ("D");
            wait (8);
            loot();
            back();
            temMob = True;
        if r1.exists (AssasAmar3):
            type ("A");
            wait (8);
            loot();
            back();
            temMob = True;
        if r1.exists (AssasVerm1):
            type ("S");
            wait (7);
            loot();
            back();
            temMob = True;
        if r1.exists (AssasVerm2):
            type ("D");
            wait (7);
            loot();
            back();
            temMob = True;
        if r1.exists (AssasVerm3):
            type ("A");
            wait (7);
            loot();
            back();
            temMob = True;

def andaDireita():
    reconnect();
    global lado;
    global temMob;
    if (lado == 0):
        procuraMob();
        if (temMob == False):
            if rRight.exists (vasoCinza):
                lado = 1;
            if regR1.exists (florVerm):
                try:
                    regR1.click (florVerm);
                    back();
                    reconnect();
                    wait (6);
                except:
                    type ("D");
            else:
                reconnect();
                click (Location(1232, 395));
                wait (7);

def andaEsquerda():
    reconnect();
    global lado;
    global temMob;
    if (lado == 1):
        procuraMob();
        if (temMob == False):
            if rLeft.exists (cercaVerde):
                lado = 0;
            if regL1.exists (florVerm):
                try:
                    regL1.click (florVerm);
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
    procuraMob();
    andaDireita();
    andaEsquerda();