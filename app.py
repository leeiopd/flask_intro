import datetime
from flask import Flask, render_template, request, redirect
import requests
from bs4 import BeautifulSoup
import csv

app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>hello!~</h1>'
    
@app.route('/helloo')
def helloo():
    return render_template('index.html')
    
@app.route('/hi')
def hi():
    return '안녕!, 지원'
    
@app.route('/dday')
def dday():
    end_date = datetime.datetime(2019, 5, 20)
    now = datetime.datetime.now()
    d = end_date - now
    # return 은 반드시 string으로 되어야 한다.
    return f'{d.days} 일 뒤에는 방학'
    
# variable routing
@app.route('/hi/<string:name>')
def greeting(name='홍길동'):
    return render_template('greeting.html', html_name = name)
    
# 세제곱의 결과를 출력해 볼까요
@app.route('/cube/<int:num>')
def cube(num):
    # return str(num**3)
    return  f'세제곱의 결과는 {num**3}'
    
@app.route('/movie')
def movie():
    movies = ['말모이', '극한직업', '국가부도의날', '신비한 동물 사전', '그린랜턴']
    return render_template('movie.html', movies=movies)
    
@app.route('/google')
def google():
    return render_template('google.html')
    
@app.route('/naver')
def naver():
    return render_template('naver.html')
        

@app.route('/ping')
def ping():
    return render_template('ping.html')
    
@app.route('/pong')
def pong():
    # .get()은 key가 없어도 에러 없이 none값 return
    name = request.args.get('name')
    msg = request.args.get('msg')
    return render_template('pong.html', name=name, msg=msg)
    # return render_template('pong.html')
    
@app.route('/opgg')
def opgg():
    return render_template('opgg.html')
    
@app.route('/opgg_result')
def opgg_result():
    url = 'http://www.op.gg/summoner/userName='
    username = request.args.get('username')
    response = requests.get(url+username).text
    soup = BeautifulSoup(response, 'html.parser')
    wins = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.wins')
    losses = soup.select_one('#SummonerLayoutContent > div.tabItem.Content.SummonerLayoutContent.summonerLayout-summary > div.SideContent > div.TierBox.Box > div.SummonerRatingMedium > div.TierRankInfo > div.TierInfo > span.WinLose > span.losses')
    
    return render_template('opgg_result.html', userName=username, wins=wins.text, losses=losses.text)

# ---------------------------------------------------------------------------------------------------------------

@app.route('/timeline')
def timeline():
    # 지금까지 기록되어있는 방명록들 ('timeline.csv')
    # 를 읽어서 보여주자!
    
    with open('timeline.csv', 'r',encoding='utf-8', newline='' ) as f:
        reader = csv.DictReader(f)
        timelines=[]
        for row in reader:
            timelines.append(row)
            
    return render_template('timeline.html', timelines=timelines)
    
    
    
    
    
@app.route('/timeline/create')
def timeline_create():
    username = request.args.get('username')
    message = request.args.get('message')
    
    # a : append, w :wirte
    with open('timeline.csv', 'a', encoding='utf-8', newline='') as f:
        fieldnames = ['username', 'message']
        write = csv.DictWriter(f, fieldnames=['username', 'message'])
        write.writerow(
            {
                'username':username,
                'message':message
            })
        
        
    # return render_template('timeline_create.html', username=username, message=message)
    return redirect('/timeline')
    
#---------------------------------------------------------------------------
    
@app.route('/dictionary/<string:word>')
def words(word):
    mean = '나만의 단어장에 없는 내용입니다'
    with open('dictionary.scv', 'r', encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row['word'] == word:
                mean = row['mean']
            
    return render_template('dictionary.html', word=word, mean=mean)
    
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8080', debug=True)