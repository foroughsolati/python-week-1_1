my_list=['milk','notebook','tomato']

def add_list():
    new_list=input('please enter new required items' )
    my_list.append(new_list)

def remove_list():
     new_list=input(' please Remove the extra item.')
     for i in my_list:
         if (new_list== i):
               my_list.remove(new_list)
               break
     else:
           print('your input not in my_list,please enter a new item')

def show_list():
     print(my_list)

def exit_list():
         print ('Exit of list')

text=int(input('please enter a number between 1 to 4'))
while text<1 or text>4:
    text= int(input('please enter new number'))

if text==1:
    add_list()
elif text==2:
    remove_list()
elif text==3:
    show_list()
elif text==4:
    exit_list()
