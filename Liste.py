katzen= []
while True:
	print("Gebe den Namen der " +str(len(katzen)+1) + " Katze ein oder drücke einfach Enter um die Liste anzuzeigen: ")
	name=input()
	if name == "":
		break
	katzen= katzen+[name]
print("Die Katzennamen lauten: ")
for name in katzen:
  print(" " + name)

print(name[])
