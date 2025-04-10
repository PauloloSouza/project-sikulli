Settings.MoveMouseDelay = 0.2
running = True
r1 = Region(519,25,608,685);
lootIcon = Pattern("1686857793755.png").similar(0.80);
back = "1686858003534.png";
honey = "1687033582171.png";

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.CTRL, runHotkey)

def loot():
    if r1.exists (back):
        type (Key.F2);
        
def close():
    if exists (back) and not exists (lootIcon):
            type (Key.F1);

def heal():
    if not exists (Pattern("nl11.png").similar(0.85)) and exists (Pattern("1686853568558.png").similar(0.80)):
        type ("5");

def healPet():
    if not exists (Pattern("B483.png").similar(0.80)) and exists (Pattern("1686853659783.png").similar(0.80)):
        type ("3");
        
while running:
    heal();
    loot();
    healPet();
