class User:
    '''
    Class that generates new instances of the user.
    '''
    user_list = []
    def save_user(self):
        '''
        save_user method saves contact objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)    

    def __init__(self, first_name, last_name, user_name, password):
        '''
        init__helps us to define our users' properties.
        Args:
            first_name: New contact first name.
            last_name: New contact last name.
            user_name: New user's login username.
            password: New user's login password   
        '''

        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password