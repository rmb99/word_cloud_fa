from hazm import Normalizer, WordTokenizer
import pathlib
import os


def source_reader(filename):
    return os.path.join(pathlib.Path(__file__).parent.resolve(), '', filename)



class Tokenizer:
    def __init__(self):
        self.wordtokenizer = WordTokenizer()
        self.normalizer = Normalizer(token_based=True)
        with open(source_reader('custom_tokens.txt'), 'r', encoding="utf-8") as txt_file:
            txt_reader = txt_file.read()
            frequency = 10
            tag = 'N'
            for word in txt_reader.split('\n'):
                word = word.strip().replace(' ', '‌')
                self.normalizer.words.update({word: (frequency, (tag))})

    def get_tokens(self, text):
        """ Turning a meaningful piece of data into tokens
        we use refined version of Hazm for this module and need to be installed from git repo (requirement)
        Arg:
            Text(string)
        Return:
            list of tokens
        """
        tokens = self.wordtokenizer.tokenize(text)
        normalized_tokens = self.normalizer.token_spacing(tokens)

        return normalized_tokens
