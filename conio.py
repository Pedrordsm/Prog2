def home():
  print(chr(27) + "[H")

def cls():
  print(chr(27) + "[2J")
  home()

def gotoyx(y, x):
  comando = chr(27) + "[" + str(y) + ";" + str(x) + "H"
  print(comando,end="")
    
def cordochar(cc):
    print(chr(27) + '[' + str(cc) + 'm',end='')
# fim cordochar