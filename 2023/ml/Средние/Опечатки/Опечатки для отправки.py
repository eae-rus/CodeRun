import sys

def main():
    '''
    Реализовал через дерьвья поиска    
    '''
    def find_all_substrings(string, substring):
        indices = []
        index = 0
        while index < len(string):
            index = string.find(substring, index)
            if index == -1:
                break
            indices.append(index)
            index += 1
        return indices

    def replacement_tree(expected_word, mistake_word, substitutions, iterration = 0):
        '''
        '''
        iterration += 1
        min_iterration = 5
        
        for expected_sub, mistake_sub in substitutions:
            mistake_sub_len = len(mistake_sub)
            indices = find_all_substrings(mistake_word, mistake_sub)
            if len(indices) == 0:
                continue
            for index in indices:
                new_mistake_word = mistake_word[:index] + expected_sub + mistake_word[index + mistake_sub_len:]
                if new_mistake_word == expected_word:
                    return iterration
                else:
                    if iterration >= 4:
                        continue
                    new_min_iterration = replacement_tree(expected_word, new_mistake_word, substitutions, iterration)
                    if new_min_iterration < min_iterration and new_min_iterration != -1:
                        min_iterration = new_min_iterration
        
        if min_iterration == 5:
            return -1
        else:
            return min_iterration
        
    expected_word = input()
    mistake_word = input()
    n = int(input())
    substitutions = []
    for _ in range(n):
        expected_sub, mistake_sub = input().split()
        if expected_sub != mistake_sub:
            substitutions.append([expected_sub, mistake_sub])

    if expected_word == mistake_word:
        print(0)
        sys.exit()
    print(replacement_tree(expected_word, mistake_word, substitutions))

if __name__ == '__main__':
	main()