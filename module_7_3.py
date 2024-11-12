class WordsFinder:
    def __init__(self,*file_list):
        self.file_names = [*file_list]

    def get_all_words(self):
        marks =  [',', '.', '=', '!', '?', ';', ':', ' - ']
        all_words = {}
        for file in self.file_names:
            with open(file) as in_file:
                temp_str = ''
                temp_list = []
                for line in in_file:
                    for char in line.lower():
                        if char not in marks:
                            temp_str += char
                    temp_list = temp_str.split()
                all_words[file] = temp_list
        return all_words

    def find(self, word):
        word_dic = {}
        for name, words in self.get_all_words().items():
            for index, el in enumerate(words):
                if word.lower() == el:
                    word_dic[name] = index+1
                    return word_dic

    def count(self, word):
        word_dic = {}
        count = 0
        for name, words in self.get_all_words().items():
            for el in words:
                if word.lower() == el:
                    count += 1
                    word_dic[name] = count
        return word_dic



finder2 = WordsFinder('test.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
