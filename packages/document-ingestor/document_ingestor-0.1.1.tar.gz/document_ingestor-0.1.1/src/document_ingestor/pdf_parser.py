import fitz
import json
import re
import os


class Node:
    def __init__(self, val, children=None):
        self.val = val
        self.children = children if children is not None else []


def build_tree(preorder):
    def helper(level):
        if preorder and preorder[0][0] == level:
            element = preorder.pop(0)
            # print(element)
            val = [element[1], element[2], element[3]]
            node = Node(val)
            while preorder and preorder[0][0] > level:

                child = helper(preorder[0][0])
                node.children.append(child)
            return node

    return helper(0)


def print_tree(node, level=0):
    if node is None:
        return
    print("  " * level + str(node.val))
    for child in node.children:
        print_tree(child, level + 1)


def extract_hyperlinks_from_toc(pdf_path):
    doc = fitz.open(pdf_path)
    toc = doc.get_toc()
    return toc


def dfs(node, level, result, list):
    if node is None:
        return
    json_obj = {}
    list.append((node.val[0], node.val[1]))
    for item in list:
        json_obj['level'+str(list.index(item)+1)] = item
    json_obj['text'] = node.val[2]
    result.append(json_obj)
    for child in node.children:
        dfs(child, level+1, result, list)
    list.pop()


def create_json_list(root):
    result = []
    dfs(root, 1, result, [])
    return result


def get_contents(pdf_path="/home/manandraj20/AI_services/SpanishDocSearch/sample/Seguridad Nacional/BOE-404_Seguridad_Nacional_Organos_competentes_de_la_Seguridad_Nacional.pdf"):
    pdf_document = fitz.open(pdf_path)
    start_page_number = pdf_document.get_toc()[2][2]
    print(start_page_number)
    hyperlinks = pdf_document.get_toc()
    new_list = []
    for inner_list in hyperlinks:
        txt = inner_list[1]
        # print(txt)
        x = txt.split(".")
        inner_list[1] = x[0]
        if not inner_list[1].startswith('['):
            new_list.append(inner_list)
            # print(inner_list[1])
    hyperlinks = [hyperlink[1] for hyperlink in new_list][2:]
    # reverse the list
    # print(hyperlinks)

    hyperlinks.reverse()
    print("len hyperlinks:"+str(len(hyperlinks)))
    # print(hyperlinks)
    pages = []
    # print(hyperlinks)
    # print(pdf_document[24].number)
    for page in pdf_document:
        if page.number >= start_page_number-1:
            pages.append(page)

    # blocks_list = [block[4]
    #                for page in pages for block in page.get_text("blocks", sort=False)[:-3]]
    blocks_list = []
    for page in pages:
        blocks = [block[4]
                  for block in page.get_text("blocks", sort=False)[:-3]]
        if len(blocks_list) > 0:
            try:
                if blocks[0][0].islower():
                    blocks[0] = blocks_list[-1]+blocks[0]
                    blocks_list.pop()
            except:
                pass
            # if blocks[0][0].islower():
            #     blocks[0] = blocks_list[-1]+blocks[0]
            #     blocks_list.pop()       We had to use this try and except as the above was not working properly with pymupdf==1.23.11
        blocks_list.extend(blocks)
    # print(blocks_list)
    contents_list = []
    temp_list = []
    start_text = "start"
    translation_table = str.maketrans({ord('\xa0'): ' ', ord('\x00'): ' ', ord(
        '\x01'): ' ', ord('\x02'): ' ', ord('\x03'): ' ', ord('\x04'): ' '})
    done = False
    for block in blocks_list:
        # check if the hyperlinks is empty
        if len(hyperlinks) > 0:
            current_heading = hyperlinks[-1]
            current_heading = current_heading.strip()
            current_heading = current_heading.replace('\n', '')

            modified_block = block.replace('\n', '')
            modified_block = modified_block.strip()

            # modified_block = block.strip()
            # block = block.replace('\n', '')
            block = block.strip()
            if not block:
                continue
            if modified_block.startswith(current_heading.upper()) or block.startswith(current_heading) or block.startswith(current_heading.upper()) or modified_block.startswith(current_heading) or modified_block.startswith(current_heading.translate(translation_table)) or current_heading.translate(translation_table).startswith(modified_block):
                # print(start_text+":")
                start_text = hyperlinks.pop()
                # print(start_text+":"+block)
                contents_list.append(temp_list)

                # contents_list.append(temp_list)

                # print(temp_list)
                temp_list = []
            else:
                temp_list.append(block)

        else:
            temp_list.append(block)

    # print(start_text+":")
    # print(temp_list)
    contents_list.append(temp_list)
    # contents_list.pop(0)
    print("len(contents_list):"+str(len(contents_list)))
    return contents_list


def process_pdf(pdf_path):
    pdf_document = fitz.open(pdf_path)
    hyperlinks = pdf_document.get_toc()[2:]
    hyperlinks.insert(0, [0, pdf_document.metadata['title'].upper(), 0])

    # .split function
    new_list = []
    hyperlinks_raw = []
    for inner_list in hyperlinks:
        txt = inner_list[1]
        # print(txt)
        x = txt.split(".")
        inner_list[1] = x[0]
        if not inner_list[1].startswith('['):
            new_list.append(inner_list)
            inner_list[1] = txt
            hyperlinks_raw.append(inner_list)
            # print(inner_list[1])
    hyperlinks = new_list

    contents = get_contents(pdf_path=pdf_path)
    print("[contents generated]")
    # print(contents)
    print(len(contents))
    print(len(hyperlinks))
    for idx, item in enumerate(hyperlinks_raw):
        item.append(contents[idx])
    # print(hyperlinks)

    root = build_tree(hyperlinks_raw)
    print("[tree built]")
    # print_tree(root,0)
    json_list = create_json_list(root)
    return json_list
