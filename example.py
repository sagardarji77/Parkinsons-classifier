from tkinter import *
import tkinter.messagebox as tm
import numpy as np
from sklearn import preprocessing
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
import pandas as pd


class LoginFrame(Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label_data = Label(self, text="Enter the values \n'MDVP:Fo(Hz),MDVP:Fhi(Hz)\n,MDVP:Flo(Hz),MDVP:Jitter(%),MDVP:Jitter(Abs)\n,MDVP:RAP,MDVP:PPQ,Jitter:DDP\n,MDVP:Shimmer,MDVP:Shimmer(dB)\n,Shimmer:APQ3,Shimmer:APQ5,MDVP:APQ\n,Shimmer:DDA,NHR,HNR,status,RPDE\n,DFA,spread1,spread2,D2,PPE'")
        self.entry_data = Entry(self)

        self.label_data.grid(row=0, sticky=E)


        self.entry_data.grid(row=0, column=1)

        self.logbtn = Button(self, text="submit", command=self._submit_btn_clicked)
        self.logbtn.grid(columnspan=2)

        self.pack()

    def _submit_btn_clicked(self):
        data = self.entry_data.get()
        data = data.split(',')
        df = pd.read_csv('parkinsons.data.txt')
        df.replace('?', -99999, inplace=True)
        df.drop(['name'], 1, inplace=True)
        print(df.shape)

        x = np.array(df.drop(['status'], 1))
        y = np.array(df['status'])

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

        clf = KNeighborsClassifier(n_neighbors=5)
        clf.fit(x_train, y_train)
        accuracy = clf.score(x_test, y_test)
        predict = clf.predict([data])
        str1 = "Parkinson\nAccuracy : "+str(accuracy)
        str2 = "Healthy\nAccuracy : "+str(accuracy)
        if predict[0] == 1:
            tm.showinfo("Test Result", str1)
        else:
            tm.showinfo("Test Result", str2)


root = Tk()
lf = LoginFrame(root)
root.mainloop()
