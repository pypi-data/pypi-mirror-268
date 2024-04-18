import json
import fitz
import re
# global variables
threshold_content_block= 10




def get_blocks(pdf_document, start_page_number):
    complete_list_blocks = []
    for i in range(start_page_number, pdf_document.page_count):
        page = pdf_document[i-1]
        curr_page_list_blocks = [[block[4], i]
                                 for block in page.get_text("blocks", sort=False)[:-3]]  # last 3 blocks removed to remove headers and footers
        # if the first block of the current page is a continuation of the last block of the previous page
        if len(complete_list_blocks) > 0:
            try:
                if curr_page_list_blocks[0][0][0].islower():
                    curr_page_list_blocks[0][0] = complete_list_blocks[-1][0]+curr_page_list_blocks[0][0]
                    curr_page_list_blocks.pop()
            except:
                pass
        
        complete_list_blocks.extend(curr_page_list_blocks)

    return complete_list_blocks

def label_contents(complete_list_blocks):
    most_recent_heading_block = ["the associated first text was supposed to be the heading of the first content block", 0]
    headings_list = []
    contents_list = []
    last_content_window_list =[]
    for block in complete_list_blocks:
        if block[0].strip() == "": 
            continue
        num_words = len(block[0].split(" "))
        # block[0] starts with the a natural number followed by a period
        if re.match(r"^\d+\.", block[0]):
            last_content_window_list.append(block[0])
            continue
        if num_words < threshold_content_block:
            if last_content_window_list and most_recent_heading_block:
                headings_list.append(most_recent_heading_block)
                contents_list.append(last_content_window_list)
                last_content_window_list = []
            most_recent_heading_block = block
        else:
            last_content_window_list.append(block[0])
    return headings_list, contents_list

def segment_document(file_path):
    pdf_document = fitz.open(file_path)
    book_title = pdf_document.metadata['title'].upper()
    start_page_number = pdf_document.get_toc()[2][2]

    # #
    # #
    toc = pdf_document.get_toc()[2:]
    # #
    # # 
   
    complete_list_blocks = get_blocks(pdf_document, start_page_number) 
    headings_list, contents_list = label_contents(complete_list_blocks)
    json_list = []
    

    for heading, content in zip(headings_list, contents_list):
        json_data = {
        "level1": [book_title, 0],
        "level2": heading,
        "text": content
                }
        json_list.append(json_data)
    return json_list
 