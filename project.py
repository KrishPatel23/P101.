import dropbox
import os 
from dropbox.files import WriteMode
class Transferdata:
    def __init__(self, accesstoken):
        self.accesstoken=accesstoken
    def uploadfile(self, filefrom, fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        for root, dirs, files in os.walk(filefrom):
            for filename in files:
                localpath = os.path.join(root,filename)
                relativepath = os.path.relpath(localpath, filefrom)
                dropboxpath = os.path.join(fileto, relativepath)
                with open(localpath,'rb') as f:
                    dbx.files_upload(f.read(),dropboxpath, mode=WriteMode('overwrite'))
def main():
    accesstoken='sl.AxK9Db6O4coMYUxVphnXTNp5pFiU8NrBXuLHmVJi0FBw4b7DehwLusXarxqHBXkjqxRYa7aiMLigzdFnFxOpKMuTs002vhhaYtgquZZZRne-rlB0kngvVCgxNymSD70zIDQA8Lrf4tnZ'
    transferdata=Transferdata(accesstoken)
    filefrom=r"C:/Users/munna/Desktop/Krish"
    fileto="/Dropbox/"
    transferdata.uploadfile(filefrom,fileto)

main()
