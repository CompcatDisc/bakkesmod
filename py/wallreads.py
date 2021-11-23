from bakkesmod import Vector, Rotator
import math
from random import randint, choice

ballVelocity = Vector(0)
reverse = (randint(0, 1) == 1)
if gameWrapper.IsInTutorial():
	tut = gameWrapper.GetGameEventAsTutorial()
	player = tut.GetGameCar()
	ball = tut.GetBall()

	ballStart = Vector(randint(-3071, -843), randint(514,3911), randint(100, 1700))
	
	playerStart = Vector(randint(-3300, -400), randint(-2800, -900), 25)
	playerStartRot = Rotator(0, randint(12760, 20760), 0)
	playerStartVel = Vector(0, randint(800, 2100), 0)
	
	if reverse:
		ballStart.X = -ballStart.X 
		playerStart.X = -playerStartVel.X 
		
	player.Stop()
	player.SetLocation(playerStart)
	player.SetRotation(playerStartRot)
	player.SetVelocity(playerStartVel)
	ball.Stop()
	ball.SetLocation(ballStart)
	
	#playerStartRot.Yaw -= 32000
	#playerStartRot.Roll = 0
	
	dest = Vector(randint(-4071, -2200), randint(1381, 2502), randint(1250, 1616))
	if reverse:
		dest.X = -dest.X
	
	ballVelocity = tut.GenerateShot(ballStart, dest, randint(1100, 1400))
	
	
	bakpy.SetTimeout("shootBall", .3)
	
def shootBall():
	ball.SetVelocity(ballVelocity)
	ball.SetAngularVelocity(Vector(randint(-5000, 5000),randint(-5000, 5000),randint(-5000, 5000)))