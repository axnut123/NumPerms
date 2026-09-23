#Haoriwa (C) 2026.
#Using GPL 3.0 license.
#NumPerm main module.
#This is a permission API for software and game.
#Designed for TI-Nspire CX II.
#Uses number to measure a weight of users,
#groups and nodes.
#You can:
#create or remove group, user and node.
#compare weight between group, user and node.
#Allocate or remove node to user,
#check if a user has the required node.

import sys
from ti_system import store_value,recall_value,clear_history,get_key,get_platform

VERSION=(1,1,0)

def version():
  global VERSION
  return VERSION
  
def _cout(string):
  sys.stdout.write("[NP]"+str(string)+"\n")
  
def _quit(code=None):
  _cout("Good bye, NumPerms. Program shutting down.")
  raise SystemExit(code)
  
class Group:
  def __init__(self):pass
  
  @staticmethod
  def exist(name):
    try:check=recall_value("pn_"+str(name))
    except:return False
    if check==0:
      return False
    if check is not None and int(check) !=0:
      return True
    
  @staticmethod
  def Create(name,weight):
    if not name:
      _cout("Group name with weight %s was blank."%(name,str(weight)))
      return -1
    if Group.exist(name) is True:
      _cout("This group name %s was already exist."%(name))
      return -1
    if weight<=0:
      _cout("Group weight cannot be 0. given number was %s."%(str(weight)))
      return -1
    if len(str(name)) > 2:
      _cout("Group name should under 2 letters. given name was %s."%(str(name)))
      return -1
    store_value("pn_"+str(name),1)
    store_value("pn_w_"+str(name),weight)
    _cout("Group %s was successfully created with weight %s."%(str(name),str(weight)))
    return 0
  
  @staticmethod
  def SetWeight(name,weight):
    if weight<=0:
      _cout("Group weight cannot be 0. given number was %s."%(str(weight)))
      return -1
    if Group.exist(name) is False:
      _cout("Group %s does not exist."%(name))
      return -1
    store_value("pn_w_"+str(name),weight)
    _cout("New weight for group %s has set. (%s)"%(name,str(weight)))
    return 0
    
  @staticmethod
  def Remove(name):
    if Group.exist(name) is False:
      _cout("Group %s does not exist."%(name))
      return -1
    store_value("pn_"+str(name),0)
    store_value("pn_w_"+str(name),0)
    _cout("Group %s was successfully deleted."%(str(name)))
    return 0
    
  @staticmethod
  def Compare(name1,name2):
    if Group.exist(name1) is False:
      _cout("Group from first argument does not exist. given: %s."%(name1))
      return -1
    if Group.exist(name2) is False:
      _cout("Group from second argument does not exist. given: %s."%(name2))
      return -1
    a=recall_value("pn_w_"+str(name1))
    b=recall_value("pn_w_"+str(name2))
    if a>b:return 1
    if a<b:return 2
    if a==b:return 3
    return -1
    
class Node:
  def __init__(self):pass
  
  @staticmethod
  def exist(name,group):
    try:check=recall_value("pn_"+str(group)+"_"+str(name))
    except:return False
    if check==0:return False
    if check is not None and check != 0:
      return True
    
  @staticmethod
  def Create(name,fatherGroup,weight):
    if not name:
      _cout("Node name for group %s with weight %s was blank."%(fatherGroup,str(weight)))
      return -1
    if Group.exist(fatherGroup) is False:
      _cout("Given group name '%s' does not exist."%(fatherGroup))
      return -1
    if Node.exist(name,fatherGroup) is True:
      _cout("This node '%s' under the given group '%s' was already exist."%(name,fatherGroup))
      return -1
    if len(str(name))>2:
      _cout("Node name should under 2 letters. given: %s."%(name))
      return -1
    if weight<=0:
      _cout("Node weight should greater than 0. given: %s."%(str(weight)))
      return -1
    store_value("pn_"+str(fatherGroup)+"_"+str(name),weight)
    _cout("Node '%s' under group %s with weight %s was created."%(name,fatherGroup,str(weight)))
    return 0

  @staticmethod
  def Compare(name1,fatherGroup1,name2,fatherGroup2):
    if Node.exist(name1,fatherGroup1) is False:
      _cout("This node under the given group does not exist in first group of given arguments. details: node1: %s, group1: %s."%(name1,fatherGroup1))
      return -1
    if Node.exist(name2,fatherGroup2) is False:
      _cout("This node under the given group does not exist in second group of second given arguments. details: node2: %s, group2: %s."%(name2,fatherGroup2))
      return -1
    a=recall_value("pn_"+str(fatherGroup1)+"_"+str(name1))
    b=recall_value("pn_"+str(fatherGroup2)+"_"+str(name2))
    if a>b:return 1
    if a<b:return 2
    if a==b:return 3
    return -1
    
  @staticmethod
  def GetWeight(name,fatherGroup):
    if Node.exist(name,fatherGroup) is False:
      _cout("This node under the given group does not exist in first group of given arguments. details: node1: %s, group1: %s."%(name,fatherGroup))
      return -1
    return recall_value("pn_"+str(fatherGroup)+"_"+str(name))
    
  @staticmethod
  def Remove(name,fatherGroup):
    if Node.exist(name,fatherGroup) is False:
      _cout("Node %s under group %s does not exist."%(name,fatherGroup))
      return -1
    store_value("pn_"+str(fatherGroup)+"_"+str(name),0)
    _cout("Node %s under group %s was successfully deleted."%(str(name),fatherGroup))
    return 0

  @staticmethod
  def SetWeight(name,fatherGroup,weight):
    if weight<=0:
      _cout("Node weight cannot be 0 or under 0. given number was %s."%(str(weight)))
      return -1
    if Group.exist(fatherGroup) is False:
      _cout("Group %s does not exist."%(fatherGroup))
      return -1
    if Node.exist(name,fatherGroup) is False:
      _cout("Node %s under %s does not exist."%(name,fatherGroup))
      return -1
    store_value("pn_"+str(fatherGroup)+"_"+str(name),int(weight))
    _cout("New weight of %s has set. (%s, under: %s)"%(name,str(weight),fatherGroup))
    return 0
    
class User:
  def __init__(self):pass
  
  @staticmethod
  def exist(name,group):
    try:
      a=recall_value("u_"+str(name)+"_"+str(group))
      b=Group.exist(group)
    except: return False
    if a is None or b is False or a==0:
      return False
    return True
    
  @staticmethod
  def Create(name,fatherGroup,weight):
    if not name:
      _cout("User name for group %s with weight %s was blank."%(fatherGroup,str(weight)))
      return -1
    if User.exist(name,fatherGroup) is True:
      _cout("This user %s under specified group %s was already exist."%(name,fatherGroup))
      return -1
    if Group.exist(fatherGroup) is False:
      _cout("Allocated group name '%s' does not exist."%(fatherGroup))
      return -1
    if weight<=0:
      _cout("User weight cannot be 0 or under 0. given: %s."%(str(weight)))
      return -1
    if len(str(name))>2:
      _cout("User name cannot be longer than 2 characters. given: %s."%(name))
      return -1
    store_value("u_"+str(name)+"_"+str(fatherGroup),1)
    store_value("u_"+str(name)+"_w_"+str(fatherGroup),int(weight))
    _cout("User %s under group %s with weight %s has created."%(name,fatherGroup,str(weight)))
    return 0
    
  @staticmethod
  def AllocateNode(user,fatherGroup,node):
    if Node.exist(node,fatherGroup) is False:
      _cout("Node %s under %s does not exist."%(node,fatherGroup))
      return -1
    if Group.exist(fatherGroup) is False:
      _cout("Group %s does not exist."%(fatherGroup))
      return -1
    if User.exist(user,fatherGroup) is False:
      _cout("User %s from group %s does not exist."%(user,fatherGroup))
      return -1
    store_value("u_"+str(user)+"_"+str(fatherGroup)+"_"+str(node),1)
    _cout("Allocated node %s from group %s to user %s."%(node,fatherGroup,user))
    return 0
  
  @staticmethod
  def RemoveNode(name,fatherGroup,node):
    if Node.exist(node,fatherGroup) is False:
      _cout("Node %s under %s does not exist."%(node,fatherGroup))
      return -1
    if Group.exist(fatherGroup) is False:
      _cout("Group %s does not exist."%(fatherGroup))
      return -1
    if User.exist(name,fatherGroup) is False:
      _cout("User %s under %s does not exist."%(name,fatherGroup))
      return -1
    store_value("u_"+str(name)+"_"+str(fatherGroup)+"_"+str(node),0)
    _cout("Removed node %s from group %s's user %s."%(node,fatherGroup,name))
    return 0
#  
# Discarded function. I am considering to remove or add features on it.
#  @staticmethod
#  def CheckNode(name,fatherGroup,node):
#    if Node.exist(node,fatherGroup) is False:
#      _cout("Node %s under %s does not exist."%(node,fatherGroup))
#      return False
#    if Group.exist(fatherGroup) is False:
#      _cout("Group %s does not exist."%(fatherGroup))
#      return False
#    if User.exist(name,fatherGroup) is False:
#      _cout("User %s under %s does not exist."%(name,fatherGroup))
#      return False
#    try:a=recall_value("u_"+str(name)+"_"+str(fatherGroup)+"_"+str(node))
#    except:return False
#    if a==0 or a==None:return False
#    elif a==1:return True
#    return False
  
  @staticmethod
  def CompareNode(user1,name1,fatherGroup1,user2,name2,fatherGroup2):
    if User.CheckNode(user1,fatherGroup1,name1) is False:
      _cout("This user under the given group or node does not exist in first group of given arguments. details: node1: %s, user1: %s, group1: %s."%(name1,user1,fatherGroup1))
      return -1
    if User.CheckNode(user2,fatherGroup2,name2) is False:
      _cout("This user under the given group or node does not exist in second group of second given arguments. details: node2: %s, user2: %s, group2: %s."%(name2,user2,fatherGroup2))
      return -1
    a = recall_value("pn_"+str(fatherGroup1)+"_"+str(name1))
    b = recall_value("pn_"+str(fatherGroup2)+"_"+str(name2))
    if a>b:return 1
    if a<b:return 2
    if a==b:return 3
    return -1

  @staticmethod
  def CompareUser(user1,fatherGroup1,user2,fatherGroup2):
    if User.exist(user1,fatherGroup1) is False:
      _cout("User %s under %s does not exist."%(user1,fatherGroup1))
      return -1
    if User.exist(user2,fatherGroup2) is False:
      _cout("User %s under %s does not exist."%(user2,fatherGroup2))
      return -1
    a=recall_value("u_"+str(user1)+"_w_"+fatherGroup1)
    b=recall_value("u_"+str(user2)+"_w_"+fatherGroup2)
    if a>b:return 1
    if a<b:return 2
    if a==b:return 3
    return -1
    
  @staticmethod
  def Remove(name,fatherGroup):
    if User.exist(name,fatherGroup) is False:
      _cout("User %s under %s does not exist."%(name,fatherGroup))
      return -1
    store_value("u_"+str(name)+"_"+str(fatherGroup),0)
    store_value("u_"+str(name)+"_w_"+fatherGroup,0)
    _cout("User %s under %s successfully removed."%(str(name),fatherGroup))
    return 0

  @staticmethod
  def SetWeight(name,fatherGroup,weight):
    if weight<=0:
      _cout("User weight cannot be 0 or under 0. given number was %s."%(str(weight)))
      return -1
    if User.exist(name,fatherGroup) is False:
      _cout("User %s under %s does not exist."%(name,fatherGroup))
      return -1
    store_value("u_"+str(name)+"_w_"+fatherGroup,int(weight))
    _cout("New weight for %s under %s set to %s."%(name,fatherGroup,str(weight)))
    return 0
    
def main():
  outputs={0:"+"+"-"*15+"+",
  1:"|   NumPerms 1.1.0    |",
  2:"|   Running on %s         |"%(get_platform())}
  for index in outputs:
    print(outputs.get(index))
  print(outputs.get(0))
  _cout("You are running this library as a program.")
  _cout("In order to use it, please import this file in your program.")
  _cout("There are the list of the APIs:")
  help(User)
  help(Group)
  help(Node)
  _quit(0)

if __name__=="__main__":
  main()
