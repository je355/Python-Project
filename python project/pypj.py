import random
import time

# 그림 생성 함수
def create_picture(rows, cols):
    picture = []
    for _ in range(rows):
        row = []
        for _ in range(cols):
            pixel = random.choice(['0', '-'])
            row.append(pixel)
        picture.append(row)
    return picture

# 그림 출력 함수
def print_picture(picture):
    for row in picture:
        print(' '.join(row))

# 그림 숨김 함수
def hide_picture(picture, num_hidden):
    hidden_picture = [row[:] for row in picture]  # 그림을 복사하여 숨김 그림을 생성
    hidden_coords = []
    rows, cols = len(picture), len(picture[0])

    # 숨길 픽셀 좌표 선택
    while len(hidden_coords) < num_hidden:
        coord = (random.randint(0, rows - 1), random.randint(0, cols - 1))
        if coord not in hidden_coords:
            hidden_coords.append(coord)
            hidden_picture[coord[0]][coord[1]] = 'X'  # 픽셀을 X로 변경

    return hidden_picture, hidden_coords

# 게임 실행 함수
def play_game(rows, cols, num_hidden):
    picture = create_picture(rows, cols)
    hidden_picture, hidden_coords = hide_picture(picture, num_hidden)
    attempts = 1

    print()
    print("......................")
    print("Hello, Capybara World!")
    print("......................")
    print()
    time.sleep(2)

    print("카피바라 세계에 오신 것을 환영합니다.")
    print('(*ˊᗜˋ*)ᵗʰᵃⁿᵏ ʸᵒᵘ')
    print()
    start = input("카피바라를 만나시겠습니까? \n실행을 위해서는 공백을 입력해주세요. > ")
    print()

    if start == ' ':
        time.sleep(2)

        print('.................................')
        print()
        print('          1. 게임시작')
        print()
        print('          2. 게임방법')
        print()
        print('          3. 게임종료')
        print()
        print('.................................')
        
        num = input('실행할 서비스의 번호를 입력하세요 > ')
        print()
        if num == '1':
            name = input('사용자의 이름을 알려주세요! > ')
            print(name, "님, 게임을 시작합니다.")
            print()
            time.sleep(2)

            print()
            print("                            /\\     /\\")
            print("                            ---------")
            print("                          /            \\")
            print("                         /      ㅡ    ㅡ|")
            print("   ---------------------             [] |")
            print("  /                                     | ")
            print(" /                                     /")
            print("|                                     /")
            print("|                                    /")
            print(" \                                  |")
            print("  |                                 /")
            print("  |    -   -------------   -----   |")
            print("  |  /  | |             | |      \\ |")
            print("  /  |  | \             | \      |  \\")
            print("  ---    --              ---       ---")
            print()
            time.sleep(2)

            while True:
                print()
                print_picture(picture)
                print("찾을 픽셀 좌표를 입력하세요 : ")
                row_guess, col_guess = map(int, input().split())

                if row_guess < 0 or row_guess >= rows or col_guess < 0 or col_guess >= cols:
                    print("입력한 좌표가 그림의 범위를 벗어났습니다. 다시 입력하세요.")
                    print('(*`н´*)')
                    print()
                    continue
        
                if (row_guess, col_guess) in hidden_coords:
                    print("축하합니다! 숨은 카피바라를 찾았습니다.")
                    time.sleep(1)
                    print()
                    print('      /|        |\\')
                    print('     / |        | \\')
                    print('     --------------')
                    print('    /              \\')
                    print('   /                \\')
                    print('   |   []      []   |')
                    print('   |                |')
                    print('  /       -----      \\')
                    print(' /       /     \\      \\')
                    print('|       | ----- |      |')
                    print('|       |   |   |      |')
                    print(' \      |  ---  |     /')
                    print('  \      -------     /')
                    print('   ------------------')
                    print()
                    time.sleep(1)
                    print('*ੈ✩‧₊˚(๑ ᐢ ᵕ ᐢ ๑)𝚈𝙾𝚄𝚁 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃*ੈ✩‧₊˚')
                    print()
                    break
                else:
                    print("카피바라를 찾지 못했습니다. 다시 시도하세요.")
                    print('୧( ˙Ⱉ˙⠕)୨')
                    print()
                    attempts += 1

                    # 힌트 제공
                    adjacent_coords = []
                    for dr in [-1, 0, 1]:
                        for dc in [-1, 0, 1]:
                            if dr == 0 and dc == 0:
                                continue

                            adj_row = row_guess + dr
                            adj_col = col_guess + dc
                            if 0 <= adj_row < rows and 0 <= adj_col < cols:
                                adjacent_coords.append((adj_row, adj_col))

                    hidden_adjacent_coords = [coord for coord in adjacent_coords if coord in hidden_coords]
                    if hidden_adjacent_coords:
                        print("힌트: 주변에 숨은 카피바라가 있습니다!")
                    else:
                        print("힌트: 주변에 숨은 카피바라가 없습니다.")

            print()
            print("게임 종료!") 
            time.sleep(1)
            print('✧*｡٩(ˊᗜˋ*)و✧*｡')
            print()
            time.sleep(1)
            print(name, "님의 총 시도 횟수:", attempts)
        
        elif num == '2':
            print('..................................................................')
            print()
            print('                           게임 방법')
            print()
            print()
            print('1. 게임을 시작하면 가로 세로 8칸의 보드가 나타납니다.')
            print()
            print('2. 보드 판 속에는 카피바라가 숨겨져 있습니다.')
            print()
            print('3. 좌표를 0 1, 3 4와 같이 입력합니다.')
            print()
            print('4. 만약 입력한 좌표 근처에 카피바라가 숨어있다면 \n카피바라가 주변에 숨어있다는 메시지를 \n근처에 없다면 주변에 숨어있지 않다는 메시지를 출력합니다.')
            print()
            print('5. 주어진 힌트를 이용하여 \n카피바라 위치 범위를 조금씩 좁혀나갑니다.')
            print()
            print('6. 만약 카피바라를 찾게 된다면\n카피바라를 찾을 때까지 시도한 횟수가 출력됩니다.')
            print()
            print()
            print('..................................................................')
            
            game = input('게임을 시작하려면 공백을 출력하세요 > ')
            if game == ' ':
                name = input('사용자의 이름을 알려주세요! > ')
                print(name, "님, 게임을 시작합니다.")
                print()
                time.sleep(2)

                print()
                print("                            /\\     /\\")
                print("                            ---------")
                print("                          /            \\")
                print("                         /      ㅡ    ㅡ|")
                print("   ---------------------             [] |")
                print("  /                                     | ")
                print(" /                                     /")
                print("|                                     /")
                print("|                                    /")
                print(" \                                  |")
                print("  |                                 /")
                print("  |    -   -------------   -----   |")
                print("  |  /  | |             | |      \\ |")
                print("  /  |  | \             | \      |  \\")
                print("  ---    --              ---       ---")
                print()
                time.sleep(2)

                while True:
                    print()
                    print_picture(picture)
                    print("찾을 픽셀 좌표를 입력하세요 : ")
                    row_guess, col_guess = map(int, input().split())

                    if row_guess < 0 or row_guess >= rows or col_guess < 0 or col_guess >= cols:
                        print("입력한 좌표가 그림의 범위를 벗어났습니다. 다시 입력하세요.")
                        print('(*`н´*)')
                        print()
                        continue
        
                    if (row_guess, col_guess) in hidden_coords:
                        print("축하합니다! 숨은 카피바라를 찾았습니다.")
                        time.sleep(1)
                        print()
                        print('      /|        |\\')
                        print('     / |        | \\')
                        print('     --------------')
                        print('    /              \\')
                        print('   /                \\')
                        print('   |   []      []   |')
                        print('   |                |')
                        print('  /       -----      \\')
                        print(' /       /     \\      \\')
                        print('|       | ----- |      |')
                        print('|       |   |   |      |')
                        print(' \      |  ---  |     /')
                        print('  \      -------     /')
                        print('   ------------------')
                        print()
                        time.sleep(1)
                        print('*ੈ✩‧₊˚(๑ ᐢ ᵕ ᐢ ๑)𝚈𝙾𝚄𝚁 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃*ੈ✩‧₊˚')
                        print()
                        break
                    else:
                        print("카피바라를 찾지 못했습니다. 다시 시도하세요.")
                        print('୧( ˙Ⱉ˙⠕)୨')
                        print()
                        attempts += 1

                        # 힌트 제공
                        adjacent_coords = []
                        for dr in [-1, 0, 1]:
                            for dc in [-1, 0, 1]:
                                if dr == 0 and dc == 0:
                                    continue

                                adj_row = row_guess + dr
                                adj_col = col_guess + dc
                                if 0 <= adj_row < rows and 0 <= adj_col < cols:
                                    adjacent_coords.append((adj_row, adj_col))

                        hidden_adjacent_coords = [coord for coord in adjacent_coords if coord in hidden_coords]
                        if hidden_adjacent_coords:
                            print("힌트: 주변에 숨은 카피바라가 있습니다!")
                        else:
                            print("힌트: 주변에 숨은 카피바라가 없습니다.")

                print()
                print("게임 종료!") 
                time.sleep(1)
                print('✧*｡٩(ˊᗜˋ*)و✧*｡')
                print()
                time.sleep(1)
                print(name, "님의 총 시도 횟수:", attempts)

            else:
                print('!!(ﾉﾟﾛﾟ)o･：*‥…━━━☆)ﾟ3ﾟ(★━━━…‥*：･o(ﾟﾛﾟヽ)')
                print()
                time.sleep(1)
                print('게임을 종료합니다.') 

        elif num == '3':
            print('!!(ﾉﾟﾛﾟ)o･：*‥…━━━☆)ﾟ3ﾟ(★━━━…‥*：･o(ﾟﾛﾟヽ)')
            print()
            time.sleep(1)
            print('게임을 종료합니다.')

    else:
        print("게임을 시작하지 않았습니다. 다음에 다시 만나요!")
        print('٩(⌯꒦ິ̆ᵔ꒦ິ)۶ᵒᵐᵍᵎᵎᵎ')

rows = 8
cols = 8
num_hidden = 10
play_game(rows, cols, num_hidden)
