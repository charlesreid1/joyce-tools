# Joyce Tools

This repo contains tools for parsing/fixing/analyzing Joyce's texts. 

It primarily uses [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) (`bs4`) 
and [regular expressions](https://docs.python.org/3/library/re.html) (`re`).

To use BeautifulSoup on Mac OS X, you may need to run this first:

```
pip install lxml
```

## Portrait

The `portrait/` directory contains scripts for cleaning up Joyce's Portrait; see
[https://github.com/open-editions/corpus-joyce-portrait-TEI](https://github.com/open-editions/corpus-joyce-portrait-TEI).

### `find_said_problems.py`

This searches the document for `<said>` tags in which the actual words spoken
contain the word "X said", "he said", etc. 

It then suggests a few ways of fixing the `<said>` tags.

*This script is designed to aid in manual fixes to `<said>` tags in the text and is not fully automated.*

## Ulysses

The `ulysses/` directory contains scripts for cleaning up Joyce's Ulysses; see
[https://github.com/open-editions/corpus-joyce-ulysses-tei](https://github.com/open-editions/corpus-joyce-ulysses-tei).

### `find_street_addesses.sh`

The `find_street_addresses.sh` script searches for patterns that might yield street addresses
or place names for tagging with `<place>`.

Summary of operation:
* Clean `<lb>` and `<said>` tags
* Use grep to search for `[0-9]\{1,3\}` - 1-3 digit numbers - or `street`
* Put the results in a file for review

*This script is designed to aid in manual additions of `<place>` tags in the text and is not fully automated.*


