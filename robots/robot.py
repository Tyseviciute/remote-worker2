import lgpio

# Set the pins for the motors
motor1_pin1 = 17
motor1_pin2 = 18

motor2_pin1 = 23
motor2_pin2 = 24

ena = 12
enb = 13
FREQ = 10000

# nustatomas kad galima butu juos naudoti
h = lgpio.gpiochip_open(0)
lgpio.gpio_claim_output(h, 17)
lgpio.gpio_claim_output(h, 18)
lgpio.gpio_claim_output(h, 23)
lgpio.gpio_claim_output(h, 24)
lgpio.gpio_claim_output(h, 12)
lgpio.gpio_claim_output(h, 13)


def move_backward(speed):
    # Set the motor1_pin1 to high and motor1_pin2 to low
    # Set the motor2_pin1 to high and motor2_pin2 to low
    lgpio.gpio_write(h, motor1_pin1, 1)
    lgpio.gpio_write(h, motor1_pin2, 0)
    lgpio.gpio_write(h, motor2_pin1, 1)
    lgpio.gpio_write(h, motor2_pin2, 0)
    lgpio.tx_pwm(h, ena, FREQ, speed)
    lgpio.tx_pwm(h, enb, FREQ, speed)


def move_forward(speed):
    # Set the motor1_pin1 to low and motor1_pin2 to high
    # Set the motor2_pin1 to low and motor2_pin2 to high
    lgpio.gpio_write(h, motor1_pin1, 0)
    lgpio.gpio_write(h, motor1_pin2, 1)
    lgpio.gpio_write(h, motor2_pin1, 0)
    lgpio.gpio_write(h, motor2_pin2, 1)
    lgpio.tx_pwm(h, ena, FREQ, speed)
    lgpio.tx_pwm(h, enb, FREQ, speed)


def turn_left(speed):
    # Set the motor1_pin1 to low and motor1_pin2 to high
    # Set the motor2_pin1 to high and motor2_pin2 to low
    lgpio.gpio_write(h, motor1_pin1, 0)
    lgpio.gpio_write(h, motor1_pin2, 1)
    lgpio.gpio_write(h, motor2_pin1, 1)
    lgpio.gpio_write(h, motor2_pin2, 0)
    lgpio.tx_pwm(h, ena, FREQ, speed)
    lgpio.tx_pwm(h, enb, FREQ, speed)


def turn_right(speed):
    # Set the motor1_pin1 to high and motor1_pin2 to low
    # Set the motor2_pin1 to low and motor2_pin2 to high
    lgpio.gpio_write(h, motor1_pin1, 1)
    lgpio.gpio_write(h, motor1_pin2, 0)
    lgpio.gpio_write(h, motor2_pin1, 0)
    lgpio.gpio_write(h, motor2_pin2, 1)
    lgpio.tx_pwm(h, ena, FREQ, speed)
    lgpio.tx_pwm(h, enb, FREQ, speed)


def stop_robot():
    # Set the motor1_pin1 and motor1_pin2 to low
    # Set the motor2_pin1 and motor2_pin2 to low
    lgpio.gpio_write(h, motor1_pin1, 0)
    lgpio.gpio_write(h, motor1_pin2, 0)
    lgpio.gpio_write(h, motor2_pin1, 0)
    lgpio.gpio_write(h, motor2_pin2, 0)
    lgpio.tx_pwm(h, ena, FREQ, 0)
    lgpio.tx_pwm(h, enb, FREQ, 0)
