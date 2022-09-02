import string
import re
import jieba

import numpy as np
from py2neo import Node, Relationship, Graph, NodeMatcher, RelationshipMatcher
#from py2neo import Node,Relationship,Graph,Path,Subgraph
#from py2neo import NodeMatcher,RelationshipMatcher


from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)


# 只接受get方法访问
@app.route("/api/", methods=["GET"])
def check():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    #age = get_data.get('age')
    # 对参数进行操作
    #return_dict['result'] = tt(name, age)
    return_dict['result'] = chaxun(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)
    # return json.dumps("nmap", ensure_ascii=False)
@app.route("/api/xxsjtool/", methods=["GET"])
def xxsjtool():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    #age = get_data.get('age')
    # 对参数进行操作
    #return_dict['result'] = tt(name, age)
    return_dict['result'] = xxsjtools(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)
    # return json.dumps("nmap", ensure_ascii=False)
@app.route("/api/ls/", methods=["GET"])
def ls():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    #age = get_data.get('age')
    # 对参数进行操作
    #return_dict['result'] = tt(name, age)
    return_dict['result'] = lschaxun(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)
    # return json.dumps("nmap", ensure_ascii=False)
@app.route("/api/lsname/", methods=["GET"])             #漏扫名称
def lsn():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    #age = get_data.get('age')
    # 对参数进行操作
    #return_dict['result'] = tt(name, age)
    return_dict['result'] = lsname(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)
    # return json.dumps("nmap", ensure_ascii=False)
@app.route("/api/lsnames/", methods=["GET"])             #漏扫名称
def lsns():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    #age = get_data.get('age')
    # 对参数进行操作
    #return_dict['result'] = tt(name, age)
    return_dict['result'] = lsnames(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)
    # return json.dumps("nmap", ensure_ascii=False)
@app.route("/api/st/", methods=["GET"])
def st():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    #age = get_data.get('age')
    # 对参数进行操作
    #return_dict['result'] = tt(name, age)
    return_dict['result'] = stchaxun(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)
    # return json.dumps("nmap", ensure_ascii=False)
@app.route("/api/sts/", methods=["GET"])
def sts():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    #age = get_data.get('age')
    # 对参数进行操作
    #return_dict['result'] = tt(name, age)
    return_dict['result'] = stchaxuns(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)
    # return json.dumps("nmap", ensure_ascii=False)
@app.route("/api/hj/", methods=["GET"])
def hj():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    #age = get_data.get('age')
    # 对参数进行操作
    #return_dict['result'] = tt(name, age)
    return_dict['result'] = hjchaxun(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)




    # return json.dumps("nmap", ensure_ascii=False)
# 功能函数
#def tt(name, age):
#    result_str = "%s今年%s岁" % (name, age)
#    return result_str
@app.route("/api/hjs/", methods=["GET"])
def hjs():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    #age = get_data.get('age')
    # 对参数进行操作
    #return_dict['result'] = tt(name, age)
    return_dict['result'] = hjchaxuns(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)

@app.route("/api/tq/", methods=["GET"])     #提权
def tq():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    #age = get_data.get('age')
    # 对参数进行操作
    #return_dict['result'] = tt(name, age)
    return_dict['result'] = tq(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)
@app.route("/api/tqs/", methods=["GET"])     #提权
def tqs():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    #age = get_data.get('age')
    # 对参数进行操作
    #return_dict['result'] = tt(name, age)
    return_dict['result'] = tqs(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)


def tqs(index):
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]    #将输入每个数以空格键隔开做成数组
    arr2=[]             #记录多少个
    node_matcher = NodeMatcher(graph)
    # for q in range(len(arr)):
    #     # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
    nodes = list(node_matcher.match("TQ").where("_.func=~ \'"+arr+"\' "))
    for i in range(len(nodes)):
        # arr2.append(nodes[i]['os'])
        arr2.append(nodes[i]['id'])

        arr2.append(nodes[i]['func'])
        arr2.append(nodes[i]['type'])

    return arr2
@app.route("/api/hm/", methods=["GET"])     #提权
def hm():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    #age = get_data.get('age')
    # 对参数进行操作
    #return_dict['result'] = tt(name, age)
    return_dict['result'] = hm(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)
def hm(index):
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]    #将输入每个数以空格键隔开做成数组
    arr2=[]             #记录多少个
    node_matcher = NodeMatcher(graph)
    for q in range(len(arr1)):
        # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
        nodes = list(node_matcher.match("HMZR"))
        for i in range(len(nodes)):
            # arr2.append(nodes[i]['type'])
            # arr2.append(nodes[i]['id'])
            arr2.append(nodes[i]['method'])
            # arr2.append(nodes[i]['method'])
    newlist = list(dict.fromkeys(arr2))
    return newlist
@app.route("/api/hms/", methods=["GET"])     #提权
def hms():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    #age = get_data.get('age')
    # 对参数进行操作
    #return_dict['result'] = tt(name, age)
    return_dict['result'] = hms(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)


def hms(index):
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]    #将输入每个数以空格键隔开做成数组
    arr2=[]             #记录多少个
    node_matcher = NodeMatcher(graph)
    # for q in range(len(arr)):
    #     # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
    nodes = list(node_matcher.match("HMZR").where("_.method=~ \'"+arr+"\' "))
    for i in range(len(nodes)):
        # arr2.append(nodes[i]['os'])
        arr2.append(nodes[i]['id'])

        arr2.append(nodes[i]['method'])
        arr2.append(nodes[i]['type'])

    return arr2
def tt(name):
    result_str = "输入%s" % (name)
    return result_str
def xxsjtools(index):
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]    #将输入每个数以空格键隔开做成数组
    arr2=[]             #记录多少个
    node_matcher = NodeMatcher(graph)
    for q in range(len(arr1)):
        # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
        nodes = list(node_matcher.match("TOOL"))
        for i in range(len(nodes)):
            # arr2.append(nodes[i]['type'])
            # arr2.append(nodes[i]['id'])
            arr2.append(nodes[i]['tool'])
            # arr2.append(nodes[i]['method'])
    newlist = list(dict.fromkeys(arr2))
    return newlist
def lschaxun(index):
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]    #将输入每个数以空格键隔开做成数组
    arr2=[]             #记录多少个
    node_matcher = NodeMatcher(graph)
    for q in range(len(arr1)):
        # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
        nodes = list(node_matcher.match("lstools").where("_.type=~ \'"+arr1[q]+"\' "))
        for i in range(len(nodes)):
            arr2.append(nodes[i]['type'])
            arr2.append(nodes[i]['id'])
            arr2.append(nodes[i]['tool'])
            arr2.append(nodes[i]['method'])
    return arr2

def lsname(index):                  #漏扫工具名称
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]    #将输入每个数以空格键隔开做成数组
    arr2=[]             #记录多少个
    node_matcher = NodeMatcher(graph)
    for q in range(len(arr1)):
        # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
        nodes = list(node_matcher.match("lstools").where("_.type=~ \'"+arr1[q]+"\' "))
        for i in range(len(nodes)):
            # arr2.append(nodes[i]['type'])
            # arr2.append(nodes[i]['id'])
            arr2.append(nodes[i]['tool'])
            # arr2.append(nodes[i]['method'])
    return arr2
def lsnames(index):                  #漏扫工具名称
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]    #将输入每个数以空格键隔开做成数组
    arr2=[]             #记录多少个
    node_matcher = NodeMatcher(graph)
    for q in range(len(arr1)):
        # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
        nodes = list(node_matcher.match("lstools").where("_.tool=~ \'"+arr1[q]+"\' "))
        for i in range(len(nodes)):
            arr2.append(nodes[i]['type'])
            # arr2.append(nodes[i]['id'])
            # arr2.append(nodes[i]['tool'])
            arr2.append(nodes[i]['method'])
    return arr2
def hjchaxun(index):
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]    #将输入每个数以空格键隔开做成数组
    arr2=[]             #记录多少个
    node_matcher = NodeMatcher(graph)
    for q in range(len(arr1)):
        # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
        nodes = list(node_matcher.match("HJQC").where("_.os=~ \'"+arr1[q]+"\' "))
        for i in range(len(nodes)):
            # arr2.append(nodes[i]['os'])
            # arr2.append(nodes[i]['id'])
            arr2.append(nodes[i]['type'])
    return arr2

def hjchaxuns(index):
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]    #将输入每个数以空格键隔开做成数组
    arr2=[]             #记录多少个
    node_matcher = NodeMatcher(graph)
    # for q in range(len(arr)):
    #     # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
    nodes = list(node_matcher.match("HJQC").where("_.type=~ \'"+arr+"\' "))
    for i in range(len(nodes)):
        arr2.append(nodes[i]['os'])
        arr2.append(nodes[i]['id'])
        arr2.append(nodes[i]['type'])
        arr2.append(nodes[i]['func'])


    return arr2
def tq(index):
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]    #将输入每个数以空格键隔开做成数组
    arr2=[]             #记录多少个
    node_matcher = NodeMatcher(graph)
    for q in range(len(arr1)):
        # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
        nodes = list(node_matcher.match("TQ"))
        for i in range(len(nodes)):
            # arr2.append(nodes[i]['type'])
            # arr2.append(nodes[i]['id'])
            arr2.append(nodes[i]['func'])
            # arr2.append(nodes[i]['method'])
    newlist = list(dict.fromkeys(arr2))
    return newlist

def stchaxun(index):
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]    #将输入每个数以空格键隔开做成数组
    arr2=[]             #记录多少个
    node_matcher = NodeMatcher(graph)
    for q in range(len(arr1)):
        # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
        nodes = list(node_matcher.match("shentou").where("_.type=~ \'"+arr1[q]+"\' "))
        for i in range(len(nodes)):
            # arr2.append(nodes[i]['type'])
            # arr2.append(nodes[i]['id'])
            arr2.append(nodes[i]['method'])
    return arr2
def stchaxuns(index):
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]  # 将输入每个数以空格键隔开做成数组
    arr2 = []  # 记录多少个
    node_matcher = NodeMatcher(graph)
    # for q in range(len(arr)):
    #     # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
    nodes = list(node_matcher.match("shentou").where("_.method=~ \'" + arr + "\' "))
    for i in range(len(nodes)):
        # arr2.append(nodes[i]['os'])
        arr2.append(nodes[i]['type'])
        arr2.append(nodes[i]['id'])

        arr2.append(nodes[i]['method'])

    return arr2
def chaxun(index):
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]    #将输入每个数以空格键隔开做成数组
    arr2=[]             #记录多少个
    node_matcher = NodeMatcher(graph)
    for q in range(len(arr1)):
        # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
        nodes = list(node_matcher.match("TOOL").where("_.type=~ \'"+arr1[q]+"\' "))
        for i in range(len(nodes)):
            arr2.append(nodes[i]['type'])
            arr2.append(nodes[i]['id'])
            arr2.append(nodes[i]['tool'])
            arr2.append(nodes[i]['method'])
    # b={}
    # if len(arr2)==0:
    #     nodea = list(node_matcher.match("tool").where("_.score > 0 "))
    #     # nodea = list(node_matcher.match("toolattribute").where("_.score > 0 "))
    #     for i in range(len(nodea)):
    #         b[nodea[i]['name']]=nodea[i]['score']
    # new_order1 = sorted(b.items(), key=lambda x: x[1],reverse =True)
    # new_b = { k : v for k,v in new_order1} #有序列表插入新的字典
    # print(new_b)
    a = {}
    for i in arr2:
        if arr2.count(i)>=1:
            a[i] = arr2.count(i)
    new_order = sorted(a.items(), key=lambda x: x[1],reverse =True)
    new_a = { k : v for k,v in new_order} #有序列表插入新的字典
    # keys = new_a.keys()
    # print(arr1)
    # print(new_a)

    key_value = list(new_a.keys())

    return arr2

@app.route("/api/tool/", methods=["GET"])
def tool():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    #age = get_data.get('age')
    # 对参数进行操作
    #return_dict['result'] = tt(name, age)
    return_dict['result'] = chaxun1(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)
    # return json.dumps("nmap", ensure_ascii=False)
# 功能函数
#def tt(name, age):
#    result_str = "%s今年%s岁" % (name, age)
#    return result_str
def chaxun1(index):
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]    #将输入每个数以空格键隔开做成数组
    arr2=[]             #记录多少个
    node_matcher = NodeMatcher(graph)
    for q in range(len(arr1)):
        # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
        nodes = list(node_matcher.match("TOOL").where("_.tool=~ \'"+arr1[q]+"\' "))
        for i in range(len(nodes)):
            arr2.append(nodes[i]['type'])
            # arr2.append(nodes[i]['id'])
            # arr2.append(nodes[i]['tool'])
            arr2.append(nodes[i]['method'])

    a = {}
    for i in arr2:
        if arr2.count(i)>=1:
            a[i] = arr2.count(i)
    new_order = sorted(a.items(), key=lambda x: x[1],reverse =True)
    new_a = { k : v for k,v in new_order} #有序列表插入新的字典

    key_value = list(new_a.keys())

    return arr2


@app.route("/api/tools/", methods=["GET"])
def tools():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    # age = get_data.get('age')
    # 对参数进行操作
    # return_dict['result'] = tt(name, age)
    return_dict['result'] = chaxun2(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)
    # return json.dumps("nmap", ensure_ascii=False)


# 功能函数
# def tt(name, age):
#    result_str = "%s今年%s岁" % (name, age)
#    return result_str
def chaxun2(index):
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]  # 将输入每个数以空格键隔开做成数组
    arr2 = []  # 记录多少个
    node_matcher = NodeMatcher(graph)
    for q in range(len(arr1)):
        # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
        nodes = list(node_matcher.match("TOOL").where("_.type=~ \'" + arr1[q] + "\' "))
        for i in range(len(nodes)):
            # arr2.append(nodes[i]['type'])
            # arr2.append(nodes[i]['id'])
            arr2.append(nodes[i]['tool'])
            # arr2.append(nodes[i]['method'])

    a = {}
    for i in arr2:
        if arr2.count(i) >= 1:
            a[i] = arr2.count(i)
    new_order = sorted(a.items(), key=lambda x: x[1], reverse=True)
    new_a = {k: v for k, v in new_order}  # 有序列表插入新的字典

    key_value = list(new_a.keys())

    return key_value
@app.route("/api/toolss/", methods=["GET"])
def toolss():
    # 默认返回内容
    return_dict = {'return_code': '200', 'return_info': '处理成功', 'result': False}
    # 判断入参是否为空
    if request.args is None:
        return_dict['return_code'] = '5004'
        return_dict['return_info'] = '请求参数为空'
        return json.dumps(return_dict, ensure_ascii=False)
    # 获取传入的params参数
    get_data = request.args.to_dict()
    name = get_data.get('name')
    # age = get_data.get('age')
    # 对参数进行操作
    # return_dict['result'] = tt(name, age)
    return_dict['result'] = chaxun3(name)
    # return_dict['result'] = ['nmap','12']
    return json.dumps(return_dict, ensure_ascii=False)
    # return json.dumps("nmap", ensure_ascii=False)


# 功能函数
# def tt(name, age):
#    result_str = "%s今年%s岁" % (name, age)
#    return result_str
def chaxun3(index):
    graph = Graph('http://localhost:7474/', auth=("neo4j", "123456"))
    # g = Graph("http://localhost:7474", auth=("neo4j", "123456"))
    # node_matcher = NodeMatcher(graph)
    relationship_matcher = RelationshipMatcher(graph)
    arr = index
    jieba.load_userdict(r"D:\word.txt")
    aa = arr
    cc = jieba.lcut(aa, cut_all=False)
    dd = ' '.join(cc)
    arr1 = [str(n) for n in dd.split()]  # 将输入每个数以空格键隔开做成数组
    arr2 = []  # 记录多少个
    node_matcher = NodeMatcher(graph)
    for q in range(len(arr1)):
        # nodes = list(node_matcher.match("toolattribute").where("_.server=~ \'"+arr1[q]+"\' "))
        nodes = list(node_matcher.match("TOOL").where("_.type=~ \'" + arr1[q] + "\' "))
        for i in range(len(nodes)):
            # arr2.append(nodes[i]['type'])
            # arr2.append(nodes[i]['id'])
            arr2.append(nodes[i]['tool'])
            arr2.append(nodes[i]['method'])

    a = {}
    for i in arr2:
        if arr2.count(i) >= 1:
            a[i] = arr2.count(i)
    new_order = sorted(a.items(), key=lambda x: x[1], reverse=True)
    new_a = {k: v for k, v in new_order}  # 有序列表插入新的字典

    key_value = list(new_a.keys())

    return arr2
@app.after_request
def after(resp):
    resp.headers[' Access-Control-Allow-Origin'] = '*'
    resp.headers[' Access-Control-Allow-Methods'] = 'GET,POST'
    resp.headers[' Access-Control-Allow-Headers'] = 'x-requested-with, content-type'
    return resp



if __name__ == "__main__":
    CORS(app,supports_credentials=True)
    app.run(debug=True)
