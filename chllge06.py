# Input: '/Users/Joma/Documents/../Desktop/./../'
# Output: '/Users/Joma/'

def shortest_path(file_path: str):
    paths = file_path.split('/')

    i = 0
    while i < len(paths):
        if paths[i] == '.':
            del paths[i]
            i -= 1

        if paths[i] == '..':
            del paths[i]
            del paths[i-1]
            i -= 2
        i += 1

    return '/'.join(paths) 


print(shortest_path('/Users/Joma/Documents/../Desktop/./../'))

# /Users/Joma/
