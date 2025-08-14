import random

hands = ['グー', 'チョキ', 'パー']
results = {'win':'勝ち', 'lose':'負け', 'draw':'あいこ'}

def start_message():
  print('じゃんけんスタート')


#自分が出す手のバリデーション
def is_hand(string):
  if string.isdigit():
    number = int(string)
    if number >= 0 and number <= 2:
      return True
    else:
      return False
  else:
    return False


#自分が出す手の入力メッセージ生成関数
def get_my_hand():
  print('自分の手を入力してください')
  input_message = ''
  index = 0
  for hand in hands:
    input_message += str(index) + ':' + hand
    if index < 2:
      input_message += ', '
    index += 1
  return input(input_message)


#CPUが出す手の生成関数
def get_you_hand():
  return random.randint(0, 2)


#出された手の表示名を取得する関数
def get_hand_name(hand_number):
  return hands[hand_number]


#出された手の表示関数
def view_hand(my_hand, you_hand):
  print('自分の手は ' + get_hand_name(my_hand))
  print('相手の手は ' + get_hand_name(you_hand))


#じゃんけん結果の計算関数
def get_result(hand_diff):
  if hand_diff == 0:
    return 'draw'
  elif hand_diff == -1 or hand_diff == 2:
    return 'win'
  else:
    return 'lose'


#じゃんけん結果の表示関数
def view_result(result):
  print(results[result])


#ゲーム全体の実行関数
def play():
  my_hand = get_my_hand()
  while not is_hand(my_hand):
    my_hand = get_my_hand()

  my_hand = int(my_hand)
  you_hand = get_you_hand()
  hand_diff = my_hand - you_hand

  view_hand(my_hand, you_hand)
  result = get_result(hand_diff)
  view_result(result)
  if result == 'draw':
    play()



start_message()
play()