"""Module to generate  random users"""

from faker import Faker
from pathlib import	 Path
import logging




BASE_DIR = Path(__file__).resolve().parent /"user.log"
logging.basicConfig(filename=BASE_DIR, level=logging.DEBUG, format= '%(asctime)s - %(levelname)s - %(message)s') 

fake = Faker(locale="fr_FR")

def get_user():
    """Generate a single user

    Returns:
        str: user
    """
    logging.info("Generating user.")
    return f"{fake.unique.first_name()} {fake.unique.last_name()}"

def get_users(number: int = 1): 
    """Generate a list of a user        

    Args:
        number (int, optional): a number of users we desire. Defaults to 1.

    Returns:
        list[str]: users
    """
    logging.info(f"Genarating a list of {number} users")
    return [get_user() for _ in range (number)]



if __name__ == "__main__":
    print(get_user())
    print(get_users(5))