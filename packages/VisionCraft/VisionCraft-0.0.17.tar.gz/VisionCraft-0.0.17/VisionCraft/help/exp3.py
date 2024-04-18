import shutil

def download(destination_path = "./"):
    shutil.copy("./Experiment/Exp3.ipynb", destination_path)