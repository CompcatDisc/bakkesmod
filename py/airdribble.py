from bakkesmod import Vector, Rotator
import math

tut = gameWrapper.GetGameEventAsTutorial()

player = tut.GetGameCar()
ball = tut.GetBall()
playerLoc = player.GetLocation()
ballLoc = ball.GetLocation()

distToBall = 400
if ballLoc.Y > 0:
	distToBall = -distToBall
	
destLocation = Vector(ballLoc.X - 50, ballLoc.Y - distToBall, 40)

newRotNorm = ballLoc - destLocation 
newRotNorm.Normalize()
newRot = bakpy.VectorToRotator(newRotNorm)
newRot.Pitch = 0 #Just want yaw
newRotNorm.Z = 0
player.Stop()

player.SetLocation(destLocation)
player.SetRotation(newRot)
player.SetVelocity(Vector(400) * newRotNorm)

ball.Stop()
ball.SetLocation(Vector(ballLoc.X, ballLoc.Y, 100))

newBallVel = Vector(500, 500, 0) * newRotNorm
newBallVel.Z = 400
ball.SetVelocity(newBallVel)
#shot = tut.GenerateShot(ball.GetLocation(), player.GetLocation(), 1300)
