

carac_array = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
    'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F',
    'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
    'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '-', '_'] 
    
def crypt_password(password,key):
    pass_crypt = "#1"
    for i in range(len(password)):
        ch = password[i]
        ch2 = key[i]
        #ch doit donner ça valeur ASCII (exemple r = 114) et etre diviser par 16
        num2 = int(ord(ch) / 16)
        num3 = int(ord(ch) % 16)
        index = int((num2 + ord(ch2)) % len(self.carac_array))
        num5 = int((num3 + ord(ch2)) % len(self.carac_array))
            
        pass_crypt = pass_crypt + self.carac_array[index] + self.carac_array[num5]
    return str(pass_crypt)


         
def decrypt_IP(packet):
    ip = ""
    for i in range(0,8,2):
        frist = int(ord(packet[i])  - 48) 
        segond = int(ord(packet[i+1]) - 48) 
            #print(packet[i],ord(packet[i]),int(ord(packet[i])  - 48) ) 
           # print(packet[i+1],ord(packet[i+1]),int(ord(packet[i+1])  - 48) )
        if i != 0:
            ip += (".")

        ip += str((((frist & 15) << 4) | (segond & 15)))
    return str(ip)



def crypt_IP(IP="127.0.0.1"):
    res = ""

    for value in IP.split("."):
        v1 = str(bin(int(value))).ljust(8,'0')
        print(str(v1))


def get_Cell_Id_From_Hash(cell_code):
    char1 = cell_code[0]
    char2 = cell_code[1]
    
    code1 = 0
    code2 = 0
    a = 0
    
    while (a < len(carac_array)):
    
        if (carac_array[a] == char1):
            code1 = (a * 64)

        if (carac_array[a] == char2):
            code2 = a

        a += 1
    print((code1 + code2))
    return (code1 + code2)



if __name__ == "__main__":
    print(aa.decrypt_IP("7?000001"))