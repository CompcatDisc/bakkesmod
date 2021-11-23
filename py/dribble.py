from bakkesmod import Vector, Rotator
import math
from random import randint, choice


	
if gameWrapper.IsInTutorial():
	tut = gameWrapper.GetGameEventAsTutorial()
	player = tut.GetGameCar()
	ball = tut.GetBall()

	#xStart = randint(-1500, 1500) if randint(0, 1) is 1 else -randint(500, 1200)
	ballSpawn = Vector(randint(-1500, 1500), randint(-1700, 1700), 95)
	ballSpawnNorm = Vector(ballSpawn.X, ballSpawn.Y, ballSpawn.Z)
	ballSpawnNorm.Normalize()
	
	#ballSpawnNorm*Vector(randint(300, 800), randint(300, 800), 0)
	carSpawn = ballSpawn - Vector(randint(300, 800), randint(300, 800), 65)
	
	ball.Stop()
	player.Stop()
	ball.SetLocation(ballSpawn)
	player.SetLocation(carSpawn)
	
	distToBall = (ballSpawn - carSpawn)
	distToBall.Normalize()
	carRot = bakpy.VectorToRotator(distToBall)
	carRot.yaw = carRot.yaw + randint(-5000, 5000)
	
	player.SetRotation(carRot)
	
	velocity = Vector(randint(700, 1400), randint(700, 1400), 0)
	
	ball.SetVelocity(velocity)
	player.SetVelocity(velocity)
	
def shootBall():
	ball.SetVelocity(ballVelocity)