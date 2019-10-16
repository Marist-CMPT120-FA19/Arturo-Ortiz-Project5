#This program determines the average word length of a sentence which is written by the user
#It also prints the number of words and number of characters
#By Arturo Ortiz, arturo.ortiz1@marist.edu
def main():
    sentence = input("Enter a sentence w/o punctutation : ")
    words = sentence.split(" ")
    
    avgWordLen = 0
    for i in words:
        avgWordLen = avgWordLen + len(i)
        
    avgWordLen = avgWordLen / len(words)
    characters = len(sentence)
    numWords = len(words)
    
    print("Number of characters:" , characters)
    print("Number of words:" , numWords)
    print("Average word length:" , avgWordLen)
    
main()
