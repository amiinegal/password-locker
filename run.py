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
