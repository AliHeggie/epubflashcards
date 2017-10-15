# epubflashcards
Create an epub of flash cards from markdown files

##15/10/2017

Having difficulty getting links to work correctly.

I want the link to be to the title so that kindle shows the full page. pubcards now sets the header id using `{#id}`. This works fine for links when I use markdown preview. However, pandoc thinks this header attribute is just part of the header it seems.

In principle it must be possible to do it this way - The links work when I save the markdown preview and convert this html to epub with calibre.

How about, instead of pandoc I use https://pythonhosted.org/Markdown/ and then calibre to do the convert?

`pip install markdown`

Does not seem to process header attributes. I think I need the attributes eature from here: https://pythonhosted.org/Markdown/extensions/extra.html

**Solved** use extensions.header_attributes option in pandoc and make sure each identifier has a leading non number