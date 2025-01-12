def arithmetic_arranger(problems, show_answers=False):
    if len(problems)>5:
        return 'Error: Too many problems.'
    else:
        result=[]
        for i in problems:
            ls=i.split()
            if ls[1]!='-' and ls[1]!='+':
                return "Error: Operator must be '+' or '-'."
            elif not (ls[0].isdigit() and ls[2].isdigit()):
                return 'Error: Numbers must only contain digits.'
            elif max(len(ls[0]),len(ls[2]))>4:
                return 'Error: Numbers cannot be more than four digits.'
            else:
                x=max(len(ls[0]),len(ls[2]))+1
                y=str(eval(f"{int(ls[0])} {ls[1]} {int(ls[2])}")).rjust(x+1,' ')
                if show_answers==True:
                    result.append([(ls[0].rjust(x+1,' ')),
                    (ls[1]+ls[2].rjust(x,' ')),
                    ('-'*(x+1)),y])
                    a=4
                else:
                    a=3
                    result.append([(ls[0].rjust(x+1,' ')),
                    (ls[1]+ls[2].rjust(x,' ')),
                    ('-'*(x+1))])
                m=[]
                for g in range(a):
                    m.append('    '.join(x[g] for x in result))
        return  '\n'.join(m)
print(arithmetic_arranger(["3801 - 2", "123 + 49","1234 - 49","23 + 2"],True))