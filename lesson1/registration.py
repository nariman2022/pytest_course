
class Registration:
    def __init__(self):
        self.users = {}

    def register(self, name, email, phone):
        if email in self.users:
            return f'Error: User exist already.'
        self.users[email] = {'name': name, 'email': email, 'phone': phone}
        return f'User was successfully registered'

    def delete_user_by_email(self, email):
        if email not in self.users:
            return f'User does not exist'
        del self.users[email]
        return f'User with email {email} was deleted'

    def delete_all_users(self):
        self.users = {}
        return f'All users were deleted'

    def view_all_users(self):
        return self.users

system = Registration()

print(system.register("Misha", "micha@email.com", "+1234567890"))
print(system.view_all_users())
print(system.delete_user_by_email('micha@email.com'))
print(system.delete_all_users())

