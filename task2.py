import re

b = """Lorem Ipsum is simply dummy 
text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled 
it to make a type specimen book?/. It has survived not only five centuries,
but also the leap into electronic typesetting, remaining essentially unchanged.
It was popularised in the 1960s with the release of Letraset sheets 
containing Lorem Ipsum passages, and more recently with desktop publishing software like 
Aldus PageMaker including versions of Lorem Ipsum.!?"""


def top3(text, n):
    res_dict = dict()
    text_cleared = re.sub(r"[?|$|.|?|!|.|,|/|@|\n]", r" ", text).split(" ")  # clearing from special symbols and splitting all the text

    for i in text_cleared:  # lopping over text
        if i.lower() not in res_dict.keys():  #
            res_dict[i.lower()] = 1
        else:
            res_dict[i.lower()] += 1

    if "" in res_dict:  # if "" exists then delete it
        del res_dict[""]

    if len(res_dict.keys()) < 3:  # if number of our numbers is less then 3 then returning empty list
        return list()

    return sorted(res_dict, key=res_dict.get, reverse=True)[:n]  # sorting by our values and selecting first n-numbers


if __name__ == "__main__":
    print(top3(b, 3))
    print(top3(b, 2))
    print(top3(b, 1))
