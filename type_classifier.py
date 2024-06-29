def message(string1):
    try:
        if '!' in string1:
            info = "it is an exclamatory sentence"
        elif '?' in string1:
            info="it is an interrogative sentence"
        elif '.' in string1:
            list1 = ['please', 'go', 'do', 'get', 'close', 'may']
            for i in list1:
                if i in string1:
                    info="it is an imperative sentence"
                    break
                else:
                   info="it is a simple sentence"
        else:
            info = "incomplete senetnce; missing: punctuation"
        return info
    except:
        pass
