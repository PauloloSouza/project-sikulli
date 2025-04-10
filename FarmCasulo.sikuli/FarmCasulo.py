Settings.MoveMouseDelay = 0.2
running = True
r1 = Region(519,25,608,685);
casulo = Pattern("1686857793755.png").similar(0.80);
sair = "1686858003534.png";
mel = "1687033582171.png";

def runHotkey(event):
    global running
    running = False

Env.addHotkey(Key.F1, KeyModifier.CTRL, runHotkey)

def lootCasulo():
    if r1.exists (sair):
        type (Key.F2);
        
def fechar():
    if exists (sair) and not exists (casulo):
            type (Key.F1);

def cura():
    if not exists (Pattern("nl11.png").similar(0.85)) and exists (Pattern("1686853568558.png").similar(0.80)):
        type ("5");

def curaPet():
    if not exists (Pattern("B483.png").similar(0.80)) and exists (Pattern("1686853659783.png").similar(0.80)):
        type ("3");
        
while running:
    cura();
    lootCasulo();
    curaPet();