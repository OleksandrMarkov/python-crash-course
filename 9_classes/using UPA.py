#from UPA import Privileges, User, Admin

from AdminPrivileges import Admin, Privileges

admin = Admin('A.', 'B.', 50, 'status...')
admin.privileges.show_privileges()