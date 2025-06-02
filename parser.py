import pandas as pd 

df = pd.read_csv('./backend/metaphysics.csv')
print(df)



#####################
## commit 1 - successfully parses .txt file - 01-06-25
## need to remove \n and one numbers

# import pandas as pd

# with open('./backend/metaphysics.txt', 'r', encoding='utf-8') as file:
#     text = file.read()
    
# sentences = text.split('. ')
# sentences = [sentence.strip() for sentence in sentences]

# df = pd.DataFrame(sentences, columns=['sentence'])  # Remove empty sentences
# df = df[df['sentence'] != '']  # Remove empty sentences
# df.to_csv('metaphysics.csv', index=False)  # Save to CSV
# print(df)



######################
# import pandas as pd 

# df = pd.read_csv('metaphysics.txt', headeer=None, sep='.')
# print(df)