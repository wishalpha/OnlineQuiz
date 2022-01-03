#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  9 18:18:54 2022

@author: hujiujiu
"""

import flask
import pandas as pd
import os,glob
from datetime import datetime
from flask import Flask,request,redirect
from quiz_generator import addition, subtraction, multiplication,division,GCD,LCM,CRP,Sequence,spelling

import glob

current_user={}

start_time=''

app = Flask(__name__)


def user_profile_update (user,login=0,points=0,pra=0,exam=0):
    with open(f"Users/{user.lower()}/data.txt",'r') as f:
        l=int(f.readline())
        pts=int(f.readline())
        p=int(f.readline())
        e=int(f.readline())

    with open(f"Users/{user.lower()}/data.txt",'w') as f:
        f.write (f"{l+login}\n{pts+points}\n{p+pra}\n{e+exam}\n")
    return {'name':user,'login':l+login,'points':pts+points ,'practice':p+pra,'exam':e+exam}

def problem_record (problem,answer):
    pass
@app.route("/")
def index():

    html="""
    <h1> welcome to the mini math quiz !!! </h1>

    <p>
    <form action="/auth" method="get">

        <lable for="name">User name </lable>
        <input type="text" name="name">    <br>

        <lable for="password">Password </lable>
        <input type="password" name="password">    <br>

    <input type="submit" value="login/register">
    </form>
    </p>
    """

    return html
@app.route("/unauth")
def unauth():

    html="""
    <h2> your password is incorrect, please reenter or register a new user</h2>
    <p>
    <form action="/auth" method="get">

        <lable for="name">User name </lable>
        <input type="text" name="name">    <br>

        <lable for="password">Password </lable>
        <input type="password" name="password">    <br>

    <input type="submit" value="login/register">
    </form>
    <p>
    """

    return html

@app.route("/auth")
def auth():
    global current_user
    user=request.args.get("name", "guest")
    user=''.join(user.lower().split(' '))
    password=request.args.get("password",'0')
    try:
        user_profiles=pd.read_csv("data/profiles.txt",sep=' ', index_col=False, names=['name','password','admin','tester'])
    except:
        with open ("data/profiles.txt",'w') as f:
            f.write ('guest 0 0 0 \n')
        user_profiles=pd.read_csv("data/profiles.txt",sep=' ', index_col=False, names=['name','password','admin','tester'])
    #print(user_profiles)
    if user.lower() in list(user_profiles['name']):
        if password==str(user_profiles.loc[user_profiles['name']==user.lower()]['password'].item()):
            #current_user=(user_profiles.loc[user_profiles['name']==user.lower()])
            pass
        else:
            return redirect('/unauth')
    else:
        with open('data/profiles.txt','a') as f:
            f.write (f'{user} {password} 0 0 \n')

    if not os.path.exists(f"Users/{user.lower()}"):
        os.makedirs(f"Users/{user.lower()}")
        with open(f"Users/{user.lower()}/data.txt",'w') as f:
            f.write('0\n0\n0\n0\n') # login time, total point, number of practice, number of exam

    current_user=user_profile_update(user,login=1)
    #current_user=(user_profiles.loc[user_profiles['name']==user.lower()])


    html=f"""
         <h1> welcome back {user} </h1> <br>
         <p> you have logined {current_user["login"]} times of quize </p> <br>
         <p> you have played {current_user["practice"]+current_user['exam']} times of excercise </p> <br>
         <p> What do you want to do this time? </p>

    <form action="/excercise" method="get">

        <p> I want to do
        <input type="radio" name="mode" value="a" id="add">
        <lable for='add'> addition </lable>
        <input type="radio" name="mode" value="s" id="sub">
        <lable for='sub'> subtraction </lable>
        <input type="radio" name="mode" value="m" id="mul">
        <lable for='mul'> multiplication </lable>
        <input type="radio" name="mode" value="d" id="div">
        <lable for='div'> division </lable> <br>
        
        <input type="radio" name="mode" value="GCD" id="GCD">
        <lable for='GCD'> Greatest Common Dividor</lable>
        <input type="radio" name="mode" value="LCM" id="LCM">
        <lable for='LCM'> Least Common Multiple </lable>
        <input type="radio" name="mode" value="Seq" id="seq">
        <lable for='seq'> number sequence</lable>
        <input type="radio" name="mode" value="CRP" id="CRP">
        <lable for='CRP'> Chicken & Rabbits </lable> <br>


        <input type="radio" name="mode" value="spelling" id="spelling">
        <lable for='spelling'> sight word spelling </lable> <br>
        
        </p>
        <p> I want to do
        <lable for="number"> </lable>
        <input type="text" name="number"> questions <br>

        I want the number is limited to
        <lable for="Cap"> </lable>
        <input type="text" name="Cap"> <br>

    <input type="submit" value="Start the test">

    """
    return html
@app.route("/retake")
def retake ():
    global current_user
    user=request.args.get("name", "guest")
    user=''.join(user.lower().split(' '))
    html=f"""
         <h1> welcome back {user} </h1> <br>
         <p> you have logined {current_user["login"]} times of quize </p> <br>
         <p> you have played {current_user["practice"]+current_user['exam']} times of excercise </p> <br>
         <p> What do you want to do this time? </p>

    <form action="/excercise" method="get">

        <p> I want to do
        <input type="radio" name="mode" value="a" id="add">
        <lable for='add'> addition </lable>
        <input type="radio" name="mode" value="s" id="sub">
        <lable for='sub'> subtraction </lable>
        <input type="radio" name="mode" value="m" id="mul">
        <lable for='mul'> multiplication </lable>
        <input type="radio" name="mode" value="d" id="div">
        <lable for='div'> division </lable> <br>
        
        <input type="radio" name="mode" value="GCD" id="GCD">
        <lable for='GCD'> Greatest Common Dividor</lable>
        <input type="radio" name="mode" value="LCM" id="LCM">
        <lable for='LCM'> Least Common Multiple </lable>
        <input type="radio" name="mode" value="Seq" id="seq">
        <lable for='seq'> number sequence</lable>
        <input type="radio" name="mode" value="CRP" id="CRP">
        <lable for='CRP'> Chicken & Rabbits </lable> <br>


        <input type="radio" name="mode" value="spelling" id="spelling">
        <lable for='spelling'> sight word spelling </lable> <br>
        
        
        </p>
        <p> I want to do
        <lable for="number"> </lable>
        <input type="text" name="number"> questions <br>

        I want the number is limited to
        <lable for="Cap"> </lable>
        <input type="text" name="Cap"> <br>

    <input type="submit" value="Start the test">

    """
    return html
@app.route("/excercise")
def exercise ():
    #global problem
    num=int(request.args.get("number",20))
    level=int(request.args.get("Cap",20))
    mode=request.args.get("mode","a")
    if mode=="a":

        problem=addition(num,level)
    elif mode=='s':
        problem=subtraction(num,level)
    elif mode=='m':
        problem=multiplication(num,level)
    elif mode=='d':
        problem=division(num,level)
        
    elif mode=='GCD':
        problem=GCD(num,level)
    elif mode=='LCM':
        problem=LCM(num,level)
    elif mode=='Seq':
        problem=Sequence(num,level)
    elif mode=='CRP':
        problem=CRP(num,level)
    elif mode=='spelling':
        problem=spelling(num,level)

    else:
        problem=addition(num,level)
    html="""
            <html>
            <head>
            <style>

            </style>
            </head>
            <body>
            <p>Please key in the answer for all questions </p>

            <form action="/results" method="get">
            <table>
        """
    if mode=='spelling':
        
        html+= """
                <audio id='word_audio' controls>
                    <source src='/static/does.mp3' type='audio/mp3'>
                    Your browser does not support the audio element.
                    </audio>    
        
        <script> 
                var aid = document.getElementById('word_audio'); 
                
                function playAid(path) { 
                    aid.src=path;
                    aid.play(); 
                } 
                

            </script> 
        
        """
        for i in range(len(problem)):
            html+=f"""
    
                <tr>
                    <td> <button type="button" onclick="playAid('/static/{problem[i][1]}.mp3')">play Q{i}</button> </td>
                    <td><input type="text" name="{problem[i][0]}{problem[i][1]}" value=''> <td>
                </tr>
    
    
            """
            
    else:
        
        for i in range(len(problem)):
            html+=f"""
    
                <tr>
                    <td><lable for="{problem[i][0]}{problem[i][1]}"> {problem[i][0]} </lable> </td>
                    <td><input type="text" name="{problem[i][0]}{problem[i][1]}" value=''><td>
                </tr>
    
    
            """
    html+="""
             </table>
               <p> <input type="submit" value="submit"> </p>
            </form>
            </body>
            </html>
         """
    global start_time
    start_time=datetime.now()
    return html

@app.route("/results")

def results ():
    result=request.args
    global current_user
    global start_time
    mark =0
    name=current_user['name']
    total=len(result)

    min_taken=(datetime.now()-start_time).total_seconds()//60
    sec_taken=(datetime.now()-start_time).total_seconds()%60

    now=datetime.now().strftime("%y-%m-%d-%H-%M")
    with open (f'Users/{name}/{now}.txt','w') as f:
        f.write('******************************\n')
        f.write(f'time taken : {min_taken} m {sec_taken:.1f} s\n')
        index=1

        for q,a in result.items():
            q1=q.split('=')[0]
            a1=q.split('=')[1]
            if a=='':
                f.write(f'Qestion{index}: {q1}=? {name} did not input any answer\n')
            else:

                if a1==a:
                    mark+=1
                    f.write(f'Qestion{index}: {q1}=? {name} answer is {a} well done!!\n')
                else:
                    f.write(f'Qestion{index}: {q1}=? {name} answer is {a} and the correct answer is {a1}\n')
            index+=1
        f.write(f'results:{mark} out of {total}\n')

    current_user=user_profile_update(current_user['name'],points=mark,pra=1)
    total_points=current_user['points']
    for file in glob.glob("static/*.mp3"):
        os.remove(file)
    return f"""
            <h1>congrat {name}, you have got {mark} out of {total} for this quiz</h1>

            <p> you have earned {total_points} so far!!! </p>

            <p>
            <button type="button"> <a href='/history'>History</a>   </button>

                        <form action="/retake">
                <input type='hidden' name='name' value={name}>
                <input type='submit' value="Retake a test">

            </form>

            </p>

           """

@app.route("/history")

def history ():
    global current_user
    name=current_user['name']
    html="""
                <style>
                   table, th, td {border: 1px solid black;}
                   table.center {margin-left: auto;
                                 margin-right: auto; }
               </style>
        """

    html+=f"""  <h1>Hi {name}, you have done so much on the math!!</h1>

                <table>

                  <tr>
                    <th>index</th>
                    <th>date</th>
                    <th>time used</th>
                    <th>Scores</th>

                  </tr>


    """

    filelist=glob.glob(f'Users/{name}/*-*')
    filelist.sort()

    for i,file in enumerate (filelist):
        with open (file,'r') as f:
            lines=f.readlines()
            times=file.split('.')[0].split('/')[2].split('-')
            year,month,day,hour,mins=times

            time_taken=lines[1].split(':')[1]
            result=lines[-1].split(':')[1]
            try:
                score= int(result.split(' out of ')[0]) / int( result.split(' out of ')[1])
            except:
                score=0

            html+=f"""
                   <tr>
                    <td><a href="/history/view?file={file}">   {i}   </a></th>
                    <td>{year}/{month}/{day}</th>
                    <td>{time_taken}</th>
                    
                    <td>{score*100:.2f}%</th>
                    <td>{result}</th>

                  </tr>


            """

    html+=f"""
            </table>
            <form action="/retake">
                <input type='text' name='name' value={name}>
                <input type='submit' value="Retake a test">

            </form>
    """
    return html

@app.route ('/history/view')
def view_history ():
    file=request.args['file']
    name=file.split('/')[1]
    with open(file,'r') as f:
        text=f.readlines()

    html=''

    for line in text:
        html+=line[0:-1]+'<br>'

    html+=f"""

            <button type="button"> <a href='/history'>back</a>   </button>

            <form action="/retake">
                <input type='text' name='name' value={name}>
                <input type='submit' value="Retake a test">

            </form>




"""
    return html



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)

