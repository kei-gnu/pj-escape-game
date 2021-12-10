
                    elif (find_obj == battery_box and "電池のないランプ" in play_player.item_have):
                        play_player.item_have += ["ランプ"]
                        play_player.item_have.remove("電池のないランプ")
                        find_obj.empty = 1
                        return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}\n"+f"{Color.YELLOW}ランプに電池を入れた{Color.RESET}"

                    else:
                        play_player.item_have += find_obj.item
                        #print(f"{get_item}を手に入れた")
                        find_obj.empty = 1
                        play_player.item_have.remove(find_obj.item_info)
                        return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}"


        else:#ただの箱
            get_item = find_obj.item[0]
            if find_obj == right_memo:
                get_item += f"({pas_right})"
            if find_obj == left_memo:
                get_item += f"({pas_left})"
            play_player.item_have += [get_item]
            #print(f"{get_item}を手に入れた")
            find_obj.empty = 1
            if (get_item == "電池のないランプ" and "電池" in play_player.item_have):
                play_player.item_have += ["ランプ"]
                play_player.item_have.remove("電池")
                find_obj.empty = 1
                return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}\n"+f"{Color.YELLOW}ランプに電池を入れた{Color.RESET}"
            if (get_item == "からのライター" and "ライターオイル" in play_player.item_have):
                play_player.item_have += ["ライター"]
                play_player.item_have.remove("ライターオイル")
                find_obj.empty = 1
                return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}\n"+f"{Color.YELLOW}ライターにオイルを入れた{Color.RESET}"
            #play_player.item_have.remove(find_obj.item_info)
            return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}"

    elif type(find_obj) == Door:#ドアだった場合
        if find_obj.door_num == 0:#ifアイテムが必要なドアである
            if find_obj.door_item_info in play_player.item_have:#ifそのアイテムを持っている
                if find_obj == door_5_pas:
                    try:
                        pas_5 = int(input(f"{Color.MAGENTA}パスワードを入力してください：{Color.RESET}"))
                        if pas_5 == pas_5_rand:
                            find_obj.op_cl = 0
                            for player in player_list:
                                player.item_have.remove(find_obj.door_item_info)
                            return f"{Color.YELLOW}扉が開いた{Color.RESET}"
                        else:
                            return f"{Color.RED}パスワードが間違っています{Color.RESET}"
                    except ValueError:
                        return f"{Color.RED}パスワードが間違っています{Color.RESET}"
                elif find_obj == door_6_pas:
                    try:
                        pas_6 = int(input(f"{Color.MAGENTA}パスワードを入力してください：{Color.RESET}"))
                        if pas_6 == pas_6_rand:
                            find_obj.op_cl = 0
                            for player in player_list:
                                player.item_have.remove(find_obj.door_item_info)
                            return f"{Color.YELLOW}扉が開いた{Color.RESET}"
                        else:
                            return f"{Color.RED}パスワードが間違っています{Color.RESET}"
                    except ValueError:
                        return f"{Color.RED}パスワードが間違っています{Color.RESET}"

                #elif find_obj == door_8_pas:
                #    pas_8 = int(input("パスワードを入力してください："))
                #    if pas_8 == pas_8_rand:
                #        find_obj.op_cl = 0
                #        return "扉が開いた"
                #    else:
                #        return "パスワードが間違っています"
                elif find_obj == door_lamp:
                    find_obj.op_cl = 0
                    return f"{Color.YELLOW}ランプをつけた{Color.RESET}"

                else:
                    find_obj.op_cl = 0
                    return f"{Color.YELLOW}扉が開いた{Color.RESET}"

            else:#アイテムを持ってない
                if find_obj == door_x_student:
                    return f"{Color.YELLOW}＊学生証がないと通れない{Color.RESET}"
                if find_obj == door_y_student:
                    return f"{Color.YELLOW}＊学生証がないと通れない{Color.RESET}"
                if find_obj == door_werehouse_key:
                    return f"{Color.YELLOW}＊鍵がかかっている{Color.RESET}"
                if find_obj == door_lamp:
                    return f"{Color.YELLOW}＊暗くては入れない{Color.RESET}"
                if find_obj == door_old_key:
                    return f"{Color.YELLOW}＊鍵がかかっている{Color.RESET}"
                if find_obj == door_5_pas:
                    return f"{Color.YELLOW}＊5ケタのパスワードが必要なようだ{Color.RESET}"
                if find_obj == door_6_pas:
                    return f"{Color.YELLOW}＊6ケタのパスワードが必要なようだ{Color.RESET}"
                #if find_obj == door_8_pas:
                #    return "＊8ケタのパスワードが必要なようだ"
        else:#開いてないスイッチドア
            return f"{Color.YELLOW}{find_obj.door_num}と書かれている{Color.RESET}"

    try:
        if find_obj == 1:
            pas_8 = int(input(f"{Color.MAGENTA}パスワードを入力してください：{Color.RESET}"))
            if pas_8 == pas_8_rand:
                return 1
            else:
                return f"{Color.RED}パスワードが間違っています{Color.RESET}"
        else:
            return ""
    except ValueError:
        return f"{Color.RED}パスワードが間違っています{Color.RESET}"

#マップ情報を取得し、整える
with open("./map_sqare.txt") as fb:
    map_info = fb.readlines()
    for num in range(len(map_info)):
        map_info[num] = map_info[num].strip("\n")
        map_info[num] = map_info[num].split(",")
        #map_info[num] = [int(s) for s in map_info[num]]
    init_map = copy.deepcopy(map_info)

"""
with open("./blind_sqare.txt") as fb:
    blind_sqare = fb.readlines()
    for num in range(len(blind_sqare)):
        blind_sqare[num] = blind_sqare[num].strip("\n")
        blind_sqare[num] = blind_sqare[num].split(",")
"""

#初期化
init(map_info, game_state=0)

#ルール表示
print_rule()

#時間の基準
start_time = time.time()

map_info = print_out(map_info)

#メインループ
while game_state == 0:
    open_num = []
    print_txt = ""
    game_state = check_game_over(start_time)
    if game_state == 1:
        print("game over!!!!!!!")
        break

    print(f"X君の持ち物：\n{player_x.item_have}")
    print(f"Y君の持ち物：\n{player_y.item_have}")


    print("------------------------------------------------")
    do = ""
    while do == "":
        do = input("move or action: ")#入力を待つ
    if do == " ":
        print_txt = action(map_info, play_player, goal_open)
        if print_txt == 1:
            goal_open = 1
            print_txt == "扉が開いた"
    elif do == "c":
        play_player = change_player(play_player)
    elif do == "r":
        print_rule()
    else:
"commit python code"
        move_player(map_info, do, play_player)
        open_door_list = [check_switch(player_x), check_switch(player_y)]
        open_num = check_door(open_door_list)
    map_info = print_out(map_info)
    if len(open_num) == 2:
        print(f"＊{open_num[0]}と{open_num[1]}のドアが開いている")
    if len(open_num) == 1:
        print(f"＊{open_num[0]}のドアが開いている")
    if print_txt != "":
        print(print_txt)
    print("------------------------------------------------")
    game_state = check_game_clear(player_x, player_y)
    if game_state == 2:
        print("game clear!!!!!!")

tomita%@apple.local ~/g3scond/project_ai2/pj-escape-game
→ :q!                                                                                         +main
zsh: command not found: :q!

tomita%@apple.local ~/g3scond/project_ai2/pj-escape-game
→ git checkout develop                                                                        +main
M	main.py
Switched to branch 'develop'

tomita%@apple.local ~/g3scond/project_ai2/pj-escape-game
→ ls                                                                                       +develop
README.md*     main.py*       map_sqare.txt*

tomita%@apple.local ~/g3scond/project_ai2/pj-escape-game
→ git status                                                                               +develop
On branch develop
Changes not staged for commit:
  (use "git add <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	modified:   main.py

no changes added to commit (use "git add" and/or "git commit -a")

tomita%@apple.local ~/g3scond/project_ai2/pj-escape-game
→ git commit -a -m "add code " .                                                           +develop
fatal: paths '. ...' with -a does not make sense

tomita%@apple.local ~/g3scond/project_ai2/pj-escape-game
→ git commit -a                                                                            +develop
[develop eaf32c7] "commit python code"
 1 file changed, 719 insertions(+)

tomita%@apple.local ~/g3scond/project_ai2/pj-escape-game
→ git log                                                                                   develop
commit eaf32c7faab91ba025c628e5e87baaa34c01e759 (HEAD -> develop)
Author: tomita <319012kei@users.noreply.github.com>
Date:   Fri Dec 10 13:29:18 2021 +0900

    "commit python code"

commit 164963d48a50c2b3d1b9f199a54b511d2021a28d (main)
Author: tomita <319012kei@users.noreply.github.com>
Date:   Fri Dec 10 13:27:49 2021 +0900

    commit game

commit 14ee7ebc70bf1989466060ec1bd28eb4a42b4840
Author: tomita <319012kei@users.noreply.github.com>
Date:   Fri Dec 10 13:24:54 2021 +0900

    commit map

commit 0704b64dc7da33ca9f46a1ea2a83890ae16e2c97 (origin/main, origin/HEAD)
Author: kei <61653118+kei-gnuy@users.noreply.github.com>
Date:   Fri Dec 10 13:22:37 2021 +0900

    Initial commit

tomita%@apple.local ~/g3scond/project_ai2/pj-escape-game
→ git checkout main                                                                         develop
Switched to branch 'main'
Your branch is ahead of 'origin/main' by 2 commits.
  (use "git push" to publish your local commits)

tomita%@apple.local ~/g3scond/project_ai2/pj-escape-game
→ ls                                                                                           main
README.md*     main.py*       map_sqare.txt*

tomita%@apple.local ~/g3scond/project_ai2/pj-escape-game
→ cat main.py                                                                                  main

tomita%@apple.local ~/g3scond/project_ai2/pj-escape-game
→ vi main.py                                                                                   main

tomita%@apple.local ~/g3scond/project_ai2/pj-escape-game
→ git checkout develop                                                                         main
Switched to branch 'develop'

tomita%@apple.local ~/g3scond/project_ai2/pj-escape-game
→ cat main.py                                                                               develop
import copy
import time
from random import randint

class Map:
    def __init__(self):
        pass

class Room:
    def __init__(self, left_up, right_down, open):#, box,wall,door,switch):
        self.left_up = left_up
        self.right_down = right_down
        self.open = open
        #self.box = box
        #self.wall = wall
        #self.door = door
        #self.switch = switch

class Box:
    def __init__(self,pos, item, item_info):
        self.item = item
        self.item_info = item_info
        self.pos = pos
        self.empty = 0

class Player:
    def __init__(self, x, y, player_cur,item_have):
        self.x = x
        self.y = y
        self.player_cur = player_cur
        self.item_have = item_have

class Door:
    def __init__(self, door_num, pos, op_cl, door_item_info):
        self.door_num = door_num
        self.pos = pos
        self.op_cl = op_cl
        self.door_item_info = door_item_info

class switch:
    def __init__(self, switch_num, on_off, pos):
        self.switch_num = switch_num
        self.on_off = on_off
        self.pos = pos

class Color:
	BLACK          = '\033[30m'#(文字)黒
	RED            = '\033[31m'#(文字)赤
	GREEN          = '\033[32m'#(文字)緑
	YELLOW         = '\033[33m'#(文字)黄
	BLUE           = '\033[34m'#(文字)青
	MAGENTA        = '\033[35m'#(文字)マゼンタ
	CYAN           = '\033[36m'#(文字)シアン
	WHITE          = '\033[37m'#(文字)白
	COLOR_DEFAULT  = '\033[39m'#文字色をデフォルトに戻す
	BOLD           = '\033[1m'#太字
	UNDERLINE      = '\033[4m'#下線
	INVISIBLE      = '\033[08m'#不可視
	REVERCE        = '\033[07m'#文字色と背景色を反転
	BG_BLACK       = '\033[40m'#(背景)黒
	BG_RED         = '\033[41m'#(背景)赤
	BG_GREEN       = '\033[42m'#(背景)緑
	BG_YELLOW      = '\033[43m'#(背景)黄
	BG_BLUE        = '\033[44m'#(背景)青
	BG_MAGENTA     = '\033[45m'#(背景)マゼンタ
	BG_CYAN        = '\033[46m'#(背景)シアン
	BG_WHITE       = '\033[47m'#(背景)白
	BG_DEFAULT     = '\033[49m'#背景色をデフォルトに戻す
	RESET          = '\033[0m'#全てリセット

color_list = [Color.WHITE, Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE, Color.MAGENTA, Color.CYAN, Color.RESET]

#パスワード
pas_4_rand = randint(1000,9999)
pas_5_rand = randint(10000,99999)
pas_6_rand = randint(100000,999999)
pas_right = randint(1000,9999)
pas_left = randint(1000,9999)
pas_8_rand = int(str(pas_left) + str(pas_right))


#ゲーム終了かどうかの状態
#0で続行、1で終了
game_state = 0

#上下左右
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

#プレイヤーXとYのインスタンス
player_x = Player(22, 1, 0, [])
player_y = Player(22, 22, 0, [])

#プレイヤーのリスト
player_list = [player_x, player_y]

#操作しているプレイヤー
play_player = player_x

box_list = []

#箱インスタンス、引数は場所、入っているアイテム、開けるのに必要なアイテム(0は必要なし)
#1:電池
battery_box = Box((20, 1), ["電池"], "カッター")
box_list.append(battery_box)
#2：学生証
StudenCard_box = Box((19, 3), ["学生証"], "ドライバー")
box_list.append(StudenCard_box)
#3:ランプ
lamp_box = Box((16, 1), ["電池のないランプ"], 0)
box_list.append(lamp_box)
#4:古びた鍵
old_key_box = Box((13, 1), ["古びた鍵"], "椅子")
box_list.append(old_key_box)
#5:メモの右端
right_memo = Box((8, 1), ["メモの右端"], 0)
box_list.append(right_memo)
#6:椅子
chair = Box((2, 2), ["椅子"], 0)
box_list.append(chair)
#7:＋ドライバ
screw_driver_box = Box((22, 9), ["ドライバー"], 0)
box_list.append(screw_driver_box)
#8:6桁パスワード
passward_6_box = Box((10, 10), [f"6桁のパスワード({pas_6_rand})"], "ペンチ")
box_list.append(passward_6_box)
#9:鍵カッター
key_cutter_box = Box((7, 10), ["倉庫の鍵", "カッター"], f"4桁のパスワード({pas_4_rand})")
box_list.append(key_cutter_box)
#10:ペンチ
pliers_box = Box((4, 7), ["ペンチ"], 0)
box_list.append(pliers_box)
#11:200円
coin_200_box = Box((22, 13), ["200円"], 0)
box_list.append(coin_200_box)
#12:4桁パスワード
passward_4_box = Box((10, 20), [f"4桁のパスワード({pas_4_rand})"], "ライター")#(19, 14)
box_list.append(passward_4_box)
#13:5桁パスワード
projector_box = Box((16, 15), [f"5桁のパスワード({pas_5_rand})"], "電源コード")
box_list.append(projector_box)
#14:メモの左端
left_memo = Box((8, 14), ["メモの左端"], 0)
box_list.append(left_memo)
#15:学生証
StudenCard_jihan = Box((20, 22), ["学生証", "100円"], "200円")
box_list.append(StudenCard_jihan)
#16:ライター
righter_box = Box((14, 21), ["からのライター"], 0)
box_list.append(righter_box)
#17:ライターオイル
righter_oil_box = Box((19, 14), ["ライターオイル"], "100円")#(10, 20)
box_list.append(righter_oil_box)
#18:電源コード
code_box =Box((1, 20), ["電源コード"], 0)
box_list.append(code_box)

#ドアリスト
door_list = []

#ドアインスタンス、引数はスイッチとの番号(アイテムが必要な場合は0)、位置、開いてるかどうか(開いてる場合は0閉まっている場合は1)、開けるのに必要なアイテム(ない場場合は0))
door_1 = Door(1, [(11, 8), (12, 8)], 1, 0)
door_list.append(door_1)

door_2 = Door(2, [(20, 5), (20, 6)], 1, 0)
door_list.append(door_2)

door_3 = Door(3, [(21, 17), (21, 18)], 1, 0)
door_list.append(door_3)

door_4 = Door(4, [(5, 21), (6, 21)], 1, 0)
door_list.append(door_4)

door_5 = Door(5, [(5, 2), (6, 2)], 1, 0)
door_list.append(door_5)

door_6 = Door(6, [(5, 15), (6, 15)], 1, 0)
door_list.append(door_6)

#door_8_pas = Door(0, [0, 14], 1, "8桁のパスワード")
#door_list.append(door_8_pas)

door_werehouse_key = Door(0, [(14, 5), (14, 6)], 1, "倉庫の鍵")
door_list.append(door_werehouse_key)

door_old_key = Door(0, [(2, 5), (2, 6)], 1, "古びた鍵")
door_list.append(door_old_key)

door_lamp = Door(0, [(8, 5), (8, 6)], 1, "ランプ")
door_list.append(door_lamp)

door_5_pas = Door(0, [(9, 17), (9, 18)], 1, f"5桁のパスワード({pas_5_rand})")
door_list.append(door_5_pas)

door_6_pas = Door(0, [(2, 11), (2, 12)], 1, f"6桁のパスワード({pas_6_rand})")
door_list.append(door_6_pas)

door_x_student = Door(0, [(17, 8), (18, 8)], 1, "学生証")
door_list.append(door_x_student)

door_y_student = Door(0, [(17, 21), (18, 21)], 1, "学生証")
door_list.append(door_y_student)

switch_list = []

#スイッチインスタンス、引数は番号、オンオフ、位置
switch_1 = switch(1, 0, (9, 22))
switch_list.append(switch_1)

switch_2 = switch(2, 0, (22, 20))
switch_list.append(switch_2)

switch_3 = switch(3, 0, (15, 10))
switch_list.append(switch_3)

switch_4 = switch(4, 0, (10, 1))
switch_list.append(switch_4)

switch_5 = switch(5, 0, (10, 13))
switch_list.append(switch_5)

switch_6 = switch(6, 0, (4, 13))
switch_list.append(switch_6)

room_list = []

room1_1 = Room([0, 18], [5, 23], 1)
room_list.append(room1_1)
room1_2 = Room([0, 12], [5, 17], 0)
room_list.append(room1_2)
room1_3 = Room([0, 6], [5, 11], 0)
room_list.append(room1_3)
room1_4 = Room([0, 0], [5, 5], 0)
room_list.append(room1_4)
room2_1 = Room([6, 18], [11, 23], 0)
room_list.append(room2_1)
room2_2 = Room([6, 12], [11, 17], 0)
room_list.append(room2_2)
room2_3 = Room([6, 6], [11, 11], 0)
room_list.append(room2_3)
room2_4 = Room([6, 0], [11, 5], 0)
room_list.append(room2_4)
room3_1 = Room([12, 18], [17, 23], 0)
room_list.append(room3_1)
room3_2 = Room([12, 12], [17, 17], 0)
room_list.append(room3_2)
room3_3 = Room([12, 6], [17, 11], 0)
room_list.append(room3_3)
room3_4 = Room([12, 0], [17, 5], 0)
room_list.append(room3_4)
room4_1 = Room([18, 18], [23, 23], 1)
room_list.append(room4_1)
room4_2 = Room([18, 12], [23, 17], 0)
room_list.append(room4_2)
room4_3 = Room([18, 6], [23, 11], 0)
room_list.append(room4_3)
room4_4 = Room([18, 0], [23, 5], 0)
room_list.append(room4_4)

goal_pos = (0, 14)
goal_open = 0


#初期化関数
def init(map, game_state):
    pass

#画面出力
def print_out(map):
    map = copy.deepcopy(init_map)
    print_map = copy.deepcopy(init_map)
    #箱リストから出力
    for box in box_list:
        if box.empty == 1:
            continue
        x, y = box.pos
        map[x][y] = "5"
        print_map[x][y] = "☆"
    #ドアリストから出力
    for door in door_list:
        if door.op_cl == 1:
            for x, y in door.pos:
                map[x][y] = "3"
                print_map[x][y] = f"{color_list[door.door_num]}□{color_list[-1]} "
        #ドアが開いてるなら出力しない
        if door.op_cl == 0:
            for x, y in door.pos:
                map[x][y] = "0"

    #スイッチリストから出力
    for switch in switch_list:
        x, y = switch.pos
        map[x][y] = "4"
        print_map[x][y] = f"{color_list[switch.switch_num]}○{color_list[-1]} "

    #プレイヤーリストから出力
    for player in player_list:
        if player == player_x:
            x1, y1 = player.x, player.y
            map[x1][y1] = "2"
            print_map[x1][y1] = f"{Color.RED}♥{Color.RESET} "
        else:
            x2, y2 = player.x, player.y
            map[x2][y2] = "6"
            print_map[x2][y2] = f"{Color.BLUE}♥{Color.RESET} "

    if goal_open == 0:
        map[goal_pos[0]][goal_pos[1]] = "3"#ゴール
        map[goal_pos[0]][goal_pos[1]] = "□"

    blind_map = copy.deepcopy(map)
    #for room in room_list:
        #if room.open == 0:
            #blind_map[room.left_up[0]:room.left_up[1]][room.right_down[0]:room.right_down[1]] = blind_sqare
    print("------------------------------------------------")
    for mapline in print_map:
        mapline = [" " if i == "0" else i for i in mapline]
        mapline = [f"{Color.WHITE}■ " if i == "1" else i for i in mapline]
        #mapline = ["♥" if i == "2" else i for i in mapline]
        #for switch in switch_list:
        #    switch.switch_num ==
        #mapline = ["□" if i == "3" else i for i in mapline]
        #mapline = ["○" if i == "4" else i for i in mapline]
        #mapline = ["☆" if i == "5" else i for i in mapline]
        #mapline = ["♡" if i == "6" else i for i in mapline]
        """
        mapline = "".join(mapline)
        mapline = mapline.replace("0", " ")
        mapline = mapline.replace("1", "■")
        mapline = mapline.replace("2", "♥")
        mapline = mapline.replace("3", "□")
        mapline = mapline.replace("4", f"{Color.RED}○{Color.RESET}")
        mapline = mapline.replace("5", "☆")
        mapline = mapline.replace("6", "♡")
        """
        fom = "{:<2}"*len(mapline)
        print(fom.format(*mapline))
    print("------------------------------------------------")
    return map

#ゲーム終了判定
def check_game_over(start_time):
    now = time.time()
    limit = now - start_time
    print(f"爆発まであと{900-round(limit)}秒")
    if limit >= 900:
        return 1

#ゲーム勝利判定
def check_game_clear(player_x, player_y):
    if player_x.x == 0 and player_x.y == 14 and player_y.x == 0 and player_y.y == 14:
        return 2
    return 0

#プレイヤーの切り替え
def change_player(play_player):
    if play_player == player_x:
        print("change to Y")
        return player_y
    else:
        print("change to X")
        return player_x

#ルールの表示
def print_rule():
    print(f"{Color.GREEN}～ストーリー～{Color.RESET}")
    print("爆弾の仕掛けられた東京工科大学にX君とY君が閉じ込められてしまった！爆弾が爆発する前に二人一緒に脱出しよう！")
    print("------------------------------------------------")
    print(f"{Color.GREEN}～ルール～{Color.RESET}")
    print("・部屋にある複数のギミックやアイテムを使ってゴールを目指そう！")
    print("・あなたはX君、Y君の二人を操作することができるよ.最初はX君から動かせるよ！")
    print("・X君とY君は一人ずつしか操作できないんだ...X君とY君を切り替えながら進もう！")
    #print("・ドア、スイッチ保留")
    print("・対応するスイッチを踏んでいる間だけドアが開くよ")
    print("・アイテムは一回使ったらなくなっちゃうよ")
    print("・X君とY君は電話を持っているから情報は共有出来るよ.でもアイテムは共有出来ないよ")
    print("・爆発までの制限時間は900秒だ！")
    print("------------------------------------------------")
    print(f"{Color.GREEN}～マップの表示と操作方法～{Color.RESET}")
    print("X君…♥　Y君…♡　アイテム…☆　スイッチ…〇　ドア…□")
    print("上…'w'　下…'s'　左…'a'　右…'d'")
    print("X君とY君の切り替え…'c'")
    print(f"アイテムや{Color.RED}{Color.BOLD}{Color.UNDERLINE}ドア{Color.RESET}を調べる…'space'")
    print("ルールを表示…'r'")
    s = input("Enterでスタート！：")

#壁と箱の衝突判定
def check_cpllide(map, x, y):
    print(map[x][y])
    if map[x][y] == "1" or map[x][y] == "3" or map[x][y] == "5":
        print("これ以上進めない")
        return True
    return False

#プレイヤーの移動
def move_player(map, direction, play_player):

    #操作しているプレイヤーの判定
    if play_player == player_x:
        move_player = player_x
    else:
        move_player = player_y

    #移動
    if direction == "a":
        move_player.y += -1
        if check_cpllide(map, move_player.x, move_player.y):
            move_player.y += 1
    elif direction == "w":
        move_player.x += -1
        if check_cpllide(map, move_player.x, move_player.y):
            move_player.x += 1
    elif direction == "s":
        move_player.x += 1
        if check_cpllide(map, move_player.x, move_player.y):
            move_player.x += -1
    elif direction == "d":
        move_player.y += 1
        if check_cpllide(map, move_player.x, move_player.y):
            move_player.y += -1

#ドアを開け閉め
def check_door(open_num):
    open_list = []
    for door in door_list:
        if door.door_num in open_num:
            door.op_cl = 0
            open_list.append(door.door_num)
        elif door.door_num != 0:
            door.op_cl = 1
    return open_list

#ドアを閉める
def close_door():
    pass

#スイッチを踏んでいるかの判定
def check_switch(player):
    for switch in switch_list:
        if (player.x, player.y) == switch.pos:
            #print(f"{switch.switch_num}のドアが開いた")
            return switch.switch_num

    return -1

#アクションを行う
def action(map, play_player, goal_open):
    find_obj = 0
    for dir in directions:#上下左右を調べる
        checkx = play_player.x + dir[0]
        checky = play_player.y + dir[1]
        if map[checkx][checky] == "3" or map[checkx][checky] == "5":#if箱かドアだったら
            for box in box_list:#箱リストから探して見つけたらbreak
                if box.pos == (checkx, checky):
                    find_obj = box
                    break
            for door in door_list:
                if door.pos[0] == (checkx, checky) or door.pos[1] == (checkx, checky):
                    find_obj = door
                    break
            if (checkx, checky) == goal_pos:
                find_obj = 1

    if type(find_obj) == Box:#見付けたのが箱だった場合
        if find_obj.item_info != 0:#ifただの箱でない
            if find_obj.item_info not in play_player.item_have:#必要なアイテムを持っていない
                if find_obj == battery_box:
                    #print("＊ガムテープででグルグル巻きになっている")
                    return f"{Color.YELLOW}＊ガムテープでグルグル巻きになっている{Color.RESET}"
                if find_obj == StudenCard_jihan:
                    #print("＊100円で僕の学生証が売ってる！！")
                    return f"{Color.YELLOW}＊100円で僕の学生証が売ってる！！{Color.RESET}"
                if find_obj == passward_4_box:
                    #print("＊掲示板に何も書かれてない紙が貼ってある")
                    return f"{Color.YELLOW}＊掲示板に何も書かれてない紙が貼ってある{Color.RESET}"
                if find_obj == projector_box:
                    #print("＊電源コードのないプロジェクタだ")
                    return f"{Color.YELLOW}＊電源コードのないプロジェクタだ{Color.RESET}"
                if find_obj == StudenCard_box:
                    #print("＊＋ドライバーでねじ留めされている")
                    return f"{Color.YELLOW}＊＋ドライバーでねじ留めされている{Color.RESET}"
                if find_obj == old_key_box:
                    #print("＊ロッカーの上に何かあるけど手が届かない")
                    return f"{Color.YELLOW}＊ロッカーの上に何かあるけど手が届かない{Color.RESET}"
                if find_obj == passward_6_box:
                    #print("＊金具で留められている")
                    return f"{Color.YELLOW}＊金具で留められている{Color.RESET}"
                if find_obj == key_cutter_box:
                    #print("＊4ケタのパスワードが必要なようだ")
                    return f"{Color.YELLOW}＊4ケタのパスワードが必要なようだ{Color.RESET}"
                if find_obj == righter_oil_box:
                    #print("＊ードライバーでねじ留めされている")
                    return f"{Color.YELLOW}＊ードライバーでねじ留めされている{Color.RESET}"
            else:#アイテムを持ってた
                #play_player.item_have.remove(find_obj.item_info)
                #print("箱を開いた")#自販機や掲示板のテキスト分けが必要
                get_item = find_obj.item[0]
                if len(find_obj.item) == 2:#手に入るのが二個以上だった場合
                    get_item = f"{find_obj.item[0]}と{find_obj.item[1]}"
                if find_obj == passward_4_box or find_obj == projector_box or find_obj == passward_6_box:#パスワードだった場合、相方にもアイテムを渡す
                    #print(f"{get_item}を手に入れた")
                    find_obj.empty = 1
                    if find_obj == passward_4_box:
                        for player in player_list:
                            player.item_have += [get_item]
                        return f"{Color.YELLOW}紙をあぶったら数字が浮き出た\n{get_item}を手に入れた{Color.RESET}"

                    if find_obj == projector_box:
                        for player in player_list:
                            player.item_have += [get_item]
                        return f"{Color.YELLOW}プロジェクタから数字が映し出された\n{get_item}を手に入れた{Color.RESET}"

                    if find_obj == passward_6_box:
                        for player in player_list:
                            player.item_have += [get_item]
                        return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}"

                elif find_obj == key_cutter_box:
                    try:
                        pas_4 = int(input(f"{Color.MAGENTA}パスワードを入力してください：{Color.RESET}"))
                        if pas_4 == pas_4_rand:
                            play_player.item_have += find_obj.item
                            #print(f"{get_item}を手に入れた")
                            for player in player_list:
                                player.item_have.remove(find_obj.item_info)
                            find_obj.empty = 1
                            return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}"
                        else:
                            #print("パスワードが間違っています")
                            return f"{Color.RED}パスワードが間違っています{Color.RESET}"
                    except ValueError:
                        return f"{Color.RED}パスワードが間違っています{Color.RESET}"

                else:
                    if (find_obj == righter_oil_box and "からのライター" in play_player.item_have):
                        play_player.item_have += ["ライター"]
                        play_player.item_have.remove("からのライター")
                        find_obj.empty = 1
                        return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}\n"+f"{Color.YELLOW}ライターにオイルを入れた{Color.RESET}"

                    elif (find_obj == battery_box and "電池のないランプ" in play_player.item_have):
                        play_player.item_have += ["ランプ"]
                        play_player.item_have.remove("電池のないランプ")
                        find_obj.empty = 1
                        return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}\n"+f"{Color.YELLOW}ランプに電池を入れた{Color.RESET}"

                    else:
                        play_player.item_have += find_obj.item
                        #print(f"{get_item}を手に入れた")
                        find_obj.empty = 1
                        play_player.item_have.remove(find_obj.item_info)
                        return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}"


        else:#ただの箱
            get_item = find_obj.item[0]
            if find_obj == right_memo:
                get_item += f"({pas_right})"
            if find_obj == left_memo:
                get_item += f"({pas_left})"
            play_player.item_have += [get_item]
            #print(f"{get_item}を手に入れた")
            find_obj.empty = 1
            if (get_item == "電池のないランプ" and "電池" in play_player.item_have):
                play_player.item_have += ["ランプ"]
                play_player.item_have.remove("電池")
                find_obj.empty = 1
                return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}\n"+f"{Color.YELLOW}ランプに電池を入れた{Color.RESET}"
            if (get_item == "からのライター" and "ライターオイル" in play_player.item_have):
                play_player.item_have += ["ライター"]
                play_player.item_have.remove("ライターオイル")
                find_obj.empty = 1
                return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}\n"+f"{Color.YELLOW}ライターにオイルを入れた{Color.RESET}"
            #play_player.item_have.remove(find_obj.item_info)
            return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}"

    elif type(find_obj) == Door:#ドアだった場合
        if find_obj.door_num == 0:#ifアイテムが必要なドアである
            if find_obj.door_item_info in play_player.item_have:#ifそのアイテムを持っている
                if find_obj == door_5_pas:
                    try:
                        pas_5 = int(input(f"{Color.MAGENTA}パスワードを入力してください：{Color.RESET}"))
                        if pas_5 == pas_5_rand:
                            find_obj.op_cl = 0
                            for player in player_list:
                                player.item_have.remove(find_obj.door_item_info)
                            return f"{Color.YELLOW}扉が開いた{Color.RESET}"
                        else:
                            return f"{Color.RED}パスワードが間違っています{Color.RESET}"
                    except ValueError:
                        return f"{Color.RED}パスワードが間違っています{Color.RESET}"
                elif find_obj == door_6_pas:
                    try:
                        pas_6 = int(input(f"{Color.MAGENTA}パスワードを入力してください：{Color.RESET}"))
                        if pas_6 == pas_6_rand:
                            find_obj.op_cl = 0
                            for player in player_list:
                                player.item_have.remove(find_obj.door_item_info)
                            return f"{Color.YELLOW}扉が開いた{Color.RESET}"
                        else:
                            return f"{Color.RED}パスワードが間違っています{Color.RESET}"
                    except ValueError:
                        return f"{Color.RED}パスワードが間違っています{Color.RESET}"

                #elif find_obj == door_8_pas:
                #    pas_8 = int(input("パスワードを入力してください："))
                #    if pas_8 == pas_8_rand:
                #        find_obj.op_cl = 0
                #        return "扉が開いた"
                #    else:
                #        return "パスワードが間違っています"
                elif find_obj == door_lamp:
                    find_obj.op_cl = 0
                    return f"{Color.YELLOW}ランプをつけた{Color.RESET}"

                else:
                    find_obj.op_cl = 0
                    return f"{Color.YELLOW}扉が開いた{Color.RESET}"

            else:#アイテムを持ってない
                if find_obj == door_x_student:
                    return f"{Color.YELLOW}＊学生証がないと通れない{Color.RESET}"
                if find_obj == door_y_student:
                    return f"{Color.YELLOW}＊学生証がないと通れない{Color.RESET}"
                if find_obj == door_werehouse_key:
                    return f"{Color.YELLOW}＊鍵がかかっている{Color.RESET}"
                if find_obj == door_lamp:
                    return f"{Color.YELLOW}＊暗くては入れない{Color.RESET}"
                if find_obj == door_old_key:
                    return f"{Color.YELLOW}＊鍵がかかっている{Color.RESET}"
                if find_obj == door_5_pas:
                    return f"{Color.YELLOW}＊5ケタのパスワードが必要なようだ{Color.RESET}"
                if find_obj == door_6_pas:
                    return f"{Color.YELLOW}＊6ケタのパスワードが必要なようだ{Color.RESET}"
                #if find_obj == door_8_pas:
                #    return "＊8ケタのパスワードが必要なようだ"
        else:#開いてないスイッチドア
            return f"{Color.YELLOW}{find_obj.door_num}と書かれている{Color.RESET}"

    try:
        if find_obj == 1:
            pas_8 = int(input(f"{Color.MAGENTA}パスワードを入力してください：{Color.RESET}"))
            if pas_8 == pas_8_rand:
                return 1
            else:
                return f"{Color.RED}パスワードが間違っています{Color.RESET}"
        else:
            return ""
    except ValueError:
        return f"{Color.RED}パスワードが間違っています{Color.RESET}"

#マップ情報を取得し、整える
with open("./map_sqare.txt") as fb:
    map_info = fb.readlines()
    for num in range(len(map_info)):
        map_info[num] = map_info[num].strip("\n")
        map_info[num] = map_info[num].split(",")
        #map_info[num] = [int(s) for s in map_info[num]]
    init_map = copy.deepcopy(map_info)

"""
with open("./blind_sqare.txt") as fb:
    blind_sqare = fb.readlines()
    for num in range(len(blind_sqare)):
        blind_sqare[num] = blind_sqare[num].strip("\n")
        blind_sqare[num] = blind_sqare[num].split(",")
"""

#初期化
init(map_info, game_state=0)

#ルール表示
print_rule()

#時間の基準
start_time = time.time()

map_info = print_out(map_info)

#メインループ
while game_state == 0:
    open_num = []
    print_txt = ""
    game_state = check_game_over(start_time)
    if game_state == 1:
        print("game over!!!!!!!")
        break

    print(f"X君の持ち物：\n{player_x.item_have}")
    print(f"Y君の持ち物：\n{player_y.item_have}")


    print("------------------------------------------------")
import copy
import time
from random import randint

class Map:
    def __init__(self):
        pass

class Room:
    def __init__(self, left_up, right_down, open):#, box,wall,door,switch):
        self.left_up = left_up
        self.right_down = right_down
        self.open = open
        #self.box = box
        #self.wall = wall
        #self.door = door
        #self.switch = switch

class Box:
    def __init__(self,pos, item, item_info):
        self.item = item
        self.item_info = item_info
        self.pos = pos
        self.empty = 0

class Player:
    def __init__(self, x, y, player_cur,item_have):
        self.x = x
        self.y = y
        self.player_cur = player_cur
        self.item_have = item_have

class Door:
    def __init__(self, door_num, pos, op_cl, door_item_info):
        self.door_num = door_num
        self.pos = pos
        self.op_cl = op_cl
        self.door_item_info = door_item_info

class switch:
    def __init__(self, switch_num, on_off, pos):
        self.switch_num = switch_num
        self.on_off = on_off
        self.pos = pos
"main.py" 719L, 29409Bimport copy
import time
from random import randint

class Map:
    def __init__(self):
        pass

class Room:
    def __init__(self, left_up, right_down, open):#, box,wall,door,switch):
        self.left_up = left_up
        self.right_down = right_down
        self.open = open
        #self.box = box
        #self.wall = wall
        #self.door = door
        #self.switch = switch

class Box:
    def __init__(self,pos, item, item_info):
        self.item = item
        self.item_info = item_info
        self.pos = pos
        self.empty = 0

class Player:
    def __init__(self, x, y, player_cur,item_have):
        self.x = x
        self.y = y
        self.player_cur = player_cur
        self.item_have = item_have

class Door:
    def __init__(self, door_num, pos, op_cl, door_item_info):
        self.door_num = door_num
        self.pos = pos
        self.op_cl = op_cl
        self.door_item_info = door_item_info

class switch:
    def __init__(self, switch_num, on_off, pos):
        self.switch_num = switch_num
        self.on_off = on_off
        self.pos = pos

class Color:
	BLACK          = '\033[30m'#(文字)黒
	RED            = '\033[31m'#(文字)赤
	GREEN          = '\033[32m'#(文字)緑
	YELLOW         = '\033[33m'#(文字)黄
	BLUE           = '\033[34m'#(文字)青
	MAGENTA        = '\033[35m'#(文字)マゼンタ
	CYAN           = '\033[36m'#(文字)シアン
	WHITE          = '\033[37m'#(文字)白
	COLOR_DEFAULT  = '\033[39m'#文字色をデフォルトに戻す
	BOLD           = '\033[1m'#太字
	UNDERLINE      = '\033[4m'#下線
	INVISIBLE      = '\033[08m'#不可視
	REVERCE        = '\033[07m'#文字色と背景色を反転
	BG_BLACK       = '\033[40m'#(背景)黒
	BG_RED         = '\033[41m'#(背景)赤
	BG_GREEN       = '\033[42m'#(背景)緑
	BG_YELLOW      = '\033[43m'#(背景)黄
	BG_BLUE        = '\033[44m'#(背景)青
	BG_MAGENTA     = '\033[45m'#(背景)マゼンタ
	BG_CYAN        = '\033[46m'#(背景)シアン
	BG_WHITE       = '\033[47m'#(背景)白
	BG_DEFAULT     = '\033[49m'#背景色をデフォルトに戻す
	RESET          = '\033[0m'#全てリセット

color_list = [Color.WHITE, Color.RED, Color.GREEN, Color.YELLOW, Color.BLUE, Color.MAGENTA, Color.CYAN, Color.RESET]

#パスワード
pas_4_rand = randint(1000,9999)
pas_5_rand = randint(10000,99999)
pas_6_rand = randint(100000,999999)
pas_right = randint(1000,9999)
pas_left = randint(1000,9999)
pas_8_rand = int(str(pas_left) + str(pas_right))


#ゲーム終了かどうかの状態
#0で続行、1で終了
game_state = 0

#上下左右
directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

#プレイヤーXとYのインスタンス
player_x = Player(22, 1, 0, [])
player_y = Player(22, 22, 0, [])

#プレイヤーのリスト
player_list = [player_x, player_y]

#操作しているプレイヤー
play_player = player_x

box_list = []

#箱インスタンス、引数は場所、入っているアイテム、開けるのに必要なアイテム(0は必要なし)
#1:電池
battery_box = Box((20, 1), ["電池"], "カッター")
box_list.append(battery_box)
#2：学生証
StudenCard_box = Box((19, 3), ["学生証"], "ドライバー")
box_list.append(StudenCard_box)
#3:ランプ
lamp_box = Box((16, 1), ["電池のないランプ"], 0)
box_list.append(lamp_box)
#4:古びた鍵
old_key_box = Box((13, 1), ["古びた鍵"], "椅子")
box_list.append(old_key_box)
#5:メモの右端
right_memo = Box((8, 1), ["メモの右端"], 0)
box_list.append(right_memo)
#6:椅子
chair = Box((2, 2), ["椅子"], 0)
box_list.append(chair)
#7:＋ドライバ
screw_driver_box = Box((22, 9), ["ドライバー"], 0)
box_list.append(screw_driver_box)
#8:6桁パスワード
passward_6_box = Box((10, 10), [f"6桁のパスワード({pas_6_rand})"], "ペンチ")
box_list.append(passward_6_box)
#9:鍵カッター
key_cutter_box = Box((7, 10), ["倉庫の鍵", "カッター"], f"4桁のパスワード({pas_4_rand})")
box_list.append(key_cutter_box)
#10:ペンチ
pliers_box = Box((4, 7), ["ペンチ"], 0)
box_list.append(pliers_box)
#11:200円
coin_200_box = Box((22, 13), ["200円"], 0)
box_list.append(coin_200_box)
#12:4桁パスワード
passward_4_box = Box((10, 20), [f"4桁のパスワード({pas_4_rand})"], "ライター")#(19, 14)
box_list.append(passward_4_box)
#13:5桁パスワード
projector_box = Box((16, 15), [f"5桁のパスワード({pas_5_rand})"], "電源コード")
box_list.append(projector_box)
#14:メモの左端
left_memo = Box((8, 14), ["メモの左端"], 0)
box_list.append(left_memo)
#15:学生証
StudenCard_jihan = Box((20, 22), ["学生証", "100円"], "200円")
box_list.append(StudenCard_jihan)
#16:ライター
righter_box = Box((14, 21), ["からのライター"], 0)
box_list.append(righter_box)
#17:ライターオイル
righter_oil_box = Box((19, 14), ["ライターオイル"], "100円")#(10, 20)
box_list.append(righter_oil_box)
#18:電源コード
code_box =Box((1, 20), ["電源コード"], 0)
box_list.append(code_box)

#ドアリスト
door_list = []

#ドアインスタンス、引数はスイッチとの番号(アイテムが必要な場合は0)、位置、開いてるかどうか(開いてる場合は0閉まっている場合は1)、開けるのに必要なアイテム(ない場場合は0))
door_1 = Door(1, [(11, 8), (12, 8)], 1, 0)
door_list.append(door_1)

door_2 = Door(2, [(20, 5), (20, 6)], 1, 0)
door_list.append(door_2)

door_3 = Door(3, [(21, 17), (21, 18)], 1, 0)
door_list.append(door_3)

door_4 = Door(4, [(5, 21), (6, 21)], 1, 0)
door_list.append(door_4)

door_5 = Door(5, [(5, 2), (6, 2)], 1, 0)
door_list.append(door_5)

door_6 = Door(6, [(5, 15), (6, 15)], 1, 0)
door_list.append(door_6)

#door_8_pas = Door(0, [0, 14], 1, "8桁のパスワード")
#door_list.append(door_8_pas)

door_werehouse_key = Door(0, [(14, 5), (14, 6)], 1, "倉庫の鍵")
door_list.append(door_werehouse_key)

door_old_key = Door(0, [(2, 5), (2, 6)], 1, "古びた鍵")
door_list.append(door_old_key)

door_lamp = Door(0, [(8, 5), (8, 6)], 1, "ランプ")
door_list.append(door_lamp)

door_5_pas = Door(0, [(9, 17), (9, 18)], 1, f"5桁のパスワード({pas_5_rand})")
door_list.append(door_5_pas)

door_6_pas = Door(0, [(2, 11), (2, 12)], 1, f"6桁のパスワード({pas_6_rand})")
door_list.append(door_6_pas)

door_x_student = Door(0, [(17, 8), (18, 8)], 1, "学生証")
door_list.append(door_x_student)

door_y_student = Door(0, [(17, 21), (18, 21)], 1, "学生証")
door_list.append(door_y_student)

switch_list = []

#スイッチインスタンス、引数は番号、オンオフ、位置
switch_1 = switch(1, 0, (9, 22))
switch_list.append(switch_1)

switch_2 = switch(2, 0, (22, 20))
switch_list.append(switch_2)

switch_3 = switch(3, 0, (15, 10))
switch_list.append(switch_3)

switch_4 = switch(4, 0, (10, 1))
switch_list.append(switch_4)

switch_5 = switch(5, 0, (10, 13))
switch_list.append(switch_5)

switch_6 = switch(6, 0, (4, 13))
switch_list.append(switch_6)

room_list = []

room1_1 = Room([0, 18], [5, 23], 1)
room_list.append(room1_1)
room1_2 = Room([0, 12], [5, 17], 0)
room_list.append(room1_2)
room1_3 = Room([0, 6], [5, 11], 0)
room_list.append(room1_3)
room1_4 = Room([0, 0], [5, 5], 0)
room_list.append(room1_4)
room2_1 = Room([6, 18], [11, 23], 0)
room_list.append(room2_1)
room2_2 = Room([6, 12], [11, 17], 0)
room_list.append(room2_2)
room2_3 = Room([6, 6], [11, 11], 0)
room_list.append(room2_3)
room2_4 = Room([6, 0], [11, 5], 0)
room_list.append(room2_4)
room3_1 = Room([12, 18], [17, 23], 0)
room_list.append(room3_1)
room3_2 = Room([12, 12], [17, 17], 0)
room_list.append(room3_2)
room3_3 = Room([12, 6], [17, 11], 0)
room_list.append(room3_3)
room3_4 = Room([12, 0], [17, 5], 0)
room_list.append(room3_4)
room4_1 = Room([18, 18], [23, 23], 1)
room_list.append(room4_1)
room4_2 = Room([18, 12], [23, 17], 0)
room_list.append(room4_2)
room4_3 = Room([18, 6], [23, 11], 0)
room_list.append(room4_3)
room4_4 = Room([18, 0], [23, 5], 0)
room_list.append(room4_4)

goal_pos = (0, 14)
goal_open = 0


#初期化関数
def init(map, game_state):
    pass

#画面出力
def print_out(map):
    map = copy.deepcopy(init_map)
    print_map = copy.deepcopy(init_map)
    #箱リストから出力
    for box in box_list:
        if box.empty == 1:
            continue
        x, y = box.pos
        map[x][y] = "5"
        print_map[x][y] = "☆"
    #ドアリストから出力
    for door in door_list:
        if door.op_cl == 1:
            for x, y in door.pos:
                map[x][y] = "3"
                print_map[x][y] = f"{color_list[door.door_num]}□{color_list[-1]} "
        #ドアが開いてるなら出力しない
        if door.op_cl == 0:
            for x, y in door.pos:
                map[x][y] = "0"

    #スイッチリストから出力
    for switch in switch_list:
        x, y = switch.pos
        map[x][y] = "4"
        print_map[x][y] = f"{color_list[switch.switch_num]}○{color_list[-1]} "
    
    #プレイヤーリストから出力
    for player in player_list:
        if player == player_x:
            x1, y1 = player.x, player.y
            map[x1][y1] = "2"
            print_map[x1][y1] = f"{Color.RED}♥{Color.RESET} "
        else:
            x2, y2 = player.x, player.y
            map[x2][y2] = "6"
            print_map[x2][y2] = f"{Color.BLUE}♥{Color.RESET} "

    if goal_open == 0:
        map[goal_pos[0]][goal_pos[1]] = "3"#ゴール
        map[goal_pos[0]][goal_pos[1]] = "□"

    blind_map = copy.deepcopy(map)
    #for room in room_list:
        #if room.open == 0:
            #blind_map[room.left_up[0]:room.left_up[1]][room.right_down[0]:room.right_down[1]] = blind_sqare
    print("------------------------------------------------")
    for mapline in print_map:
        mapline = [" " if i == "0" else i for i in mapline]
        mapline = [f"{Color.WHITE}■ " if i == "1" else i for i in mapline]
        #mapline = ["♥" if i == "2" else i for i in mapline]
        #for switch in switch_list:
        #    switch.switch_num ==
        #mapline = ["□" if i == "3" else i for i in mapline]
        #mapline = ["○" if i == "4" else i for i in mapline]
        #mapline = ["☆" if i == "5" else i for i in mapline]
        #mapline = ["♡" if i == "6" else i for i in mapline]
        """
        mapline = "".join(mapline)
        mapline = mapline.replace("0", " ")
        mapline = mapline.replace("1", "■")
        mapline = mapline.replace("2", "♥")
        mapline = mapline.replace("3", "□")
        mapline = mapline.replace("4", f"{Color.RED}○{Color.RESET}")
        mapline = mapline.replace("5", "☆")
        mapline = mapline.replace("6", "♡")
        """
        fom = "{:<2}"*len(mapline)
        print(fom.format(*mapline))
    print("------------------------------------------------")
    return map

#ゲーム終了判定
def check_game_over(start_time):
    now = time.time()
    limit = now - start_time
    print(f"爆発まであと{900-round(limit)}秒")
    if limit >= 900:
        return 1

#ゲーム勝利判定
def check_game_clear(player_x, player_y):
    if player_x.x == 0 and player_x.y == 14 and player_y.x == 0 and player_y.y == 14:
        return 2
    return 0

#プレイヤーの切り替え
def change_player(play_player):
    if play_player == player_x:
        print("change to Y")
        return player_y
    else:
        print("change to X")
        return player_x

#ルールの表示
def print_rule():
    print(f"{Color.GREEN}～ストーリー～{Color.RESET}")
    print("爆弾の仕掛けられた東京工科大学にX君とY君が閉じ込められてしまった！爆弾が爆発する前に二人一緒に脱出しよう！")
    print("------------------------------------------------")
    print(f"{Color.GREEN}～ルール～{Color.RESET}")
    print("・部屋にある複数のギミックやアイテムを使ってゴールを目指そう！")
    print("・あなたはX君、Y君の二人を操作することができるよ.最初はX君から動かせるよ！")
    print("・X君とY君は一人ずつしか操作できないんだ...X君とY君を切り替えながら進もう！")
    #print("・ドア、スイッチ保留")
    print("・対応するスイッチを踏んでいる間だけドアが開くよ")
    print("・アイテムは一回使ったらなくなっちゃうよ")
    print("・X君とY君は電話を持っているから情報は共有出来るよ.でもアイテムは共有出来ないよ")
    print("・爆発までの制限時間は900秒だ！")
    print("------------------------------------------------")
    print(f"{Color.GREEN}～マップの表示と操作方法～{Color.RESET}")
    print("X君…♥　Y君…♡　アイテム…☆　スイッチ…〇　ドア…□")
    print("上…'w'　下…'s'　左…'a'　右…'d'")
    print("X君とY君の切り替え…'c'")
    print(f"アイテムや{Color.RED}{Color.BOLD}{Color.UNDERLINE}ドア{Color.RESET}を調べる…'space'")
    print("ルールを表示…'r'")
    s = input("Enterでスタート！：")

#壁と箱の衝突判定
def check_cpllide(map, x, y):
    print(map[x][y])
    if map[x][y] == "1" or map[x][y] == "3" or map[x][y] == "5":
        print("これ以上進めない")
        return True
    return False

#プレイヤーの移動
def move_player(map, direction, play_player):

    #操作しているプレイヤーの判定
    if play_player == player_x:
        move_player = player_x
    else:
        move_player = player_y
    
    #移動
    if direction == "a":
        move_player.y += -1
        if check_cpllide(map, move_player.x, move_player.y):
            move_player.y += 1
    elif direction == "w":
        move_player.x += -1
        if check_cpllide(map, move_player.x, move_player.y):
            move_player.x += 1
    elif direction == "s":
        move_player.x += 1
        if check_cpllide(map, move_player.x, move_player.y):
            move_player.x += -1
    elif direction == "d":
        move_player.y += 1
        if check_cpllide(map, move_player.x, move_player.y):
            move_player.y += -1

#ドアを開け閉め
def check_door(open_num):
    open_list = []
    for door in door_list:
        if door.door_num in open_num:
            door.op_cl = 0
            open_list.append(door.door_num)
        elif door.door_num != 0:
            door.op_cl = 1
    return open_list

#ドアを閉める
def close_door():
    pass

#スイッチを踏んでいるかの判定
def check_switch(player):
    for switch in switch_list:
        if (player.x, player.y) == switch.pos:
            #print(f"{switch.switch_num}のドアが開いた")
            return switch.switch_num

    return -1

#アクションを行う
def action(map, play_player, goal_open):
    find_obj = 0
    for dir in directions:#上下左右を調べる
        checkx = play_player.x + dir[0]
        checky = play_player.y + dir[1]
        if map[checkx][checky] == "3" or map[checkx][checky] == "5":#if箱かドアだったら
            for box in box_list:#箱リストから探して見つけたらbreak
                if box.pos == (checkx, checky):
                    find_obj = box
                    break
            for door in door_list:
                if door.pos[0] == (checkx, checky) or door.pos[1] == (checkx, checky):
                    find_obj = door
                    break
            if (checkx, checky) == goal_pos:
                find_obj = 1
    
    if type(find_obj) == Box:#見付けたのが箱だった場合
        if find_obj.item_info != 0:#ifただの箱でない
            if find_obj.item_info not in play_player.item_have:#必要なアイテムを持っていない
                if find_obj == battery_box:
                    #print("＊ガムテープででグルグル巻きになっている")
                    return f"{Color.YELLOW}＊ガムテープでグルグル巻きになっている{Color.RESET}"
                if find_obj == StudenCard_jihan:
                    #print("＊100円で僕の学生証が売ってる！！")
                    return f"{Color.YELLOW}＊100円で僕の学生証が売ってる！！{Color.RESET}"
                if find_obj == passward_4_box:
                    #print("＊掲示板に何も書かれてない紙が貼ってある")
                    return f"{Color.YELLOW}＊掲示板に何も書かれてない紙が貼ってある{Color.RESET}"
                if find_obj == projector_box:
                    #print("＊電源コードのないプロジェクタだ")
                    return f"{Color.YELLOW}＊電源コードのないプロジェクタだ{Color.RESET}"
                if find_obj == StudenCard_box:
                    #print("＊＋ドライバーでねじ留めされている")
                    return f"{Color.YELLOW}＊＋ドライバーでねじ留めされている{Color.RESET}"
                if find_obj == old_key_box:
                    #print("＊ロッカーの上に何かあるけど手が届かない")
                    return f"{Color.YELLOW}＊ロッカーの上に何かあるけど手が届かない{Color.RESET}"
                if find_obj == passward_6_box:
                    #print("＊金具で留められている")
                    return f"{Color.YELLOW}＊金具で留められている{Color.RESET}"
                if find_obj == key_cutter_box:
                    #print("＊4ケタのパスワードが必要なようだ")
                    return f"{Color.YELLOW}＊4ケタのパスワードが必要なようだ{Color.RESET}"
                if find_obj == righter_oil_box:
                    #print("＊ードライバーでねじ留めされている")
                    return f"{Color.YELLOW}＊ードライバーでねじ留めされている{Color.RESET}"
            else:#アイテムを持ってた
                #play_player.item_have.remove(find_obj.item_info)
                #print("箱を開いた")#自販機や掲示板のテキスト分けが必要
                get_item = find_obj.item[0]
                if len(find_obj.item) == 2:#手に入るのが二個以上だった場合
                    get_item = f"{find_obj.item[0]}と{find_obj.item[1]}"
                if find_obj == passward_4_box or find_obj == projector_box or find_obj == passward_6_box:#パスワードだった場合、相方にもアイテムを渡す
                    #print(f"{get_item}を手に入れた")
                    find_obj.empty = 1
                    if find_obj == passward_4_box:
                        for player in player_list:
                            player.item_have += [get_item]
                        return f"{Color.YELLOW}紙をあぶったら数字が浮き出た\n{get_item}を手に入れた{Color.RESET}"

                    if find_obj == projector_box:
                        for player in player_list:
                            player.item_have += [get_item]
                        return f"{Color.YELLOW}プロジェクタから数字が映し出された\n{get_item}を手に入れた{Color.RESET}"

                    if find_obj == passward_6_box:
                        for player in player_list:
                            player.item_have += [get_item]
                        return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}"
                
                elif find_obj == key_cutter_box:
                    try:
                        pas_4 = int(input(f"{Color.MAGENTA}パスワードを入力してください：{Color.RESET}"))
                        if pas_4 == pas_4_rand:
                            play_player.item_have += find_obj.item
                            #print(f"{get_item}を手に入れた")
                            for player in player_list:
                                player.item_have.remove(find_obj.item_info)
                            find_obj.empty = 1
                            return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}"
                        else:
                            #print("パスワードが間違っています")
                            return f"{Color.RED}パスワードが間違っています{Color.RESET}"
                    except ValueError:
                        return f"{Color.RED}パスワードが間違っています{Color.RESET}"
                
                else:
                    if (find_obj == righter_oil_box and "からのライター" in play_player.item_have):
                        play_player.item_have += ["ライター"]
                        play_player.item_have.remove("からのライター")
                        find_obj.empty = 1
                        return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}\n"+f"{Color.YELLOW}ライターにオイルを入れた{Color.RESET}"

                    elif (find_obj == battery_box and "電池のないランプ" in play_player.item_have):
                        play_player.item_have += ["ランプ"]
                        play_player.item_have.remove("電池のないランプ")
                        find_obj.empty = 1
                        return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}\n"+f"{Color.YELLOW}ランプに電池を入れた{Color.RESET}"
                    
                    else:
                        play_player.item_have += find_obj.item
                        #print(f"{get_item}を手に入れた")
                        find_obj.empty = 1
                        play_player.item_have.remove(find_obj.item_info)
                        return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}"

                
        else:#ただの箱
            get_item = find_obj.item[0]
            if find_obj == right_memo:
                get_item += f"({pas_right})"
            if find_obj == left_memo:
                get_item += f"({pas_left})"
            play_player.item_have += [get_item]
            #print(f"{get_item}を手に入れた")
            find_obj.empty = 1
            if (get_item == "電池のないランプ" and "電池" in play_player.item_have):
                play_player.item_have += ["ランプ"]
                play_player.item_have.remove("電池")
                find_obj.empty = 1
                return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}\n"+f"{Color.YELLOW}ランプに電池を入れた{Color.RESET}"
            if (get_item == "からのライター" and "ライターオイル" in play_player.item_have):
                play_player.item_have += ["ライター"]
                play_player.item_have.remove("ライターオイル")
                find_obj.empty = 1
                return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}\n"+f"{Color.YELLOW}ライターにオイルを入れた{Color.RESET}"
            #play_player.item_have.remove(find_obj.item_info)
            return f"{Color.YELLOW}{get_item}を手に入れた{Color.RESET}"

    elif type(find_obj) == Door:#ドアだった場合
        if find_obj.door_num == 0:#ifアイテムが必要なドアである
            if find_obj.door_item_info in play_player.item_have:#ifそのアイテムを持っている
                if find_obj == door_5_pas:
                    try:
                        pas_5 = int(input(f"{Color.MAGENTA}パスワードを入力してください：{Color.RESET}"))
                        if pas_5 == pas_5_rand:
                            find_obj.op_cl = 0
                            for player in player_list:
                                player.item_have.remove(find_obj.door_item_info)
                            return f"{Color.YELLOW}扉が開いた{Color.RESET}"
                        else:
                            return f"{Color.RED}パスワードが間違っています{Color.RESET}"
                    except ValueError:
                        return f"{Color.RED}パスワードが間違っています{Color.RESET}"
                elif find_obj == door_6_pas:
                    try:
                        pas_6 = int(input(f"{Color.MAGENTA}パスワードを入力してください：{Color.RESET}"))
                        if pas_6 == pas_6_rand:
                            find_obj.op_cl = 0
                            for player in player_list:
                                player.item_have.remove(find_obj.door_item_info)
                            return f"{Color.YELLOW}扉が開いた{Color.RESET}"
                        else:
                            return f"{Color.RED}パスワードが間違っています{Color.RESET}"
                    except ValueError:
                        return f"{Color.RED}パスワードが間違っています{Color.RESET}"
                
                #elif find_obj == door_8_pas:
                #    pas_8 = int(input("パスワードを入力してください："))
                #    if pas_8 == pas_8_rand:
                #        find_obj.op_cl = 0
                #        return "扉が開いた"
                #    else:
                #        return "パスワードが間違っています"
                elif find_obj == door_lamp:
                    find_obj.op_cl = 0
                    return f"{Color.YELLOW}ランプをつけた{Color.RESET}"
                
                else:
                    find_obj.op_cl = 0
                    return f"{Color.YELLOW}扉が開いた{Color.RESET}"

            else:#アイテムを持ってない
                if find_obj == door_x_student:
                    return f"{Color.YELLOW}＊学生証がないと通れない{Color.RESET}"
                if find_obj == door_y_student:
                    return f"{Color.YELLOW}＊学生証がないと通れない{Color.RESET}"
                if find_obj == door_werehouse_key:
                    return f"{Color.YELLOW}＊鍵がかかっている{Color.RESET}"
                if find_obj == door_lamp:
                    return f"{Color.YELLOW}＊暗くては入れない{Color.RESET}"
                if find_obj == door_old_key:
                    return f"{Color.YELLOW}＊鍵がかかっている{Color.RESET}"
                if find_obj == door_5_pas:
                    return f"{Color.YELLOW}＊5ケタのパスワードが必要なようだ{Color.RESET}"
                if find_obj == door_6_pas:
                    return f"{Color.YELLOW}＊6ケタのパスワードが必要なようだ{Color.RESET}"
                #if find_obj == door_8_pas:
                #    return "＊8ケタのパスワードが必要なようだ"
        else:#開いてないスイッチドア
            return f"{Color.YELLOW}{find_obj.door_num}と書かれている{Color.RESET}"

    try:
        if find_obj == 1:
            pas_8 = int(input(f"{Color.MAGENTA}パスワードを入力してください：{Color.RESET}"))
            if pas_8 == pas_8_rand:
                return 1
            else:
                return f"{Color.RED}パスワードが間違っています{Color.RESET}"
        else:
            return ""
    except ValueError:
        return f"{Color.RED}パスワードが間違っています{Color.RESET}"

#マップ情報を取得し、整える
with open("./map_sqare.txt") as fb:
    map_info = fb.readlines()
    for num in range(len(map_info)):
        map_info[num] = map_info[num].strip("\n")
        map_info[num] = map_info[num].split(",")
        #map_info[num] = [int(s) for s in map_info[num]]
    init_map = copy.deepcopy(map_info)

"""
with open("./blind_sqare.txt") as fb:
    blind_sqare = fb.readlines()
    for num in range(len(blind_sqare)):
        blind_sqare[num] = blind_sqare[num].strip("\n")
        blind_sqare[num] = blind_sqare[num].split(",")
"""

#初期化
init(map_info, game_state=0)

#ルール表示
print_rule()

#時間の基準
start_time = time.time()

map_info = print_out(map_info)

#メインループ
while game_state == 0:
    open_num = []
    print_txt = ""
    game_state = check_game_over(start_time)
    if game_state == 1:
        print("game over!!!!!!!")
        break
    
    print(f"X君の持ち物：\n{player_x.item_have}")
    print(f"Y君の持ち物：\n{player_y.item_have}")
    
        
    print("------------------------------------------------")
    do = ""
    while do == "":
        do = input("move or action: ")#入力を待つ
    if do == " ":
        print_txt = action(map_info, play_player, goal_open)
        if print_txt == 1:
            goal_open = 1
            print_txt == "扉が開いた"
    elif do == "c":
        play_player = change_player(play_player)
    elif do == "r":
        print_rule()
    else:
        move_player(map_info, do, play_player)
        open_door_list = [check_switch(player_x), check_switch(player_y)]
        open_num = check_door(open_door_list)
    map_info = print_out(map_info)
    if len(open_num) == 2:
        print(f"＊{open_num[0]}と{open_num[1]}のドアが開いている")
    if len(open_num) == 1:
        print(f"＊{open_num[0]}のドアが開いている")
    if print_txt != "":
        print(print_txt)
    print("------------------------------------------------")
    game_state = check_game_clear(player_x, player_y)
    if game_state == 2:
        print("game clear!!!!!!")
