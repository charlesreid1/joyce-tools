from bs4 import BeautifulSoup
import subprocess
import re

## Test
#FILENAME = 'portrait_short.xml'

# The real deal
FILENAME = '../../corpus-joyce-portrait-TEI/portrait.xml'

# Where to stash the suggested fixes
STASHFILE = "PROBLEMS_SAID.txt"



# Load the soup
with open(FILENAME,'r') as f:
    soup = BeautifulSoup(f, 'lxml')

# Find the problematic tags
said_tags = [said_tag for said_tag in soup.findAll("said") if 'said' in said_tag.text]
#asked_tags = [said_tag for said_tag in soup.findAll("said") if 'asked' in said_tag.text]

## Clear out the stash file before we write to it
subprocess.call(["rm","-rf",STASHFILE])



#######################################
# Weak Sauce Version:
# 
# Just print <said> tags 
# that have the word "said"
# in their text. 
# 
# This generates a lot of output.
#######################################

#with open(STASHFILE,"a") as f:
#
#    for said in said_tags:
#        original = str(said)
#        f.write("-"*40)
#        f.write('\n')
#        f.write(original)
#        f.write('\n')
#
#    for asked in asked_tags:
#        original = str(asked)
#        f.write("-"*40)
#        f.write('\n')
#        f.write(original)
#        f.write('\n')



#######################################
# More Helpful Version:
# 
# Print <said> tags that have the word "said"
# in their text, and guess from the pattern
# what the fixed-up <said> tag will look like.
# 
# This is not always right, but it can usually
# get the <said> tag in the right place.
#
# The edits still need to be done by hand,
# but this makes them a lot faster.
#######################################

with open(STASHFILE,"a") as f:

    for said in said_tags:

        original_text = str(said)


        # This is a lot of tedious copypasta...

        sp14 = " "*14


        #####################################

        match1 = re.match(r'.* the (\w+) said, .*', original_text)

        if(match1):

            print("-"*40, file=f)
            print("Matched pattern \"the XXX said\"", file=f)
            print("Original:\n%s\n"%(sp14+original_text), file=f)

            orig_txt = re.sub('\n','@@@',original_text)

            new_text_closeopen   = re.sub(r'(.*)( the \w+ said)(.*)</said>', r'\1</said>\2<said who="???">\3</said>', orig_txt)
            new_text_closenoopen = re.sub(r'(.*)( the \w+ said)(.*)</said>', r'\1</said>\2\3', orig_txt)

            new_txt_co = re.sub('@@@','\n',new_text_closeopen)
            new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

            print("Fix 1:\n%s\n"%(sp14+new_txt_co ), file=f)
            print("Fix 2:\n%s\n"%(sp14+new_txt_cno), file=f)
    

        ##############################

        match2 = re.match(r'.* (\w+) said, .*', original_text)
    
        if(not match1 and match2):
    
            # if we find a "he said" or "she said", we want to mark it differently
            if(match2.group(1)=='he' or match2.group(1)=='she'):
                print("-"*40, file=f)
                print("Matched pattern \"he said, \" or \"she said, \"", file=f)
                print("Original:\n%s\n"%(sp14+original_text), file=f)

                orig_txt = re.sub('\n','@@@',original_text)

                new_text_closeopen   = re.sub(r'(.*)( \w+ said, )(.*)</said>', r'\1</said>\2<said who="???">\3</said>', orig_txt)
                new_text_closenoopen = re.sub(r'(.*)( \w+ said, )(.*)</said>', r'\1</said>\2\3', orig_txt)

                new_txt_co = re.sub('@@@','\n',new_text_closeopen)
                new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

                print("Fix 1:\n%s\n"%(sp14+new_txt_co), file=f)
                print("Fix 2:\n%s\n"%(sp14+new_txt_cno), file=f)
    
            else:
                likely_speaker = match2.group(1)
                print("-"*40, file=f)
                print("Matched pattern \"XXX said, \"", file=f)
                print("Likely Speaker: %s"%(likely_speaker), file=f)
                print("Original:\n%s\n"%(sp14+original_text), file=f)

                orig_txt = re.sub('\n','@@@',original_text)
    
                new_text_closeopen   = re.sub(r'<said who="\?\?\?">(.*)( \w+ said, )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2<said who="'+likely_speaker+r'">\3</said>', orig_txt)
                new_text_closenoopen = re.sub(r'<said who="\?\?\?">(.*)( \w+ said, )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2\3', orig_txt)

                new_txt_co = re.sub('@@@','\n',new_text_closeopen)
                new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

                print("Fix 1:\n%s\n"%(sp14+new_txt_co ), file=f)
                print("Fix 2:\n%s\n"%(sp14+new_txt_cno), file=f)






        #######################################

        match3a = re.match(r'.* the (\w+) said .*', original_text)

        if(not match1 and not match2 and match3a):

            likely_speaker = match3a.group(1)
            print("-"*40, file=f)
            print("Matched pattern \"the XXX said \"", file=f)
            print("Likely Speaker: %s"%(likely_speaker), file=f)
            print("Original:\n%s\n"%(sp14+original_text), file=f)
    
            orig_txt = re.sub('\n','@@@',original_text)

            new_text_closeopen   = re.sub(r'<said who="\?\?\?">(.*)( the \w+ said )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2<said who="'+likely_speaker+r'">\3</said>', orig_txt)
            new_text_closenoopen = re.sub(r'<said who="\?\?\?">(.*)( the \w+ said )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2\3', orig_txt)

            new_txt_co = re.sub('@@@','\n',new_text_closeopen)
            new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

            print("Fix 1:\n%s\n"%(sp14+new_txt_co ), file=f)
            print("Fix 2:\n%s\n"%(sp14+new_txt_cno), file=f)




        #######################################

        match3 = re.match(r'.* (\w+) said .*', original_text)

        if(not match1 and not match2 and match3):

            # if we find a "he said" or "she said", we want to mark it differently
            if(match3.group(1)=='he' or match3.group(1)=='she'):
                print("-"*40, file=f)
                print("Matched pattern \"he said \" or \"she said \"", file=f)
                print("Original:\n%s\n"%(sp14+original_text), file=f)

                orig_txt = re.sub('\n','@@@',original_text)

                new_text_closeopen   = re.sub(r'(.*)( \w+ said )(.*)</said>', r'\1</said>\2<said who="???">\3</said>', orig_txt)
                new_text_closenoopen = re.sub(r'(.*)( \w+ said )(.*)</said>', r'\1</said>\2\3', orig_txt)

                new_txt_co = re.sub('@@@','\n',new_text_closeopen)
                new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

                print("Fix 1:\n%s\n"%(sp14+new_txt_co ), file=f)
                print("Fix 2:\n%s\n"%(sp14+new_txt_cno), file=f)
    
            else:
                likely_speaker = match3.group(1)
                print("-"*40, file=f)
                print("Matched pattern \"XXX said \"", file=f)
                print("Likely Speaker: %s"%(likely_speaker), file=f)
                print("Original:\n%s\n"%(sp14+original_text), file=f)
    
                orig_txt = re.sub('\n','@@@',original_text)

                new_text_closeopen   = re.sub(r'<said who="\?\?\?">(.*)( \w+ said )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2<said who="'+likely_speaker+r'">\3</said>', orig_txt)
                new_text_closenoopen = re.sub(r'<said who="\?\?\?">(.*)( \w+ said )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2\3', orig_txt)

                new_txt_co = re.sub('@@@','\n',new_text_closeopen)
                new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

                print("Fix 1:\n%s\n"%(sp14+new_txt_co ), file=f)
                print("Fix 2:\n%s\n"%(sp14+new_txt_cno), file=f)



        #######################################

        match4a = re.match(r'.* the (\w+) said\. .*', original_text)

        if(not match1 and not match2 and not match3a and not match3 and match4a):

            likely_speaker = match4a.group(1)
            print("-"*40, file=f)
            print("Matched pattern \"the XXX said.\"", file=f)
            print("Likely Speaker: %s"%(likely_speaker), file=f)
            print("Original:\n%s\n"%(sp14+original_text), file=f)
    
            orig_txt = re.sub('\n','@@@',original_text)

            new_text_closeopen   = re.sub(r'<said who="\?\?\?">(.*)( the \w+ said\. )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2<said who="'+likely_speaker+r'">\3</said>', orig_txt)
            new_text_closenoopen = re.sub(r'<said who="\?\?\?">(.*)( the \w+ said\. )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2\3', orig_txt)

            new_txt_co = re.sub('@@@','\n',new_text_closeopen)
            new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

            print("Fix 1:\n%s\n"%(sp14+new_txt_co ), file=f)
            print("Fix 2:\n%s\n"%(sp14+new_txt_cno), file=f)




        #######################################

        match4 = re.match(r'.* (\w+) said\. .*', original_text)

        if(not match1 and not match2 and not match3a and not match3 
                and not match4a and match4):

            if(match4.group(1)=='he' or match4.group(1)=='she'):
                print("-"*40, file=f)
                print("Matched pattern \"he said.\" or \"she said.\"", file=f)
                print("Original:\n%s\n"%(sp14+original_text), file=f)

                orig_txt = re.sub('\n','@@@',original_text)

                new_text_closeopen   = re.sub(r'(.*)( \w+ said\. )(.*)</said>', r'\1</said>\2<said who="???">\3</said>', orig_txt)
                new_text_closenoopen = re.sub(r'(.*)( \w+ said\. )(.*)</said>', r'\1</said>\2\3', orig_txt)

                new_txt_co = re.sub('@@@','\n',new_text_closeopen)
                new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

                print("Fix 1:\n%s\n"%(sp14+new_txt_co ), file=f)
                print("Fix 2:\n%s\n"%(sp14+new_txt_cno), file=f)
    
            else:
                likely_speaker = match4.group(1)
                print("-"*40, file=f)
                print("Matched pattern \"XXX said.\"", file=f)
                print("Likely Speaker: %s"%(likely_speaker), file=f)
                print("Original:\n%s\n"%(sp14+original_text), file=f)
    
                orig_txt = re.sub('\n','@@@',original_text)

                new_text_closeopen   = re.sub(r'<said who="\?\?\?">(.*)( \w+ said\. )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2<said who="'+likely_speaker+r'">\3</said>', orig_txt)
                new_text_closenoopen = re.sub(r'<said who="\?\?\?">(.*)( \w+ said\. )(.*)</said>', r'<said who="'+likely_speaker+r'">\1</said>\2\3', orig_txt)

                new_txt_co = re.sub('@@@','\n',new_text_closeopen)
                new_txt_cno = re.sub('@@@','\n',new_text_closenoopen)

                print("Fix 1:\n%s\n"%(sp14+new_txt_co ), file=f)
                print("Fix 2:\n%s\n"%(sp14+new_txt_cno), file=f)

