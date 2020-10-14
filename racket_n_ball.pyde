ballX = 0
ballY = 0
ballSpeedX = 5
ballSpeedY = 2
ballRadius = 5

racketWidth = 50
racketX = 0
racketY = 0

#ici on définit la fonction setup qui sera executée comme point d'entrée dans mon code
def setup():
    #on dit qu'on va faire référence à la variable globale
    global ballX, ballY, racketX, racketY, racketWidth
    
    #on appelle la fonction print pour écrire dans la console
    print("Hello World")
    size(400, 400)
    clear()
    frameRate(60)
    ballX = width/2
    ballY = height/2
    
    racketX = mouseX - (racketWidth/2)
    racketY = height - 20
    
def draw():
    clear()
    drawRacket()
    drawBall()
    
def drawRacket():
    global racketX, racketY, racketWidth
    print("test function")
    #draw a rectangle in coords
    # x : mouseX minus half of width
    # y : height of the window minus 20
    racketX = mouseX - (racketWidth/2)
    rect(racketX, racketY, racketWidth, 10)

def drawBall():
    global ballX, ballY, ballSpeedX, ballSpeedY, ballRadius, racketX, racketY, racketWidth
    global racketX, racketY, racketWidth
    
    #ballX = ballX + ballSpeedX
    #ballY = ballY + ballSpeedY
    #idem à ce qu'il y a au-dessus
    ballX += ballSpeedX
    ballY += ballSpeedY

    #haut et bas
    if(ballY-ballRadius < 0):
        ballSpeedY *= -1
        ballY = ballRadius
    elif(ballY+ballRadius > height):
        ballSpeedY *= -1
        ballY = height-ballRadius

    #droite et gauche
    if(ballX+ballRadius > width):
        ballSpeedX *= -1
        ballX = width-ballRadius
    elif(ballX-ballRadius < 0):
        ballSpeedX *= -1
        ballX = ballRadius
    
            
        #si la position x de la balle est superieure au coté gauche de la balle et que la position x da la balle est inférieure au coté droite de la balle
          #if(postionX de la balle > coté gauche) and (postionX de la balle < coté droit):
    if(ballY+ballRadius > racketY):
        if(racketX - (racketWidth/2) < ballX < racketX + (racketWidth/2)):
            ballSpeedY *= -1
            ballY = racketY-ballRadius
    
    #draw circle
    circle(ballX, ballY, 2*ballRadius)
