class Credentials:
    '''
    Class that generates new instances of the credentials.
    '''
    credential_list = []
    def save_credential(self):
        '''
        save_user method saves contact objects into credential_list
        '''
        Credentials.credential_list.append(self)

    def delete_credentials(self):
        '''
        delete_user method deletes a saved user from the credential_list
        '''
        Credentials.credential_list.remove(self)    

    def __init__(self, account_name, password):
      

        self.account_name = account_name
        self.password = password
    @classmethod
    def find_by_account_name(cls,account_name):   
       
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return credential
    @classmethod
    def credential_exist(cls,account_name):
    
        for credential in cls.credential_list:
            if credential.account_name == account_name:
                return True
                return False
