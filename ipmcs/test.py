import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

print(os.path.join(BASE_DIR))
print(os.getenv('AWS_ACCESS_KEY_ID'))
print(os.getenv('USE_S3', 'not here'))
