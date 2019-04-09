#!/usr/bin/env python3.6

from credentials import Credentials
import pyperclip
from user import User
import string
import random


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

def generate_password(generate_password):
    '''
    Function to generate a password randomly
    '''

    gen_pass = Credential.generate_password()
    return gen_pass    

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
            print("Hello Welcome . What is your account name?")
            account_name = input()

            print("Hello {}. what would you like to do?".format(account_name))
            print('\n')
            
           
            print("Welcome to PassWord Locker app.")
            print('\n')
                
            short_code = input("Use these short codes to select an option:  Create New account: 'cc'  Login to your account:'log' dc - display user,  To exit password locker: 'ex' 'g' generate password")

            print('\n')
            if short_code == 'cc':
                
                while True:
                    print("Create an account")
                    created_account_name = input(">Enter name:  ")
            
                    created_account_password = input(">Enter a password:  ")
                
                    confirm_password = input("Confirm Your Password")

                    if confirm_password != created_account_password:
                        print("Sorry this passwords does'nt exist!")
                        continue
                    else:
                        print("Congratulations {}! You have created your new account.".format(created_account_name))
                        break
                    
                    if short_code == 'g':
                        print('\n')
                        print("generate_password")
                        default_generate_password = input()
                        print('\n')                   


            elif  short_code == 'log':
                print('/n')
                print("account_name")
                default_account_name =input()
                print('/n')
                print("password")
                default_password = input()
                print('/n')

            elif  short_code == 'ex':
                print('/n')
                print("account_name")
                default_account_name =input()
                print('/n')
                print("password")
                default_password = input()
                print('/n')
                #sys.exit()    
            elif short_code == 'dc':
                    if display_credentials():
                        print("displaying account name")
                        print('\n')
                    for credentials in display_credentials():
                        print(f"{credentials.account_name} {credentials.password}")
                        print('\n')

            else:
                        print('\n')
                        print("you don't seem to have any account")
                        print('\n')     


if __name__ == '__main__':
     main()                    