def count_substring(string, sub_string):
    k = 0
    a = string.find(sub_string)
    while a != -1:
        k += 1
        a = string.find(sub_string, a + 1)
        
    return k

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
