from bs4 import BeautifulSoup
import subprocess
import re

#FILENAME = '../../corpus-joyce-portrait-TEI/portrait.xml'
FILENAME = 'portrait_short.xml'
STASHFILE = "problems_said_asked.txt"

with open(FILENAME,'r') as f:
    soup = BeautifulSoup(f, 'lxml')

said_tags = [said_tag for said_tag in soup.findAll("said") if 'said' in said_tag.text]
asked_tags = [said_tag for said_tag in soup.findAll("said") if 'said' in said_tag.text]

subprocess.call(["rm","-rf",STASHFILE])

with open(STASHFILE,"a") as f:

    #for said in said_tags:
    #    original = str(said)
    #    f.write("-"*40)
    #    f.write('\n')
    #    f.write(original)
    #    f.write('\n')

    #for asked in asked_tags:
    #    original = str(asked)
    #    f.write("-"*40)
    #    f.write('\n')
    #    f.write(original)
    #    f.write('\n')



    for said in said_tags:

        original_text = str(said)


        #####################################

        match1 = re.match(r'.* the (\w+) said, .*', original_text)

        if(match1):

            print("-"*40)
            print("Matched pattern \"the XXX said\"")
            print("Original:\t%s"%(original_text))

            orig_txt = re.sub('\n','@@@',original_text)

            new_text_closeopen   = re.sub(r'(.*)( the \w+ said)(.*)</said>', r'\1</said>\2<said who="???">\3</said>', orig_txt)
            new_text_closenoopen = re.sub(r'(.*)( the \w+ said)(.*)</said>', r'\1</said>\2\3', orig_txt)

            new_txt_co = re.sub('@@@','\n',new_text_closeopen)
            new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

            print("Fix 1:\t\t%s"%(new_txt_co ))
            print("Fix 2:\t\t%s"%(new_txt_cno))
    

        ##############################

        match2 = re.match(r'.* (\w+) said, .*', original_text)
    
        if(not match1 and match2):
    
            # if we find a "he said" or "she said", we want to mark it differently
            if(match2.group(1)=='he' or match2.group(1)=='she'):
                print("-"*40)
                print("Matched pattern \"he said, \" or \"she said, \"")
                print("Original:\t%s"%(original_text))

                orig_txt = re.sub('\n','@@@',original_text)

                new_text_closeopen   = re.sub(r'(.*)( \w+ said, )(.*)</said>', r'\1</said>\2<said who="???">\3</said>', orig_txt)
                new_text_closenoopen = re.sub(r'(.*)( \w+ said, )(.*)</said>', r'\1</said>\2\3', orig_txt)

                new_txt_co = re.sub('@@@','\n',new_text_closeopen)
                new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

                print("Fix 1:\t\t%s"%(new_txt_co))
                print("Fix 2:\t\t%s"%(new_txt_cno))
    
            else:
                likely_speaker = match2.group(1)
                print("-"*40)
                print("Matched pattern \"XXX said, \"")
                print("Likely Speaker: %s"%(likely_speaker))
                print("Original:\t%s"%(original_text))

                orig_txt = re.sub('\n','@@@',original_text)
    
                new_text_closeopen   = re.sub(r'<said who="\?\?\?">(.*)( \w+ said, )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2<said who="'+likely_speaker+r'">\3</said>', orig_txt)
                new_text_closenoopen = re.sub(r'<said who="\?\?\?">(.*)( \w+ said, )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2\3', orig_txt)

                new_txt_co = re.sub('@@@','\n',new_text_closeopen)
                new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

                print("Fix 1:\t\t%s"%(new_txt_co ))
                print("Fix 2:\t\t%s"%(new_txt_cno))






        #######################################

        match3a = re.match(r'.* the (\w+) said .*', original_text)

        if(not match1 and not match2 and match3a):

            likely_speaker = match3a.group(1)
            print("-"*40)
            print("Matched pattern \"the XXX said \"")
            print("Likely Speaker: %s"%(likely_speaker))
            print("Original:\t%s"%(original_text))
    
            orig_txt = re.sub('\n','@@@',original_text)

            new_text_closeopen   = re.sub(r'<said who="\?\?\?">(.*)( the \w+ said )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2<said who="'+likely_speaker+r'">\3</said>', orig_txt)
            new_text_closenoopen = re.sub(r'<said who="\?\?\?">(.*)( the \w+ said )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2\3', orig_txt)

            new_txt_co = re.sub('@@@','\n',new_text_closeopen)
            new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

            print("Fix 1:\t\t%s"%(new_txt_co ))
            print("Fix 2:\t\t%s"%(new_txt_cno))




        #######################################

        match3 = re.match(r'.* (\w+) said .*', original_text)

        if(not match1 and not match2 and match3):

            # if we find a "he said" or "she said", we want to mark it differently
            if(match3.group(1)=='he' or match3.group(1)=='she'):
                print("-"*40)
                print("Matched pattern \"he said \" or \"she said \"")
                print("Original:\t%s"%(original_text))

                orig_txt = re.sub('\n','@@@',original_text)

                new_text_closeopen   = re.sub(r'(.*)( \w+ said )(.*)</said>', r'\1</said>\2<said who="???">\3</said>', orig_txt)
                new_text_closenoopen = re.sub(r'(.*)( \w+ said )(.*)</said>', r'\1</said>\2\3', orig_txt)

                new_txt_co = re.sub('@@@','\n',new_text_closeopen)
                new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

                print("Fix 1:\t\t%s"%(new_txt_co ))
                print("Fix 2:\t\t%s"%(new_txt_cno))
    
            else:
                likely_speaker = match3.group(1)
                print("-"*40)
                print("Matched pattern \"XXX said \"")
                print("Likely Speaker: %s"%(likely_speaker))
                print("Original:\t%s"%(original_text))
    
                orig_txt = re.sub('\n','@@@',original_text)

                new_text_closeopen   = re.sub(r'<said who="\?\?\?">(.*)( \w+ said )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2<said who="'+likely_speaker+r'">\3</said>', orig_txt)
                new_text_closenoopen = re.sub(r'<said who="\?\?\?">(.*)( \w+ said )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2\3', orig_txt)

                new_txt_co = re.sub('@@@','\n',new_text_closeopen)
                new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

                print("Fix 1:\t\t%s"%(new_txt_co ))
                print("Fix 2:\t\t%s"%(new_txt_cno))



        #######################################

        match4a = re.match(r'.* the (\w+) said\. .*', original_text)

        if(not match1 and not match2 and not match3a and not match3 and match4a):

            likely_speaker = match4a.group(1)
            print("-"*40)
            print("Matched pattern \"the XXX said.\"")
            print("Likely Speaker: %s"%(likely_speaker))
            print("Original:\t%s"%(original_text))
    
            orig_txt = re.sub('\n','@@@',original_text)

            new_text_closeopen   = re.sub(r'<said who="\?\?\?">(.*)( the \w+ said\. )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2<said who="'+likely_speaker+r'">\3</said>', orig_txt)
            new_text_closenoopen = re.sub(r'<said who="\?\?\?">(.*)( the \w+ said\. )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2\3', orig_txt)

            new_txt_co = re.sub('@@@','\n',new_text_closeopen)
            new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

            print("Fix 1:\t\t%s"%(new_txt_co ))
            print("Fix 2:\t\t%s"%(new_txt_cno))




        #######################################

        match4 = re.match(r'.* (\w+) said\. .*', original_text)

        if(not match1 and not match2 and not match3a and not match3 
                and not match4a and match4):

            if(match4.group(1)=='he' or match4.group(1)=='she'):
                print("-"*40)
                print("Matched pattern \"he said.\" or \"she said.\"")
                print("Original:\t%s"%(original_text))

                orig_txt = re.sub('\n','@@@',original_text)

                new_text_closeopen   = re.sub(r'(.*)( \w+ said\. )(.*)</said>', r'\1</said>\2<said who="???">\3</said>', orig_txt)
                new_text_closenoopen = re.sub(r'(.*)( \w+ said\. )(.*)</said>', r'\1</said>\2\3', orig_txt)

                new_txt_co = re.sub('@@@','\n',new_text_closeopen)
                new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

                print("Fix 1:\t\t%s"%(new_txt_co ))
                print("Fix 2:\t\t%s"%(new_txt_cno))
    
            else:
                likely_speaker = match4.group(1)
                print("-"*40)
                print("Matched pattern \"XXX said.\"")
                print("Likely Speaker: %s"%(likely_speaker))
                print("Original:\t%s"%(original_text))
    
                orig_txt = re.sub('\n','@@@',original_text)

                new_text_closeopen   = re.sub(r'<said who="\?\?\?">(.*)( \w+ said\. )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2<said who="'+likely_speaker+r'">\3</said>', orig_txt)
                new_text_closenoopen = re.sub(r'<said who="\?\?\?">(.*)( \w+ said\. )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2\3', orig_txt)

                new_txt_co = re.sub('@@@','\n',new_text_closeopen)
                new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

                print("Fix 1:\t\t%s"%(new_txt_co ))
                print("Fix 2:\t\t%s"%(new_txt_cno))

