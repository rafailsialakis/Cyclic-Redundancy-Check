def xor(a,b):
    if(a == b):
        return '0'; # 0 xor 0 == 0 , 1 xor 1 == 0
    else:
        return '1'; # 1 xor 0 == 1 , 0 xor 1 == 1

def generate_message():
    bin_message = int(input("Please insert the binary message: " ))
    return bin_message;

def generate_full_message(message,polyonym):
    parity_size = len(str(polyonym))
    factor = 10 ** (parity_size-1)
    new_message = message * factor
    print("The message that the transmitter sends is:",new_message)
    return new_message;

def generate_polyonym():
    bin_polyonym = int(input("Please insert the polyonym-generator: "))
    return bin_polyonym;

def crc(message,polyonym): 
    part_list = []
    xor_list = []
    parity_size = len(str(polyonym))
    Message_List = list(str(message))
    Polyonym_List = list(str(polyonym))
    for i in Message_List:    
        part_list.append(i)
        first_ace = False
        if(len(part_list) == parity_size):
            for j in range(parity_size):
                if(xor(part_list[j],Polyonym_List[j]) == '1'):
                    first_ace = True
                if(first_ace):
                    xor_list.append(xor(part_list[j],Polyonym_List[j]))
            part_list.clear()
            for j in xor_list:
                part_list.append(j)
            xor_list.clear()
    final_list = ['0'] * (parity_size - len(part_list)) + part_list
    print("The output of the crc is:", ''.join(map(str,final_list))) 
    size = len(part_list)
    for i in range(size):
        Message_List.pop()
    for i in part_list:
        Message_List.append(i)
    new_message = int(''.join(Message_List))
    return new_message

def main():    
    msg = generate_message()
    poly = generate_polyonym()
    full_msg = generate_full_message(msg,poly)
    new_msg = crc(full_msg,poly)
    print("The message the receiver wants to check is",new_msg)
    crc(new_msg,poly)
    
if __name__ == "__main__":
    main()
