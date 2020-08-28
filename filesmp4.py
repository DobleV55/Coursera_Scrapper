from os import listdir
import os
import re
import wget


def download_from_files():
    link_file = open('coursera_links.txt')
    title_file.readlines()
    lines = link_file.readlines()
    for line in lines:
        wget.download(line)


def rename_download_files():
    title_file = open('coursera_titles')
    titles = title_file.readlines()
    files = listdir('.')
    for f in files:
        if '_' in f:
            numb = int(re.search(r'\d+', f).group())
            title = titles[numb]
            f_mp4 = f[:-1]
            f_mp4 = f+'.mp4'
            os.rename(f, f_mp4)


if __name__ == "__main__":
    download_from_files()
    rename_download_files()
