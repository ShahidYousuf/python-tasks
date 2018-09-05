import os
import matplotlib.pyplot as plt
# execute command
def execute(command):
    try:
        result = os.popen(command)
    except (Exception):
        result = "Something Went Wrong\n"
    finally:
        return result
# save command results to file
def save_data(file,data):
    with open(file,'w') as f:
        for line in data:
            f.write(line)
        f.close()
# plot relevant data
def mtl_plot(xvalues, yvalues):
    fig, ax = plt.subplots()
    ax.bar(xvalues, yvalues, color="green")
    ax.set(xlabel="Process ID", ylabel="Memory (in KB's)", title="Process Real Memory Consumption Visual")
    ax.autoscale(True)
    xlabels = ax.get_xticklabels()
    plt.setp(xlabels, rotation=90)
    plt.grid()
    plt.show()

# test drive
if __name__ == '__main__':
    result = execute('ps aux')
    save_data('data_save1.txt',result)
    with open('data_save1.txt', 'r') as f:
        title = f.readline()
        title_list = title.strip('\n').split(" ")
        title_list2 = [item for item in title_list if len(item)>=1]
        title_cool = ' '.join(title_list2)
        print(title_cool)
        processes = []
        memory = []
        for line in f.readlines():
            lst = line.strip('\n').split(" ")
            # many things can be done with lst2
            lst2 = [item for item in lst if len(item)>=1]
            # these two lines are specifically made for command 'ps aux'
            processes.append(lst2[1])
            memory.append(int(lst2[5]))
            #print("{} {} {}".format(lst2[0], lst2[1], lst2[5]))
            l = ' '.join(lst2)
            # uncomment the below line to see the result on the console.
            #print("{}".format(l.capitalize()))
        # lets plot processes numbers versus memory consumed
        # this plot won't work for every command, makes sense!
        mtl_plot(processes[100:140], memory[100:140])
