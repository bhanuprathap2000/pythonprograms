alphabets=list("abcdefghijklmnopqrstuvwxyz")
def ceaser(direction,plain_text,shift_amount):
    end_text=""
    for char in plain_text:
        if char in alphabets:
            if direction=="encode":
                position=alphabets.index(char)
                new_position=(position+shift_amount)%25
            elif direction=="decode":
                position=alphabets.index(char)
                new_position=(position-shift_amount)%25
    
            end_text+=alphabets[new_position]
        else:
            end_text+=char
            
        
        
        
    print(end_text)

repeat=True
while repeat:
    ceaser_direction=input("Type encode, for encoding and decode, for decoding\n")
    text=input("Enter the text\n");
    shift=int(input("Enter the shift number\n"))
    ceaser(direction=ceaser_direction,plain_text=text,shift_amount=shift)
    again=input("Yes for reapeating no for exit\n")
    if (again=="no"):
        repeat=False
