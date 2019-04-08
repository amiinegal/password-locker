#!/usr/bin/env python3.6
from credentials import Credentials
import pyperclip
from user import User

def create_credentials(account_name,password):
    '''
    Function to create a new credential
    '''
    new_credentials = Credentials(account,password)
    return new_credentials
def save_credentials(credentials):
    '''
    Function to save a credentials
    '''
    credentials.save_credentials()

def del_credentials(credentials):
    '''
    Function to delete a credential
    '''
    credentials.delete_credentials()

def find_credentials(account_name):        
    '''
    Function that finds a user by account name and returns the name
    '''
    return Credentials.find_by_account_name(account_name)
def check_existing_credentials(account_name):
    '''
    Function that check if a user exists with that account name and returns a Boolean
    '''
    return Credentials.credentials_exist(account_name) 
def display_credentials():
    '''
    Function that check if a user exist with that account name and return a boolean
    '''
    return Credentials.credentials_exist(account_name) 

def main():
            print("Hello Welcome to your credentials  list. What is your account name?")
            account_name = input()

            print(f"Hello {account_name}. what would you like to do?")
            print('\n')
            
            while True:
                print("Welcome to PassWord Locker app.")
                print('\n')
                print("Use these short codes to select an option: \n Create New account: 'cc' \n Login to your account:'log' \n To exit password locker: 'ex'")
                break
            short_code = input().lower()
            print('\n')
            if short_code == 'cc':
                print("Create an account")
            created_account_name = input()
            print("Select a Password")
            created_account_password = input()
            print("Confirm Your Password")
            confirm_password = input()

            while confirm_password != created_account_password:
                print("Sorry this passwords does'nt exist!")
                print("Enter a password")
                created_user_password = input()
                print("Confirm Your Password")
                confirm_password = input()
            else:
                print(f"Congratulations {created_account_name}! You have created your new account.")
                print('\n')
        

if __name__ == '__main__':
     main()                    