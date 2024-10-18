class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            try:
                with open(file_name, 'r', encoding='utf-8') as file:

                    text = file.read().lower()
                    for p in punctuation:
                        text = text.replace(p, '')

                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for file_name, words in all_words.items():
            try:

                position = words.index(word) + 1
                result[file_name] = position
            except ValueError:
                result[file_name] = None
        return result

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        result = {}

        for file_name, words in all_words.items():
            count = words.count(word)
            result[file_name] = count
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT'))  # 4 слова teXT в тексте всего
