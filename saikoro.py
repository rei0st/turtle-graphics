#新しいデータ型の作成
import random
class Dice:#新しいデータ型 サイコロの設計図を作る
    face_num=6#サイコロは6面持っている
    def shoot(self):#メソッドを定義するときは常に引数を１つ書く。(最初の引数はselfという名前にする)        
        return random.randint(1,6)#ランダムでサイコロの数字

sai=Dice()#サイコロの実体を1面作る
print(sai.shoot())#サイコロ sai の shoot() メソッドを呼び出して表示