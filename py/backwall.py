from bakkesmod import Vector, Rotator
import math
from random import randint, choice

def vectorToRotator(v):
	rot = Rotator()
	rot.Yaw = math.Atan2(v.Y, v.X) * 10430.3783504704527
	rot.Pitch = math.Atan2(v.Z, math.Sqrt((v.X*v.X) + (v.Y * v.Y))) * 10430.3783504704527
	rot.Roll = 0
	return rot
	
if gameWrapper.IsInTutorial():
	tut = gameWrapper.GetGameEventAsTutorial()
	player = tut.GetGameCar()
	ball = tut.GetBall()

	ballSpawn = Vector(randint(-3261, 713), randint(-0, 2566), randint(18, 600))

	carSpawn = Vector(randint(-3777, -837), randint(-3891, -2946), 25)
	carSpawnRotation = Rotator(-100, randint(-23600, -9475), 0)
	ball.Stop()
	player.Stop()

	
	endLocation = Vector(randint(-3756, -983), randint(-5500, -4262), randint(600, 1900))
	
	if randint(0, 1) == 1:
		carSpawn.X = -carSpawn.X
		ballSpawn.X = -ballSpawn.X
		endLocation.X = -endLocation.X
		
	ball.SetLocation(ballSpawn)
	player.SetLocation(carSpawn)
	player.SetRotation(carSpawnRotation)
	velocity = tut.GenerateShot(ballSpawn, endLocation, randint(600, 1100))
	ball.SetVelocity(velocity)
	#player.SetVelocity(Vector)
	
def shootBall():
	ball.SetVelocity(ballVelocity)