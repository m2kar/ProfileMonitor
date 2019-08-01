import crawlers

'''
type information:
    "ID": find all html tags who's attribute id = ID, and save the areas
    "ID_KEY_ACC": find all html tags who's attribute id = ID and 
    "ID_KEY_CONTAIN": find all html tags who's attribute id = ID and 
    "CLASS":
    "CLASS_KEY_ACC":
    "CLASS_KEY_CONTAIN":
    "KEY_ACC":
    "KEY_CONTAIN":
    "TAG_TREE":
'''

# 1. input: a file, which contain several lines config info
#           each line's format: url <type> <parameter1> <parameter2> ...
# 2. output: a list of dict, each dict contain "url", "type" and "parameters", 
#           "parameters" is a list.
# I didn't check the format, so if the format is wrong, there will be some error
def reader(file_name):
    result = []
    try:
        with open(file_name) as f:
            for line in f:
                web_item = {}
                line_content = line.split()
                if(len(line_content) >= 1):
                    web_item["url"] = line_content[0]
                if(len(line_content) >= 2):
                    web_item["type"] = line_content[1]
                parameters = []
                if(len(line_content) >= 3):
                    for i in line_content[2:]:
                        parameters.append(i)
                    web_item["parameters"] = parameters
                result.append(web_item)
    except:
        print("reader(): There is some error!")
    finally:
        f.close()
    return result


# 1. input: a dict, which must contain following keys: "url", "type" and "parameters"
# 2. process: according to the dict's "type" key to decide which crawler method to use
def judger(web_type_param):
    try:
        if web_type_param.get("type") == "IDS" :
            crawlers.crawler_ids(web_type_param["url"],web_type_param["parameters"])
        elif web_type_param.get("type") == "KEYS" :
            crawlers.crawler_keys(web_type_param["url"],web_type_param["parameters"])
        else :
            crawlers.crawler_all(web_type_param["url"])
    except:
        print(str(web_type_param.get("type")) + ":judger(): There is some error!")
        pass
        
def main():
    web_type_list = reader("/home/ztx/follower/MonitedSitesAndconfig.txt")
    for web_item in web_type_list:
       judger(web_item)

if __name__ == '__main__':
    main()
