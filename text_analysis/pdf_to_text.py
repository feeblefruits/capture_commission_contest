
# coding: utf-8

# In[90]:


import PyPDF2


# In[91]:


def extract_pdf_text(pdf_name):
    
    # define file details
    
    pdfFileObj = open(pdf_name, 'rb')
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
    
    def get_page_text(page_number):
        
        # extract text from one page

        pageObj = pdfReader.getPage(page_number)
        page_content = pageObj.extractText()

        return page_content
    
    page_list = []

    for page in range(0, pdfReader.numPages):
        
        # apply text extraction to all pages

        page_list.append(get_page_text(page))

    all_text = ''.join(page_list)
    
    def remove_capped_words(my_text):
        
        # remove all_capped_words

        no_upper_list = []

        for word in my_text.split(' '):
            if word.isupper() is False:
                no_upper_list.append(word)
            else:
                pass

        text = ' '.join(no_upper_list)

        return text
    
    return remove_capped_words(all_text)

