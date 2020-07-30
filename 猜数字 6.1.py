#1.欢迎进入“幸运数字猜猜猜游戏3.0 郭彩萍 2020.6.1 ”
#2.输入用户名称，默认用户没有游戏币
#3.提示用户充值购买游戏币
#4.游戏币规则：20块钱10个游戏币，充值必须是20的倍数，可重复充值
#5.一局游戏花费两枚游戏币，猜测正确奖励两枚游戏币，猜测错误，没有奖励
#6.没有游戏币后，自动退出，提示是否再次充值

import random

print("欢迎进入 幸运数字猜猜猜3.0 郭彩萍 2020.6.1")

username = input("请输入用户名：")
money=0
answer=input("确定进入游戏吗（y/n）")
if answer=="y":
    while money<2:
    
        n=int(input("游戏币不足，请充值（20块钱10个游戏币，充值必须是20的倍数）"))
        if n%20==0 and n>0:
            money=(n//20)*10
            print("当前剩余游戏币是：",money)
            print("玩一局游戏扣除两枚游戏币")
            
            print("进入游戏...............")
            
            while True:
                number=random.randint(1,10)
                print("幸运数字已经确定，请开始猜测！")
                money-=2
                temp=input("请输入您猜测的数字：")
                guess=int(temp)
                if guess==number:
                    print("恭喜您，猜对了!获得两枚游戏币奖励！")
                    money+=2
                else:
                    print("抱歉，猜错了。")
                    
                answer1=input("是否扣除两枚游戏币，再来一局？（y/n)")
                if answer1=="n" :
                    print("退出游戏！")
                    break
                else:
                    if money<2:
                        answer2=input("游戏币已用完，是否再次充值？（y/n)")
                        if answer2=="n":
                            print("游戏结束！")
                            break
                        else:
                            break
    
else:
    print("退出游戏")
                
                
            
                
        
            
        
        
        
        



       
            
            
        
    
