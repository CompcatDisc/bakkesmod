from bakkesmod import Vector, Rotator
import math
from random import randint, choice


ballVelocity = Vector(0)

if gameWrapper.IsInTutorial():
	tut = gameWrapper.GetGameEventAsTutorial()
	player = tut.GetGameCar()
	ball = tut.GetBall()

	playerStart = Vector(randint(-3000, 3300), randint(600, 3000), 65)
	playerStartRot = Rotator(0, randint(-32000, 32000), 0)
	player.Stop()
	player.SetLocation(playerStart)
	player.SetRotation(playerStartRot)
	
	ballStart = Vector(randint(-3000, 3300), -randint(600, 3000), randint(100, 1500))
	ball.Stop()
	ball.SetLocation(ballStart)
	
	#playerStartRot.Yaw -= 32000
	#playerStartRot.Roll = 0
	behind = bakpy.RotatorToVector(playerStartRot)
	
	behind.Normalize()
	playerAwkwardSpot = playerStart - behind * Vector(randint(400, 600), randint(500, 800), randint(0, 200))
	player.SetVelocity(behind * Vector(800, 800, 0))
	
	ballVelocity = tut.GenerateShot(ballStart, playerAwkwardSpot, randint(700, 1000))
	
	
	bakpy.SetTimeout("shootBall", .3)
	
def shootBall():
	ball.SetVelocity(ballVelocity)