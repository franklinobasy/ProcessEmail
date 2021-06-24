def open_file(filename):
    '''This function opens a file and returns it as a string
       If file is not found, it returns None
     '''
    try:
        with open(filename, 'r') as file_object:
            txt = file_object.read()
            file_object.close()
        return txt
    except FileNotFoundError:
        print("file not found!")
        return None

def split_text(text, basis):
    '''
    This function using python split function to split text by a defined basis
    '''
    if not (isinstance(text, str) and isinstance(basis, str)):
        raise TypeError("Arguments must be of str type")
    else:
        return text.split(basis)

def getSender(text):
    f_text = ''  # formatted text
    text = text.strip()
    for char in text:
        if char == '@':
            break
        f_text += char
    return f_text

def generateDict(lst):
    dummy_list = lst.copy()
    lst = set(lst)  # converts the list to set, inorder to get a set of unique items
    lst = list(lst)
    sender_dict = {}
    for sender in lst:
        val = 0
        for _ in dummy_list:
            if sender == _ :
                val += 1
        sender_dict[sender] = val
    
    return sender_dict



def main():
    '''
    Main function
    '''
    filepath = r"mbox-short.txt"
    text = open_file(filepath)
    text = split_text(text, 'From ')
    sender_list = [getSender(sender) for sender in text[1:]]
    data = generateDict(sender_list)
    print(data)
    
    
    

main()