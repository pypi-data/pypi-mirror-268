class JCMath(object):
    def __init__(self, x=1.0, y=1.0, angle=0.6435):
        self.x = x
        self.y = y
        self.angle = angle
        self.pi = 3.1415926535897932384626433832795028841971693993751058209749445923

    def fmod(self, x, y):
        if y == 0.0:
            return 0.0
        quotient = x / y
        int_part = int(quotient)
        fractional_part = quotient - int_part
        result = x - y * int_part
        if (y > 0.0 and result < 0.0) or (y < 0.0 and result > 0.0):
            result += y
        return result

    def atan(self, x):
        if x == 0:
            return 0.0
        elif x > 0:
            result = x
            term = x
            sign = -1
            for n in range(3, 20, 2):
                term *= x * x
                result += sign * term / n
                sign *= -1
            return result
        else:
            return -self.atan(-x)

    def sin(self, angle):
        angle = self.fmod(angle, 2 * self.pi)
        if angle > self.pi:
            angle -= 2 * self.pi
        elif angle < -self.pi:
            angle += 2 * self.pi
        result = angle
        term = angle
        factorial = 1.0
        sign = -1
        for n in range(3, 20, 2):
            term *= angle * angle
            factorial *= n * (n - 1)
            result += sign * term / factorial
            sign *= -1

        return result

    def cos(self, angle):
        angle = self.fmod(angle, 2 * self.pi)
        if angle > self.pi:
            angle -= 2 * self.pi
        elif angle < -self.pi:
            angle += 2 * self.pi
        result = 1.0
        term = 1.0
        factorial = 1.0
        sign = -1
        for n in range(2, 21, 2):
            term *= angle * angle
            factorial *= n * (n - 1)
            result += sign * term / factorial
            sign *= -1

        return result

    def tan(self, angle):
        angle = self.fmod(angle, 2 * self.pi)
        if angle > self.pi / 2.0:
            angle -= self.pi
        elif angle < -self.pi / 2.0:
            angle += self.pi
        sin_angle = self.sin(angle)
        cos_angle = self.cos(angle)
        return sin_angle / cos_angle

    def atan2(self, y, x):
        if x > 0:
            return self.atan(y / x)
        elif x < 0 and y >= 0:
            return self.atan(y / x) + self.pi
        elif x < 0 and y < 0:
            return self.atan(y / x) - self.pi
        elif x == 0 and y > 0:
            return self.pi / 2.0
        elif x == 0 and y < 0:
            return -self.pi / 2.0
        elif x == 0 and y == 0:
            return 0.0

    def test(self):
        angle_atan2 = self.atan2(self.y, self.x)
        print(f"Angle between X-axis and line from ({self.x:.2f}, {self.y:.2f}) is {angle_atan2:.2f} radians.")

        sin_value = self.sin(self.angle)
        cos_value = self.cos(self.angle)
        tan_value = self.tan(self.angle)

        return sin_value, cos_value, tan_value, angle_atan2
    

if __name__ == '__main__':
    jcmath = JCMath()
    angle = jcmath.angle
    sin_value, cos_value, tan_value, angle_atan2 = jcmath.test()

    print(f"Sin of angle {angle:.2f} radians is {sin_value:.2f}")
    print(f"Cos of angle {angle:.2f} radians is {cos_value:.2f}")
    print(f"Tan of angle {angle:.2f} radians is {tan_value:.2f}")