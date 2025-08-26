from datetime import datetime


class MonitoredDict(dict):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.log = list()
        self.log_timestamp('MonitoredDict created')

    def __getitem__(self, key):
        val = super().__getitem__(key)
        self.log_timestamp('value for key [{}] retrieved'.format(key))
        return val

    def __setitem__(self, key, val):
        super().__setitem__(key, val)
        self.log_timestamp('value for key [{}] set'.format(key))

    def log_timestamp(self, message):
        timestampStr = datetime.now().strftime("%Y-%m-%d (%H:%M:%S.%f)")
        self.log.append('{} {}'.format(timestampStr, message))

# In this example, a class is based on Python's built-in dictionary. It is equipped with logging mechanisms for
# detais of writng nd reading operaions performed on the elements of a dictionary.

# This essentially arms a Python dictionary with the ability to log details of:
    # class instantiation
    # read access
    # new element creation or update

# The variable which will maintain the actual list is created using the class:
kk = MonitoredDict()
kk[10] = 15
kk[20] = 5

# The 'kk' variable has the list:
print('COMMENT: the "kk" variable has the list:')
print(kk)
print()

# ... and kk.log has the audit trail:
print('... and "kk.log" has the audit trail:')
print('\n'.join(kk.log))
print()

# Simply reading/accessing any element of the list triggers __getitem__ without the need for an add'l function:
print("Simply reading/accessing any element of the list triggers __getitem__ without the need for an add'l function:")
print('Element kk[10]:', kk[10])
print()

# See the new, fourth entry:
print('See the new, fourth entry:')
print('\n'.join(kk.log))
print()

print('Whole dictionary:', kk)
print()
print('Our log book:\n')
print('\n'.join(kk.log))
