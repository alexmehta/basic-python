from argparse import ArgumentParser
from colored import fg, attr
from environs import Env
from glob import glob
import Levenshtein
from math import inf
from multiprocessing import cpu_count, Pool
from os import access, chdir, getcwd, unlink, W_OK
from os.path import basename, isfile, join
from youtube_api import YouTubeDataAPI
from youtube_dl import YoutubeDL, DownloadError