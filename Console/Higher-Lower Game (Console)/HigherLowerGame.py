import random
from Game_Data import data
def format_data(account):
    """Format the account data into printable format."""
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(user_guess, a_followers, b_followers):
    """"""
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"
score = 0
continue_game = True
account_b = random.choice(data)

while continue_game:
    account_a = account_b
    account_b = random.choice(data)
    if (account_a == account_b):
        account_b = random.choice(data)
    print(f"Compare A: {format_data(account_a)}")
    print("VS")
    print(f"Against B: {format_data(account_b)}")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower().strip()

    print("\n" * 20)

    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

    if is_correct:
        score += 1
        print("You're right! Current score {score}")
    else:
        print("Sorry, that's wrong! Final score: {score}")
        continue_game = False