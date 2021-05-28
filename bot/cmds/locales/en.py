"""
    Copyright (C) 2021 BFY Entertainment
    All right reserved

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

if __name__ == "__main__":
    import sys

    print("Please execute bot.py")
    sys.exit(0)

locale_en = {
    "dictcmd_error_notadmin": "If it's not an administrator, I won't do it",
    "dictcmd_error_err": "There was an error.. :( The report was automatically generated",
    "dictcmd_checka_delete": "delete",
    "dictcmd_checkb_yes": "yes",
    "dictcmd_checkb_no": "no",
    "dictcmd_checkd_report": "report",
    "dictcmd_checkd_change": "change",
    "dictcmd_general_deleted": "Deleted :)",
    "dictcmd_general_yes": "yes",
    "dictcmd_general_no": "no",
    "dictcmd_general_editing": "Someone is editing ;)",
    "dictcmd_general_using": "Already using ;)",
    "dictcmd_general_question": "What would you say?",
    "dictcmd_general_emptyerr": "Can't register empty message",
    "dictcmd_general_limiterr": "Maximum length is 100 characters",
    "dictcmd_general_acpedit": "ㅇㅋ `💰-100000`",
    "dictcmd_general_cancel": "Okay don't hate it",
    "dictcmd_general_npntedit": "I'll earn 100000 points",
    "dictcmd_report_title": "New report",
    "dictcmd_report_cmd": "Question",
    "dictcmd_report_reply": "reply",
    "dictcmd_report_reason": "reason",
    "dictcmd_report_author": "author",
    "dictcmd_report_reported": "The response has been reported. The reported response will be reviewed by the administrator and taken action.",
    "dictcmd_general_ownercfmnew": "Master, do you need a new command",
    "dictcmd_general_cfmnew": "Will you give me an answer using 50000 points?",
    "dictcmd_general_cancel2": "What do you say?",
    "dictcmd_general_ownerquestion": "What do you want, lord.",
    "dictcmd_general_owneracpnew": "The owner registered.",
    "dictcmd_general_ownercancel": "Okay Master",
    "economy_seemoney_0": "{0} you have this much money Did you know `💰 {1}`",
    "economy_getmoney_1": "brother",
    "economy_getmoney_2": "Oh, poor man, I specially give you 1000 points `💰+1000`",
    "economy_getmoney_3": "I hate it~~Eve",
    "economy_getmoney_4": "What are you saying ㅋㅋ",
    "economy_getmoney_5": "Where would you like to take it and use it? ㅋㅋ `💰+100`",
    "economy_getmoney_6": "Brother try it",
    "economy_getmoney_7": "If you only have high self-esteem, ㅉㅉ",
    "economy_getmoney_8": "It's right, it's good, it's good old gift `💰+2500`",
    "economy_getmoney_9": "Why do I give you money?",
    "economy_getmoney_10": "ㄲㅈ",
    "economy_seeothermoney_0": "Sorry, please mention the target person.",
    "economy_seeothermoney_1": "Sorry, please mention only 1 target.",
    "economy_seeothermoney_2": "{0} Did you know that this friend has this much money `💰 {1}`",
    "economy_seestk_0": "{0} you have this much stock A: {1} shares / B: {2} shares / C: {3} shares",
    "economy_seeotherstk_0": "Sorry, please mention the subject.",
    "economy_seeotherstk_1": "Sorry, please mention only 1 target.",
    "economy_seeotherstk_2": "{0} This friend has this much stock A: {1} shares / B: {2} shares / C: {3} shares",
    "economy_sendmoney_0": "This amount cannot be gifted.",
    "economy_sendmoney_1": "Please mention the target person.",
    "economy_sendmoney_2": "Please mention only 1 target person.",
    "economy_sendmoney_3": "You gave {0} a gift of `💰 {1}`.",
    "economy_sendmoneyerror_0": "Please enter the amount correctly.",
    "economy_sendmoneyerror_1": "I think you entered something wrong,,",
    "economy_sendmoneyerror_2": "There was an error.. :( The report was automatically generated",
    "game_gamble_0": "You sound like gambling with no money",
    "game_gamble_1": "How much will it be? Balance: `💰 {0}`",
    "game_gamble_2": "If you don't do it, ㄲㅈ",
    "game_gamble_3": "Start the game with {0} points",
    "game_gamble_4": "You sound like gambling with no money",
    "game_gamble_5": "Please give me the correct number?",
    "game_gamble_6": "Honey--God'💰-{0}`",
    "game_gamble_7": "I'm full to eat 0.5 times lol `💰-{0}`",
    "game_gamble_8": "Honey--I tried to regret it and put up with it... After... `💰+0`",
    "game_gamble_9": "Twice times... isn't that bad? `💰+{0}`",
    "game_gamble_10": "4 times this year'💰+{0}`",
    "game_gamble_11": "Hey, take this 6 times `💰+{0}`",
    "game_gamble_12": "8 back and... `💰+{0}`",
    "game_gamble_13": "You're lucky 10 times? `💰+{0}`",
    "game_gamble_14": "I'll be a beggar. Isn't it 50 times too much? `💰+{0}`",
    "game_stock_0": "`{0} stocks (graph|buy|sell|statistics) (A|B|C|ENT|CORP|AT7)` is the correct usage ^^",
    "game_stock_1": "Current price: {0}",
    "game_stock_2": "This is a graph of {0}.",
    "game_stock_3": "You sound like stock without money",
    "game_stock_4": "How many would you like to buy? Balance: `💰 {0}`, Current price: {1}, Available quantity: {2} shares",
    "game_stock_5": "Go if you don't live",
    "game_stock_6": "Please enter the correct quantity",
    "game_stock_7": "The maximum stock holding is 100,000 shares.",
    "game_stock_8": "You have purchased {0} shares. `💰-{1}`",
    "game_stock_9": "Sounds like sell without stock",
    "game_stock_10": "How much will you sell? Current price: {0}, Available quantity: {1} shares",
    "game_stock_11": "Go if you don't sell",
    "game_stock_12": "You sold {0} shares. `💰+{1}`",
    "game_stock_13": "I couldn't find the transaction details haha;",
    "game_stock_14": "buy",
    "game_stock_15": "Sell",
    "game_stock_16": "{0}-{1} points-{2} weeks-total {3} points",
    "game_stock_17": "{0} stock transaction details.",
    "general_version_0": "{0} version",
    "general_version_1": "current version",
    "general_version_2": "discord.py version",
    "general_version_3": "producer",
    "general_version_4": "Check server status",
    "general_version_5": "music features of {0}",
    "general_version_6": "{0} version information",
    "general_help_0": "how to use {0}",
    "general_help_1": "Help (online)",
    "general_help_2": "music help",
    "general_help_3": "Inquiry",
    "general_help_4": "If you send a DM to the bot, a message will be delivered to the operator.\nHomepage: https://www.bfy.kr/ Developer email: jhlee@bfy.kr\nDeveloper Discord: KRMSS#9279",
    "general_help_5": "Receive maintenance instructions",
    "general_help_6": "You are the administrator of {0}! We recommend that you receive notices such as maintenance through the `{1} subscription #channel` command!",
    "general_help_7": "how to order {0}",
    "general_help_8": "Help delivery failed :( Please check if DM is blocked!",
    "general_docalculate_0": "The calculation result is {0}! (If it's weird, you've put in a weird expression)",
    "general_docalculateerror_0": "Please enter an expression to calculate.",
    "manage_error_0": "Please enter all items.",
    "manage_error_1": "If you're not an administrator, you can't use it.",
    "manage_error_2": "I think you entered something wrong,,",
    "manage_error_3": "There was an error.. :( The report was automatically generated",
    "manage_error_4": "Sorry, please mention {0}",
    "manage_error_5": "There is an error in your subscription settings. Please fix it.",
    "manage_error_6": "I don't have permission and I'm talking about it",
    "manage_cfrm": "Yeah^^7",
    "manage_delwelcome_0": "Don't you just set it up and say it?",
    "manage_delwelcome_1": "There are no welcome greetings anymore.",
    "manage_delbye_0": "Don't you just set it up and talk about it?",
    "manage_delbye_1": "No goodbye anymore",
    "manage_unsubscribe_0": "I didn't even subscribe to it, so haha",
    "manage_unsubscribe_1": "Unsubscribed Hing ㅠㅠ",
    "manage_deldefaultrole_0": "The default role has not been set.",
    "manage_cleanchat_0": "I don't have permission, but I'm lol",
    "manage_cleanchat_1": "I need to tell you how much to clean it up or not",
    "manage_cleanchat_2": "What if you give me something that's not a number?",
    "manage_cleanchat_3": "Can you give me a normal number?",
    "manage_cleanchat_4": "Too many, not more than 200 ㅅㄱ",
    "manage_cleanchat_5": "Praise him for removing {0}",
    "manage_setmutterole_0": "Sorry, please mention the role.",
    "manage_setmutterole_1": "Sorry, please mention only 1 role.",
    "manage_setpunish_0": "There are up to 10 warnings.",
    "manage_setpunish_1": "At least 1 warning.",
    "manage_setpunish_2": "mute",
    "manage_setpunish_3": "kick",
    "manage_setpunish_4": "van",
    "manage_setpunish_5": "delete",
    "manage_setpunish_6": "You can only choose between mute, kick, ban, and delete.",
    "manage_setpunish_7": "The settings are not set.",
    "manage_setpunish_8": "Please enter all items.",
    "manage_setdefaultrole_0": "Sorry, please mention the role.",
    "manage_setdefaultrole_1": "Sorry, please mention only 1 role.",
    "manage_subscribe_0": "Sorry, please mention the channel.",
    "manage_subscribe_1": "Sorry, please mention only 1 channel.",
    "manage_delguildadmin_0": "{0} you are not my master anymore ㅋㅋㅋㅋㅋㅋㅋㅋ",
    "manage_delguildadmin_1": "Who are you?",
    "manage_delguildadmin_2": "Is this touching the server owner?",
    "manage_delguildadmin_3": "Is this touching my father?",
    "manage_addguildadmin_4": "Completed ^^7 Welcome {0} Master!",
    "manage_addguildadmin_5": "You are already the master.",
    "manage_guildadmin_0": "Sorry, please mention the target person.",
    "manage_guildadmin_1": "Sorry, please mention only 1 target.",
    "manage_execmute_0": "Sorry, please specify a role.",
    "manage_execmute_1": "Sorry, the role is incorrectly assigned.",
    "manage_execmute_2": "Sorry, you don't have enough privileges.",
    "manage_execmute_3": "You are already muted.",
    "manage_execmute_4": "Processing completed-Mute {0} / Reason: {1} / Processor: {2}",
    "manage_execkick_0": "There was a problem, please contact the administrator ㅠㅠ",
    "manage_execkick_1": "There was a problem, maybe it's never been muted...?",
    "manage_execkick_2": "Processing is complete-kick {0} / reason: {1} / handler: {2}",
    "manage_execban_0": "There was a problem, please contact the administrator ㅠㅠ",
    "manage_execban_1": "There was a problem, maybe it wasn't muted..?",
    "manage_execban_2": "Processing is complete-Ban {0} / Reason: {1} / Processor: {2}",
    "manage_warning_0": "Processing completed-Warning {0} cumulative warning count {1} / Reason: {2} / Processor: {3}",
    "manage_delwarning_0": "There are no warnings.",
    "manage_delwarning_1": "Yeah^^7 (cumulative warnings: {0})",
    "manage_getpunishlist_0": "Mute {1} seconds on warning {0} times",
    "manage_getpunishlist_1": "Kick on warning {0} instances",
    "manage_getpunishlist_2": "Warning {0} banned",
    "manage_getpunishlist_3": "No punishment policy",
    "manage_getpunishlist_4": "This is the server's punishment policy.",
    "manage_seewarning_0": "{0}'s current cumulative number of warnings is {1}.",
    "privatecmd_": "",
    "update_0": "Processing ended-mute {0} / handler: {1}",
    "update_1": "Process ended-mute {0}",
    "update_2": "There is an error in your subscription settings. Please fix it.",
    "events_0": "{0} has joined",
    "events_1": "The new member role is incorrectly assigned.",
    "events_2": "Insufficient permission to change new member role.",
    "events_3": "{0} has left",
    "private_": "",
}
