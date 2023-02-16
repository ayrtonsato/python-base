def repete_vogal(word):
	"""Retonar a palavra com as vogais repetidas."""
	final_word = ""
	for letter in word:
		# forma de colocar um breakpoint no pdb
		# __import__("pdb").set_trace()
		if letter.lower() in "aeiouãõâôéáíó":
			final_word = letter * 2
		else:	
			final_word = letter
	# forma de colocar um breakpoint somente acima do python 3.7
	# breakpoint()
	return final_word

print(repete_vogal("banana"))

# debugger
# python -m pdb temdebug.py
# executa até linha x
# python -m pdb -c "until 12" temdebug.py
# continua o debugging em caso de erro (post mortem debugging)
# python -m pdb -c continue debugging/tembug.py

# ipdb é uma opção de terminal colorida
# pudb é uma opção interativa colorida