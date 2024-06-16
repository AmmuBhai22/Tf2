import torch
from torch.utils.data import Dataset

class WordMeaningDataset(Dataset):
    def __init__(self, words, meanings):
        self.words = words
        self.meanings = meanings
        
    def __len__(self):
        return len(self.words)
    
    def __getitem__(self, idx):
        word = self.words[idx]
        meaning = self.meanings[idx]
        
        # Convert word and meaning to tensors (you can customize this part)
        word_tensor = torch.tensor(word)
        meaning_tensor = torch.tensor(meaning)
        
        return word_tensor, meaning_tensor

# Sample data
words = ["Telephone", "Algebra"]
meanings = ["a system for transmitting voices over a distance using wire or radio", 
            "a branch of mathematics in which letters and symbols are used to represent quantities and quantities are manipulated according to the rules of operations"]

# Create dataset
word_meaning_dataset = WordMeaningDataset(words, meanings)

# Example usage:
for i in range(len(word_meaning_dataset)):
    word, meaning = word_meaning_dataset[i]
    #print(f"Word: {word}, Meaning: {meaning}")

while True:
    word = input("Enter prompt:\n")
    
    # Define meanings for the words
    word_meanings = {
        "Telephone": "a system for transmitting voices over a distance using wire or radio",
        "Algebra": "a branch of mathematics in which letters and symbols are used to represent quantities and quantities are manipulated according to the rules of operations"
        # Add more words and their meanings as needed
    }
    
    # Check if the word exists in the dictionary
    if word in word_meanings:
        print(f"Meaning of '{word}': {word_meanings[word]}")
    else:
        print(f"No meaning found for '{word}'")
  