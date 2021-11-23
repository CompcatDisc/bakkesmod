from bakkesmod import Vector, Rotator
import math
from random import randint, choice

	
if gameWrapper.IsInTutorial():
	tut = gameWrapper.GetGameEventAsTutorial()
	player = tut.GetGameCar()
	ball = tut.GetBall()

	xStart = randint(500, 1200) if randint(0, 1) is 0 else -randint(500, 1200)
	ballSpawn = Vector(xStart, randint(-1700, 1700), 95)
	ballSpawnNorm = Vector(ballSpawn.X, ballSpawn.Y, ballSpawn.Z)
	ballSpawnNorm.Normalize()
	carSpawn = ballSpawn - (ballSpawnNorm*Vector(500, 100, 0)) - Vector(0, min(xStart * 2, 2000), 65)
	
	impact = ballSpawn - (ballSpawnNorm*Vector(500, 100, 0))
	
	ball.Stop()
	player.Stop()
	ball.SetLocation(ballSpawn)
	player.SetLocation(carSpawn)
	
	distToBall = (ballSpawn - impact)
	distToBall.Normalize()
	carRot = bakpy.VectorToRotator(distToBall)
	player.SetRotation(carRot)
	ball.SetVelocity(distToBall * Vector(randint(2000, 3000), 1200, 0))
	player.SetVelocity(distToBall * Vector(1200, 1200, 0))
	
	#tut.GetPlayers().Get(0).SetLocation(Vector(-1400))
def shootBall():
	ball.SetVelocity(ballVelocity)