import random


def generate_all_subsets(s):
    result = []


    def generateHelper(s, i, slate):

        if i == len(s):
            result.append(''.join(slate))

        else:
            print(i)
            generateHelper(s, i + 1, slate)

            slate.append(s[i])
            generateHelper(s, i + 1, slate)
            slate.pop()

    generateHelper(s, 0, [])
    return result

#print(generate_all_subsets('xy'))


def generate_all_expression(s,target):

    result = []
    exp_out = 0


    def generate_helper(s,i,slate,exp_out):

        if i == len(s):
            return result.append(''.join(slate))

        else:
            if i == 0 :
                slate.append(s[i])
                exp_out = s[i]
                generate_helper(s, i + 1, slate,0)
                slate.pop()
            else :
                for sign in ['+','*','join']:
                    if sign = '+':



                    slate.append(sign)
                    slate.append(s[i])
                    generate_helper(s,i+1,slate,0)
                    slate.pop()
                    slate.pop()


    generate_helper(s,0,[],exp_out)
    return result,len(result)

print(generate_all_expression('222',4))