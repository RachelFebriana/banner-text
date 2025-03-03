import pyfiglet
import random
print (" ")
print ("-------------------------------------------------------")
print ("• Banner Text Random Tools")
print ("• By : rachel febriana ")
print ("-------------------------------------------------------")
print (" ")
def generate_banner(text):
    fonts = pyfiglet.FigletFont.getFonts()
    
    random_font = random.choice(fonts)
    
    banner = pyfiglet.figlet_format(text, font=random_font)
    
    return banner, random_font
    
def main():
    total_banners = 0   
    
    while True:
    
        user_input = input("Masukkan Text : ")
        
        if user_input.lower() == 'exit':     
        
            break
            
        banner_output, font_used = generate_banner(user_input)
        
        print("\n" + banner_output)
        
        print(f"Font yang digunakan: {font_used}\n")
        
        total_banners += 1
        
    print(f"Total banner : {total_banners}")
    
if __name__ == "__main__":

    main()
