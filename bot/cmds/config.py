#######################################################
#                                                     #
#      BFY Entertainment                              #
#      Written-by: J.H.Lee                            #
#      (jhlee@bfy.kr)                                 #
#                                                     #
#######################################################

import sys

if __name__ == "__main__":
    print("Please execute bot.py")
    sys.exit(0)

import discord, logging, os
from discord.ext import commands

# Owner Setting
owner = [0]  # owner IDs as list / 소유자(슈퍼오너)의 ID를 리스트로 모두 입력해주세요.
token = ""  # bot token / 봇 토큰
invlink = ""  # invite link / 초대 링크
vernum = "v1.3.1"  # version info / 버전 정보
prefix = ""  # prefix / 프리픽스
botname = ""  # bot's name / 봇 이름
hasmusic = False  # whether there is a music function / 음악 기능을 추가로 제공하는지
botcolor = 0x008EFE  # bot color / 봇의 색상
musicstr = "음악 기능은 외부 프로그램을 통해 제공됩니다."  # notice about music function
helpmusicstr = "#help를 입력해주세요."  # help command of music function
# End

pending, noticed, using, muted = [], [], [], []

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
bot = commands.Bot(command_prefix=prefix + " ", intents=intents, help_command=None)

try:
    if not os.path.exists("./bbdata"):
        os.makedirs("./bbdata")
except OSError:
    print("EMERG - Error: Creating directory. " + "./bbdata")

formatter = logging.Formatter("[%(asctime)s] [%(levelname)s]: %(message)s")
eventlogger = logging.getLogger("event")
eventlogger.setLevel(logging.DEBUG)
console = logging.StreamHandler()
console.setLevel(logging.WARNING)
console.setFormatter(formatter)
filehandler = logging.FileHandler(filename="./bbdata/log.txt", encoding="utf-8")
filehandler.setLevel(logging.DEBUG)
filehandler.setFormatter(formatter)
eventlogger.addHandler(console)
eventlogger.addHandler(filehandler)