import bakkesmod
import time
tut = gameWrapper.GetGameEventAsTutorial()

player = tut.GetGameCar()
ball = tut.GetBall()
shot = tut.GenerateShot(ball.GetLocation(), player.GetLocation(), 1300)

bakkesmod.Plugin.SetTimeout("shootie", 900)

def shootie():
	ball.SetVelocity(shot)
	console.LogToChatbox("VEL X: " + str(shot.X) + ", Y:" + str(shot.Y) + ", Z:" + str(shot.Z))