#!/usr/bin/env python
# coding: utf-8

# In[90]:


import PyPDF2

# In[3]:


def remove_capped_words(my_text):

    '''
    Requires text string
    Returns capitalised words
    '''

    no_upper_list = []

    for word in my_text.split(' '):
        if word.isupper() is False:
            no_upper_list.append(word)
        else:
            pass

    text = ' '.join(no_upper_list)

    return text


# In[4]:


def extract_pdf_text(pdf_name):

    '''
    Requires directory + name of pdf file
    Returns all text of pdf
    '''

    # define file details

    pdfFileObj = open(pdf_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    page_list = []

    for page in range(0, pdfReader.numPages):

        # apply text extraction to all pages

        pageObj = pdfReader.getPage(page)
        page_content = pageObj.extractText()

        page_list.append(page_content)

    all_text = ''.join(page_list)
    all_text = remove_capped_words(all_text)

    return all_text


# In[ ]:
