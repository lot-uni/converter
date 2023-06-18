import os

def anser_format(name,path):
    with open(f'{path}/{name}') as f:
        file_read = f.read()
    formats=['    Anser(',f'        title: "{name.split(".")[0]}",',f'        detail: "{file_read}"','    ),']
    with open(f'{os.getcwd()}/output/Anser', "a") as file:
        file.writelines(map(lambda x:f'{x}\n',formats))

def anser_enumerate(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if '.md' in file:
                anser_format(file,root)

with open(f'{os.getcwd()}/output/Anser', "w") as file:
    file.writelines('[\n')
anser_enumerate(os.getcwd())
with open(f'{os.getcwd()}/output/Anser', "a") as file:
    file.writelines(']')

# ___________________________________________________

def question_format(path,Q_num,A_num):
    if '：' in path.split('/')[-1]:
        title=path.split('/')[-1].split('：')[1]
        format_before=['    Question(',f'        message: "{title}",',f'        choices: [']
        format_after=['        ]','    ),']
        choices=[]
        for text in [f for f in os.listdir(path) if not f.startswith('.')]:
            bol=len([f for f in os.listdir(f'{path}/{text}') if (not f.startswith('.')) and (not f.endswith('.md'))])==0
            if not bol:
                Q_num+=1
                choices.append(f'            Choice(text: "{text.split("：")[0]}", next:{Q_num}, finish:false),')
            else:
                A_num+=1
                choices.append(f'            Choice(text: "{text}", next:{A_num}, finish:true),')
        form=format_before+choices+format_after
        with open(f'{os.getcwd()}/output/Question', "a") as file:
            file.writelines(map(lambda x:f'{x}\n',form))
    return Q_num,A_num
def count(path,Q_count,A_count):
    files = os.listdir(path)
    if files:
        Q_count,A_count=question_format(path,Q_count,A_count)
        return Q_count,A_count

def question_enumerate(folder_path,Q_count,A_count):
    for root, dirs, files in os.walk(folder_path):
        for dir in dirs:
            resolve=count(os.path.join(root, dir),Q_count,A_count)
            if resolve:
                Q_count,A_count=resolve


with open(f'{os.getcwd()}/output/Question', "w") as file:
    file.writelines("[\n")
question_enumerate(os.getcwd(),0,-1)
with open(f'{os.getcwd()}/output/Question', "a") as file:
    file.writelines("]")