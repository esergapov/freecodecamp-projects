from googletrans import Translator
translator=Translator()
s=input("Enter text :  ")
des=input("Which language translate:  ")
res=translator.translate(s, dest=des)
print(res.text)