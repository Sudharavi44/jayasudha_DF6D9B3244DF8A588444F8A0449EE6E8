#define the base class player
class Player:
  def play(self):
    print("The Player is playing cricket.")
#define the derived class batsman
class Batsman(Player):
  def play(self):
    print("The Batsman is batting.")
    #define the derived class bowler
class Bowler(Player):
 def play(self):
    print("The Bowler is bowling.")
   
batsman=Batsman()
bowler=Bowler()
player=Player()

player.play()
batsman.play()
bowler.play()
