import shutil

def download(destination_path = "./"):
    shutil.copy("./Experiment/Exp2.ipynb", destination_path)