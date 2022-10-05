r1y = 200
r1x = 40
r2y = 200
r2x = 960
cy = 250
cx = 500
velocityx = 5
velocityy = 2
score1 = 0
score2 = 0
def setup():
    size(1000, 500)

def keyPressed():
    global r1y, r1x, r2y, r1x
    if key == 'w' or key == 'W':
        if r1y >= 10:
            r1y = r1y - 10
    if key == 's' or key == 'S':
        if r1y <= 390:
            r1y = r1y + 10
    
def draw():
    background(0)
    global r1y, r1x, r2y, r1x, velocityx, velocityy, cx, cy, score1, score2
    r2y = mouseY
    fill(225, 0, 0)
    rect(r1x, r1y, 10, 100)
    fill(0, 0, 225)
    rect(r2x, r2y, 10, 100)
    fill(0, 225, 0)
    circle(cx, cy, 40)
    cx = cx - velocityx 
    cy = cy + velocityy
    textSize(50)
    text(score1, 550, 250)
    fill(255, 255, 255)    
    textSize(50)
    text(score2, 450, 250)
    fill(255, 255, 255)
# Paddle 1 Hitting
    if cx <= r1x + 30 and cx >= r1x and cy - 20 <= r1y + 100 and cy >= r1y:
        velocityx = velocityx * -1
        velocityx /= -0.5 
        velocityy = velocityy * -1
        velocityy /= -0.5 
        cx = 71
        color(225, 0, 0)
# Speed Limit of the Ball
        if velocityx > -5:
            velocityx = -5
# Y axis border
    if cy >= 480 or cy <= 20:
        velocityy = velocityy * -1
# Score Keeper for Paddle 1
    if cx >= 999:
        score1 = score1 + 1
# Score Keeper for Paddle 2
    if cx <= 0:
        score2 = score2 + 1
# Reseting
    if cx >= 1000 or cx <= 0:
        cx = 500
        cy = 200
    if r2x <= 10 and cx >= r2x and cy <= r2y + 100 and cy >= r2y:
        velocityx = velocityx * -0.5
        velocityy = velocityy * -0.5
# Paddle 2 Hit Detection
    if cx >= r2x - 20 and cy + 20 <= r2y + 100 and cy >= r2y:
        velocityx = velocityx * -1.2
        velocityx /= random(0.8, 2.1)
        velocityy = velocityy * -1.2 
        velocityy /= random(0.8, 2.1)
        cx = 939
        color(225, 0, 0)
# Speed Limit of the Ball
        if velocityy< 5:
            velocityy = 5

        
