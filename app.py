from flask import *

app = Flask(__name__)


@app.route('/',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        st=request.form.get('st')
        st_sp=st.split('_')
        file = open("C:\\Users\\YOONES-NIA\\PycharmProjects\\pythonProject4,1\\students3.txt", 'r')
        line = file.readline()
        names=[]
        avg_score=0
        while line:
            words = line.split()
            names.append(words[0] + '_' + words[1])
            if words[0]==st_sp[0] and words[1]==st_sp[1]:
                avg_score=(float(words[2])+float(words[3])+float(words[4]))/3
                break
            line = file.readline()
        return render_template('index.html',names=names,name=st, avscore=avg_score)
    else:
        file=open("C:\\Users\\YOONES-NIA\\PycharmProjects\\pythonProject4,1\\students3.txt",'r')
        line=file.readline()
        names=[]
        while line:
            words=line.split()
            names.append(words[0]+'_'+words[1])
            line = file.readline()
        print(names)
        return render_template('index.html',names=names)

if __name__ == '__main__':
    app.run()
