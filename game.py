def game():
    return 64

score = game()

try:
    with open('hiscore.txt', 'r') as f:
        hiscore = int(f.read())
except (FileNotFoundError, ValueError):
    hiscore = 0  # Default if file doesn't exist or is empty

# Update high score if current score is higher
if score > hiscore:
    with open('hiscore.txt', 'w') as f:
        f.write(str(score)) 