
import  re
def	apply_to_list(some_list,f):
    return	[f(x)	for	x	in	some_list]
ints = [4,	0,	1,	5,	6]
a = apply_to_list(ints,	lambda x:x*2)
print(a)

"""
states	=	['			Alabama	',	'Georgia!',	'Georgia',	'georg ia',	'FlOrIda',	'south	carolina##',	'West	virginia?']

def	remove_punctuation(value):
    return re.sub('[\t!#?]',' ',value)

for x in map(remove_punctuation,states):
    print(x)

clean_ops =	[remove_punctuation,str.strip,str.title]
def	clean_strings(strings,ops):
    result = []
    for	value in strings:
        for	function in	ops:
            value =	function(value)
        result.append(value)
    return result
a = clean_strings(states,clean_ops)
print(a)
"""