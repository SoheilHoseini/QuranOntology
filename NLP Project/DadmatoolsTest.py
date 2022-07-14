from dadmatools.models.normalizer import Normalizer

normalizer = Normalizer(
    full_cleaning=False,
    unify_chars=True,
    refine_punc_spacing=True,
    remove_extra_space=True,
    remove_puncs=False,
    remove_html=False,
    remove_stop_word=False,
    replace_email_with="<EMAIL>",
    replace_number_with=None,
    replace_url_with="",
    replace_mobile_number_with=None,
    replace_emoji_with=None,
    replace_home_number_with=None
)

text = """
<p>
دادماتولز اولین نسخش سال ۱۴۰۰ منتشر شده. 
امیدواریم که این تولز بتونه کار با متن رو براتون شیرین‌تر و راحت‌تر کنه
لطفا با ایمیل dadmatools@dadmatech.ir با ما در ارتباط باشید
آدرس گیت‌هاب هم که خب معرف حضور مبارک هست:
 https://github.com/Dadmatech/DadmaTools
</p>
"""
#print('input text : ', text)
#print('output text when replace emails and remove urls : ', normalizer.normalize(text))

#full cleaning
normalizer = Normalizer(full_cleaning=True)
#print('output text when using full_cleaning parameter', normalizer.normalize(text))

import dadmatools.pipeline.language as language

# here lemmatizer and pos tagger will be loaded
# as tokenizer is the default tool, it will be loaded even without calling
# pips = 'lem,pos' 
# pips = 'dep' 
pips = 'tok,lem,pos,dep,cons' 
nlp = language.Pipeline(pips)

# you can see the pipeline with this code
#print(nlp.analyze_pipes(pretty=True))

test_project = open("/content/testquran.txt", "r", encoding="utf8")
final_project = open("/content/Dodmatools Result.txt", "w", encoding="utf8")

def ModifyLines(line):
    listedLine = list(line)
    for i in range(len(listedLine)):
        if(listedLine[i] == ")" or listedLine[i] == "("):
            listedLine[i] = " "
        if(i == len(listedLine) - 1):
            listedLine[i] = ""


    removedParantheses = "".join(listedLine)

    return removedParantheses

cnt = 0
for line in test_project:
    print(cnt, line)
    cnt += 1
    doc = nlp(ModifyLines(str(line)))
    output = language.to_json(pips, doc)
    parsedLine = str(output) +"\n\n"
    final_project.write(parsedLine)
    print(output)

# doc is an SpaCy object

final_project.close()
test_project.close()