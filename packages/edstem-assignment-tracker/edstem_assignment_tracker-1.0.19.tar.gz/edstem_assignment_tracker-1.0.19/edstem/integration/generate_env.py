import os
from dotenv import dotenv_values

def generate_env():
    # Get the current directory
    current_dir = os.getcwd()
    
    # Get the parent directory
    parent_dir = os.path.dirname(current_dir)
    
    # Path to the .env file
    env_path = os.path.join(parent_dir, '.env')

    
    # Write environment variables to the .env file
    with open(env_path, 'w') as env_file:
        env_file.write("ED_API_TOKEN=")  # Example environment variable
        
    print(f".env file created in the parent directory: {env_path}")

if __name__ == "__main__":
    generate_env()


def main():
    link = "https://edstem.org/us/settings/api-tokens"
    # provide user instructions
    print("To get the token, follow these steps:")
    print(f"1. Go to {link}\n")
    print("2. Sign in if needed\n")
    print("3. Click on 'Create Token'\n")
    print("4. Copy the token and paste it below\n")
    # Get the token from user input
    token = input("Enter your token: ")

    # Create the .env file with the token
    create_env_file(token)

if __name__ == "__main__":
    main()