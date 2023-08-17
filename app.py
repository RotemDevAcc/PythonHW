from functions import *
import time



Dict = {}

if __name__ == "__main__":
    print("\033[H\033[J") # Clears The Screen For Some Reason
    print("\033[32mThis text is in green.\033[0m This text is not.") # Green Text / Normal Text

    first,last = GetNames() # Input For Names
    Dict[len(Dict)] = first
    Dict[len(Dict)] = last
    SaveToTargetFile(Dict,"saba.json") # SaveToTargetFile > functions.py
    time.sleep(1) # Give Time For The File To Get Set-up
    vars = OpenTargetFile("saba.json") # OpenTargetFile > functions.py
    print("File Output")
    print(vars)
    
