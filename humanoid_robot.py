from machine import Pin, PWM
import utime

FREQ = 50
TRIG_PIN = 16
ECHO_PIN = 17

servo_pins = {
    "right_hip_fb": 0, "right_hip_io": 1, "right_knee": 2, "right_ankle": 3,
    "left_hip_fb": 4, "left_hip_io": 5, "left_knee": 6, "left_ankle": 7,
    "head_yaw": 8, "head_pitch": 9,
    "right_shoulder_fb": 10, "right_shoulder_io": 11, "right_elbow": 12,
    "left_shoulder_fb": 13, "left_shoulder_io": 14, "left_elbow": 15,
}

servos = {}
current_angles = {}
for name, pin_num in servo_pins.items():
    pwm = PWM(Pin(pin_num))
    pwm.freq(FREQ)
    servos[name] = pwm
    current_angles[name] = 90
    utime.sleep(0.02)


def angle_to_duty(angle, servo_name=None):
    min_us, max_us = 500, 2500
    if servo_name in [
        "right_hip_fb", "right_hip_io", "left_hip_fb", "left_hip_io",
        "right_knee", "left_knee", "right_ankle", "left_ankle"
    ]:
        min_us, max_us = 600, 2400
    us = min_us + (angle / 180) * (max_us - min_us)
    return int(us * 65535 // 20000)


def move_servo(name, angle):
    angle = max(0, min(180, angle))
    if name in servos:
        servos[name].duty_u16(angle_to_duty(angle, name))
        current_angles[name] = angle


def smooth_servo(name, target_angle, duration=0.25, step_time=0.02):
    start = current_angles.get(name, 90)
    target = max(0, min(180, target_angle))
    steps = max(1, int(duration / step_time))
    increment = (target - start) / steps
    for i in range(steps):
        move_servo(name, start + increment * (i + 1))
        utime.sleep(step_time)


def smooth_move_multiple(moves, duration=0.35, step_time=0.02):
    profiles = {}
    steps = max(1, int(duration / step_time))

    for name, target in moves.items():
        start = current_angles.get(name, 90)
        target = max(0, min(180, target))
        increment = (target - start) / steps
        profiles[name] = (start, increment)

    for i in range(steps):
        for name, (start, increment) in profiles.items():
            move_servo(name, start + increment * (i + 1))
        utime.sleep(step_time)


def merge_moves(*parts):
    merged = {}
    for part in parts:
        if part:
            merged.update(part)
    return merged


poses = {
    "neutral": {name: 90 for name in servo_pins},
    "support_left": {
        "left_hip_fb": 115, "left_hip_io": 105, "left_knee": 70, "left_ankle": 78,
        "right_hip_fb": 80, "right_hip_io": 70, "right_knee": 110, "right_ankle": 110,
        "right_shoulder_fb": 120, "left_shoulder_fb": 60,
        "right_shoulder_io": 75, "left_shoulder_io": 105,
        "right_elbow": 80, "left_elbow": 100,
        "head_yaw": 90, "head_pitch": 88,
    },
    "support_right": {
        "right_hip_fb": 115, "right_hip_io": 75, "right_knee": 70, "right_ankle": 78,
        "left_hip_fb": 80, "left_hip_io": 110, "left_knee": 110, "left_ankle": 110,
        "left_shoulder_fb": 120, "right_shoulder_fb": 60,
        "left_shoulder_io": 105, "right_shoulder_io": 75,
        "left_elbow": 80, "right_elbow": 100,
        "head_yaw": 90, "head_pitch": 88,
    },
    "kick_right": {
        "left_hip_fb": 120, "left_hip_io": 105, "left_knee": 65, "left_ankle": 80,
        "right_hip_fb": 40, "right_hip_io": 85, "right_knee": 30, "right_ankle": 95,
        "right_shoulder_fb": 130, "right_shoulder_io": 65, "right_elbow": 40,
        "left_shoulder_fb": 55, "left_shoulder_io": 115, "left_elbow": 75,
        "head_pitch": 65, "head_yaw": 95,
    }
}


def set_pose(pose_name):
    if pose_name in poses:
        smooth_move_multiple(poses[pose_name])


trig = Pin(TRIG_PIN, Pin.OUT)
echo = Pin(ECHO_PIN, Pin.IN)


def read_distance(timeout_us=30000):
    trig.low()
    utime.sleep_us(5)
    trig.high()
    utime.sleep_us(10)
    trig.low()

    start_wait = utime.ticks_us()
    while echo.value() == 0:
        if utime.ticks_diff(utime.ticks_us(), start_wait) > timeout_us:
            return None
    pulse_start = utime.ticks_us()

    while echo.value() == 1:
        if utime.ticks_diff(utime.ticks_us(), pulse_start) > timeout_us:
            return None
    pulse_end = utime.ticks_us()

    duration = utime.ticks_diff(pulse_end, pulse_start)
    return (duration / 2) / 29.1


HEAD_SCAN_POINTS = [
    {"head_yaw": 60, "head_pitch": 94},
    {"head_yaw": 85, "head_pitch": 88},
    {"head_yaw": 100, "head_pitch": 88},
    {"head_yaw": 120, "head_pitch": 94},
]


def sweep_head(dwell=0.12):
    for target in HEAD_SCAN_POINTS:
        smooth_move_multiple(target, duration=dwell, step_time=0.015)
        utime.sleep(dwell / 2)


def arm_swing(phase="left"):
    if phase == "left":
        return {
            "left_shoulder_fb": 60,
            "left_shoulder_io": 105,
            "left_elbow": 95,
            "right_shoulder_fb": 120,
            "right_shoulder_io": 75,
            "right_elbow": 85,
        }
    else:
        return {
            "left_shoulder_fb": 120,
            "left_shoulder_io": 75,
            "left_elbow": 85,
            "right_shoulder_fb": 60,
            "right_shoulder_io": 105,
            "right_elbow": 95,
        }


def walk_cycle(steps=2, cadence=0.4):
    left_phase = [
        merge_moves(
            {
                "left_hip_io": 112, "right_hip_io": 72,
                "left_hip_fb": 115, "right_hip_fb": 70,
                "left_knee": 80, "right_knee": 110,
                "left_ankle": 82, "right_ankle": 105,
            },
            arm_swing("left"),
            HEAD_SCAN_POINTS[0]
        ),
        merge_moves(
            {
                "left_hip_io": 105, "right_hip_io": 80,
                "left_hip_fb": 120, "right_hip_fb": 55,
                "left_knee": 75, "right_knee": 125,
                "left_ankle": 85, "right_ankle": 112,
            },
            arm_swing("left"),
            HEAD_SCAN_POINTS[1]
        ),
    ]

    right_phase = [
        merge_moves(
            {
                "left_hip_io": 78, "right_hip_io": 108,
                "left_hip_fb": 70, "right_hip_fb": 115,
                "left_knee": 110, "right_knee": 80,
                "left_ankle": 105, "right_ankle": 82,
            },
            arm_swing("right"),
            HEAD_SCAN_POINTS[2]
        ),
        merge_moves(
            {
                "left_hip_io": 85, "right_hip_io": 102,
                "left_hip_fb": 55, "right_hip_fb": 120,
                "left_knee": 125, "right_knee": 75,
                "left_ankle": 112, "right_ankle": 85,
            },
            arm_swing("right"),
            HEAD_SCAN_POINTS[3]
        ),
    ]

    for _ in range(steps):
        for phase in left_phase:
            smooth_move_multiple(phase, duration=cadence, step_time=0.015)
        for phase in right_phase:
            smooth_move_multiple(phase, duration=cadence, step_time=0.015)

    set_pose("neutral")


def handle_obstacle():
    print("⚠️ Obstacle detected – scanning and kicking")
    smooth_move_multiple({"head_pitch": 65})
    sweep_head(dwell=0.07)
    set_pose("support_left")
    set_pose("kick_right")
    utime.sleep(0.8)
    set_pose("neutral")


def main_loop():
    set_pose("neutral")
    while True:
        distance = read_distance()
        if distance is not None:
            print("Distance: {:.2f} cm".format(distance))
        else:
            print("Distance: timeout")

        if distance is not None and distance < 20:
            handle_obstacle()
        else:
            walk_cycle(steps=1, cadence=0.35)


try:
    main_loop()
except KeyboardInterrupt:
    print("🛑 Program stopped. Resetting to neutral pose.")
    set_pose("neutral")
