class Car():
    def __init__(self, model, color):
        self.model = model
        self.color = color
        self.speed = 0

    def accelerate(self, speed):
        self.speed += speed
        self.speed = min(self.speed, 200)

    def brake(self, speed):
        self.speed -= speed
        self.speed = max(self.speed, 0)

    def get_speed(self):
        return self.speed
