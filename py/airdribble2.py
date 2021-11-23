from bakkesmod import Vector, Rotator
import math
from random import randint, choice


if gameWrapper.IsInTutorial():
	tut = gameWrapper.GetGameEventAsTutorial()
	player = tut.GetGameCar()
	ball = tut.GetBall()

	randomSpawnLoc = Vector(randint(-3800, 3800), randint(-4500, 4500), 35)
	goalNo = 0 if randomSpawnLoc.Y > 0 else 1 #determine which goal
	ballDest = tut.GenerateGoalAimLocation(goalNo, randomSpawnLoc)
	faceVec = ballDest - randomSpawnLoc
	faceVec.Normalize()
	playerRot = bakpy.VectorToRotator(faceVec)

	player.Stop()
	player.SetLocation(randomSpawnLoc)
	player.SetRotation(playerRot)
	player.SetVelocity(Vector(500, 500, 0) * faceVec)

	ballLoc = randomSpawnLoc + Vector(250)*faceVec + Vector(0, 0, 53)
	ball.Stop()
	ball.SetLocation(ballLoc)
	#randint(*(choice([(-900, -500), (300, 500)])))
	ballVelocity = Vector(600)*faceVec + Vector(0, 0, 300)

	bakpy.SetTimeout("shootBall", .11)
	
def shootBall():
	ball.SetVelocity(ballVelocity)