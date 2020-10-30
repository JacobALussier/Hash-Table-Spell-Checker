''' Jacob Lussier 
Assignment 3 - Spell checking with a hash table
Due on December 10th by 11:59pm
'''
import sys
class HashTable:

    def __init__(self, size: int = 0):

        self.size: int = size
        self.table: list = []
        self.make_table()
        
    ''' Function to make a hash table the size of the class's size'''   
    def make_table(self) -> None:

        for i in range(self.size):
            self.table.append("") #Initialize each item in the table to null

        return
    ''' Function to implement a hash function in order to convert a string to a hash value, 
    my implementation uses a simplified version of the DJB2 algorithm'''
    def make_hash(self, word: str) -> int:
        hashValue = 5381 #Initialize hash value to a prime number
        for ch in word: # Loop through each character in the word

            hashValue = ((( hashValue << 5) + hashValue) + ord(ch)) % self.size # shift by 5 bits (prime number), add to the current hash, add the ascii value and finally mod by the table's size
        
        return hashValue 
        
        
       
    ''' Function to insert all the words in the dictionary into the hash table, 
    taking into account possible collisons by using probing'''
    def insert(self, word: str) -> None:
        word = word.lower() # convert the word to lowercase
        index = self.make_hash(word) # get the hash value of the word and store it to use as the table index
        if self.table[index] == "": # check if the spot in the table is blank
            self.table[index] = word # since its blank insert it in that spot
        else: # if the spot is not blank
            while self.table[index % self.size] != "": # Use the probing method to find a new spot for the word if necessary
                index += 1 # move along until an empty spot is found
            self.table[index] = word # insert in the new empty spot

        return
    ''' Function to see if a word is in the hash table (in the dictionary) and 
    return True if it is or False if its not''' 
    def lookup(self, word: str) -> bool:
        index = self.make_hash(word) # Get the hash value of the word in the book
        if self.table[index] == word: # if the word is in the same spot as its hash value return true
            return True
        elif self.table[index] == "": # if the hash value index is null then the word isn't in the table
            return False
        else: # If there is another word in the spot of the current word (because a collision occurred)
            while self.table[index] != "" and self.table[index] != word: # loop until a null spot shows up or the word is found
                index += 1
            if self.table[index] == "": # if the loop finishes on null the word is not in the list
                return False
            elif self.table[index] == word: # if the loop finishes on the word then it is found and return True
                return True
            
            
def main():
    
    dTable = HashTable(175003) # make a hash table about 75% larger than the size that would be needed for a perfect hash
    
    filename = sys.argv[2] # passing the dictionary as a command line argument
    openFile = open(filename,"r",encoding="utf8") # open the file keeping utf8 encoding in mind 
    for line in openFile: 
        if line == " ": # ignore spaces so they are not printed out later
            continue
        line = line.strip() # strip the line just to be safe
        dTable.insert(line) # Insert the word from the dictionary into the table using the insert function
    
    filename2 = sys.argv[1] # pass the book into the command line
    openFile2 = open(filename2,"r",encoding="utf8")
    alphaNum = "abcdefghijklmnopqrstuvwxyz1234567890" #This string represents the accepted alpha numeric characters that should be looked at
    for line in openFile2:
        words = line.split() # split each word in the line into elements in a list
        for word in words:
            word = word.lower() # convert the word to lowercase
            for char in word:
                if char not in alphaNum and char != "’" and char != "'": # if the character is not alphanumeric and not part of another edge case then remove it from the word
                    word = word.replace(char,"")
                elif char == "’": # if the different apostrophe is present replace it with the keyboard one
                    word = word.replace(char,"'") 
                elif char == "'": # if the normal apostrophe is present, don't change it, keep it as is
                    char = "'"
            
            if dTable.lookup(word) == False: # Check if the word is in the table and print if it is not
                print(word)
        
                
            
if __name__ == "__main__":
    main()

        
         


