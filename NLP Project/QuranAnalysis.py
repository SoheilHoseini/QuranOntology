tmp_text = "به گزارش ایسنا سمینار شیمی آلی از امروز ۱۱ شهریور ۱۳۹۶ در دانشگاه علم و صنعت ایران آغاز به کار کرد. این سمینار تا ۱۳ شهریور ادامه می یابد."
from parsivar import Normalizer
my_normalizer = Normalizer()
#print(my_normalizer.normalize(tmp_text))


my_normalizer = Normalizer(statistical_space_correction=True)
#print(my_normalizer.normalize(tmp_text))


my_normalizer = Normalizer(date_normalizing_needed=True)
#print(my_normalizer.normalize(tmp_text))


my_normalizer = Normalizer(pinglish_conversion_needed=True)
#print(my_normalizer.normalize("farda asman abri ast."))


from parsivar import Tokenizer
my_normalizer = Normalizer()
my_tokenizer = Tokenizer()
sents = my_tokenizer.tokenize_sentences(my_normalizer.normalize(tmp_text))
#print(sents)

 
words = my_tokenizer.tokenize_words(my_normalizer.normalize(tmp_text))
#print(words)

 
from parsivar import FindStems
my_stemmer = FindStems()
#print(my_stemmer.convert_to_stem("بیابیم"))


# Test Project for POSTagger
def ConvertToString(line):
    tmpLine = []
    
    # Just consider nouns and verbs
    for item in line:
        if item[1] == "N" or item[1][0] == "V":
            tmpLine.append(item)
            
            
    ans = ""
    for x in tmpLine:
        ans += x[0] + " -> " + x[1] + " , "    
    
    return ans[:len(ans) - 2] + "\n\n\n\n"

from parsivar import POSTagger
my_tagger = POSTagger(tagging_model="stanford")  # tagging_model = "wapiti" or "stanford". "wapiti" is faster than "stanford"
text_tags = my_tagger.parse(my_tokenizer.tokenize_words("دعوت از منکران معاد به مطالعه در آب آشامیدنى و کیفیت قرار گرفتن آن در دسترس انسان‌ها"))
#print(text_tags)

test_project = open("testquran.txt", "r", encoding="utf8")
final_project = open("Final Project.txt", "w", encoding="utf8")

cnt = 1
for line in test_project:
    tmp_tags = my_tagger.parse(my_tokenizer.tokenize_words(line))
    #listToStr = ' '.join([str(elem) for elem in tmp_tags])
    #print(ConvertToString(tmp_tags))
    final_project.write(ConvertToString(tmp_tags))
    print(cnt)
    cnt += 1

final_project.close()
test_project.close()






 
 
from parsivar import FindChunks
my_chunker = FindChunks()
chunks = my_chunker.chunk_sentence(text_tags)
#print(my_chunker.convert_nestedtree2rawstring(chunks))


from parsivar import DependencyParser
myparser = DependencyParser()
sents = "به گزارش ایسنا سمینار شیمی آلی از امروز ۱۱ شهریور ۱۳۹۶ در دانشگاه علم و صنعت ایران آغاز به کار کرد. این سمینار تا ۱۳ شهریور ادامه می یابد"
sent_list = my_tokenizer.tokenize_sentences(sents)
parsed_sents = myparser.parse_sents(sent_list)
for depgraph in parsed_sents:
	#print(depgraph.tree())
    pass

from parsivar import SpellCheck
myspell_checker = SpellCheck()
res = myspell_checker.spell_corrector("نمازگذاران وارد مسلی شدند.")
#print(res)
