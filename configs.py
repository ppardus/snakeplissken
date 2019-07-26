FPS = 10

W_WIDTH, W_HEIGHT = 150, 150

BLACK = (0, 0, 0)
GRAY = (128, 128, 128)
CRIMSON = (220, 20, 60)
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)

SNAKE_SIZE = 10
SNAKE_SEPARATION = 1
WALL_SIZE = SNAKE_SIZE
APPLE_SIZE = SNAKE_SIZE
APPLE_QTD = 1
APPLE_PRIZE = 1.0
APPLE_RELOAD_TIME = 10  # IN SECONDS

KEY = {"UP": 1, "DOWN": 2, "LEFT": 3, "RIGHT": 4}

# Deep Learning Params
IMG_SIZE = 50
BATCH_SIZE = 128
GAMMA = 0.999
EPS_START = 0.9
EPS_END = 0.02
EPS_DECAY = 15_000
TARGET_UPDATE = 1500
MEM_LENGTH = 2_500
LEARNING_RATE = 1e-1
MOMENTUM = 0.9
