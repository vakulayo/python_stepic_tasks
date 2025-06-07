def reverse_words(string):
    words = string.split(' ')
    words.reverse()
    return ' '.join(words)


# string = "Wikis are enabled by wiki software, otherwise known as wiki engines."
print(reverse_words("Wikis are enabled by wiki software, otherwise known as wiki engines."))
#should be
#engines. wiki as known otherwise software, wiki by enabled are Wikis


