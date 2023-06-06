import email
from email.policy import default


class MboxReader:   #the class for reading through each email in a mailbox
    def __init__(self, filename):   # initialise object state, variable filename
        self.handle = open(filename, 'rb')   # open file in binary mode
        assert self.handle.readline().startswith(b'From ')   # DEBUG: 'assert' to test if condition is true
                                                            # email must start with 'from'
    def __enter__(self):    # enter makes object, returns it
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback): # closes file when conditions are met
        self.handle.close()                                 # 'exc' is exception

    def __iter__(self):  # Iterating function, through __next__() function once finished
        return iter(self.__next__())

    def __next__(self):
        lines = []
        while True:
            line = self.handle.readline()   # read in a line from file
            if line == b'' or line.startswith(b'From '):    # if it starts with nothing or 'From'
                yield email.message_from_bytes(b''.join(lines), policy=default) # suspend execution of function
                if line == b'':                                             # and send value back when line is
                    break                                                   #  empty or starts with From,
                lines = []                                                  #  meaning start of a new email
                continue
            lines.append(line)  # add processed line to 'Lines' array
            # repeat function through each email

# call class method in __main__

#Print as string loop
#with datasets.MboxReader(MyMail) as mbox:
   # for message in mbox:
    #    print(message.as_string())