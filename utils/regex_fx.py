import re

def remove_single_char(text):
    single_char_pattern = r'\s+[a-zA-Z]\s+'
    without_sc = re.sub(pattern=single_char_pattern, repl=" ", string=text)
    return without_sc

def remove_numbers(text):
    number_pattern = r'\b(?<![0-9-])(\d+)(?![0-9-])'
    without_number = re.sub(pattern=number_pattern, repl=" ", string=text)
    return without_number


def remove_urls(text):
    url_pattern = r'https?://\S+|www\.\S+'
    without_urls = re.sub(pattern=url_pattern, repl=" ", string=text)
    return without_urls


def remove_emojis(text):
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F1E0-\U0001F1FF"  # flags (iOS)
                               u"\U00002500-\U00002BEF"  # chinese char
                               u"\U00002702-\U000027B0"
                               u"\U00002702-\U000027B0"
                               u"\U000024C2-\U0001F251"
                               u"\U0001f926-\U0001f937"
                               u"\U00010000-\U0010ffff"
                               u"\u2640-\u2642"
                               u"\u2600-\u2B55"
                               u"\u200d"
                               u"\u23cf"
                               u"\u23e9"
                               u"\u231a"
                               u"\ufe0f"  # dingbats
                               u"\u3030"
                               "]+", flags=re.UNICODE)
    without_emoji = emoji_pattern.sub(r'',text)
    return without_emoji

def remove_rt(text):
    rt_pattern = 'rt @[\w_]+: '
    without_pattern = re.sub(pattern = rt_pattern, repl=" ", string = text)
    return without_pattern 

def remove_extra_spaces(text):
    space_pattern = r'\s+'
    without_space = re.sub(pattern=space_pattern, repl=" ", string=text)
    return without_space

# Extra functions required

def remove_nonalpha(text):
    # non_alpha_pattern = re.compile('[\W_]+', re.UNICODE)
    # without_nonalpha = non_alpha_pattern.sub(r'',text)
    res = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    return res

def remove_mention(text):
    res = re.sub(pattern='@[^\s]+',repl='',string=text)
    return res

def remove_non_ascii(text):
    return text.encode("ascii", errors="ignore").decode()

def remove_special_words(text):
    stopwords = ['amp', 'nt', 'trump', 'realdonaldtrump', 'say', 'news', 'obama', 's', 'new', 'year', 'meetthepress']
    querywords = text.split()
    new_words = [word for word in querywords if word not in stopwords]
    result = ' '.join(new_words)
    return result

def remove_nt(text):
    res = re.sub(r'\ nt ', '', text)
    return res
