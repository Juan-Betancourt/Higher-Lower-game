from art import logo, vs
from game_data import data
import random
from replit import clear

def format_data(account):
  """Takes account data and return the printable format"""
  name = account["name"]
  description = account["description"]
  country = account["country"]

  return f"{name} a {description} from {country}"


def check_answer(guess, a_followers, b_followers):
  """Check if user is correct"""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"
  
## Add Art
print(logo)

score=0
game_should_continue = True
account_b = random.choice(data)

## Make game repeatable
while game_should_continue:

## Make B the next A
  account_a = account_b
  account_b = random.choice(data)
  while account_a == account_b:
    account_b = random.choice(data)
  
  print(f"Compare A: {format_data(account_a)}")
  print(vs)
  print(f"Against B: {format_data(account_b)}")
    
#To-Do-List
## Generate a random account for the game_data
  
  def get_random_account():
    """Get data from a random account"""
    return random.choice(data)
  
## Ask the user for a guess
  guess = input("Who has more followers A or B? Type 'A' or 'B' ").lower()
  
  
## Get follower count
  a_follower_count = account_a["follower_count"]
  b_follower_count = account_b["follower_count"]
  
  is_correct = check_answer(guess, a_follower_count,  b_follower_count)
## Clear screen between rounds
  clear()
  print(logo)
## if statement
  if is_correct:
## Score keeping
## Feedback
    score += 1
    print(f"You're right! Current Score: {score}")
  else:
    game_should_continue = False
    print(f"Sorry, that was wrong Final Score {score}")



