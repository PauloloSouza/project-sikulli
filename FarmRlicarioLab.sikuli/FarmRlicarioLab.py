running = True
i = 0
t = 20
box = Pattern("box.png").similar(0.50)
box2 = "box2.png"
r1 = Region(268,304,472,405)

r2 = [(Location(454, 642)), (Location(500, 639)), (Location(552, 644)), (Location(598, 632))];

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F2, KeyModifier.CTRL, runHotkey)

def lootBox():
    if r1.exists (box):
        r1.click(box);

def cura():
    if not exists (Pattern("nl11.png").similar(0.85)) and exists (Pattern("1686853568558.png").similar(0.80)):
        type ("5");

def curaPet():
    if not exists (Pattern("B483.png").similar(0.80)) and exists (Pattern("1686853659783.png").similar(0.80)):
        type ("3");
        
while running:
    cura();
    curaPet();
    #lootBox();

    if exists (box2):
        type (Key.F2);