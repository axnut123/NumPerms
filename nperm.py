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
from ti_system import store_value,recall_value,clear_history,get_key

VERSION=(1,0,0)

def version():
  global VERSION
  return VERSION
  
def cout(string):
  sys.stdout.write("[NP]"+str(string)+"\n")
  
class Group:
  def __init__(self):pass
  
  @staticmethod
  def Exists(name):
    try:check=recall_value("pn_"+str(name))
    except:return False
    print(check)
    if check==0:
      return False
    if check is not None or int(check) !=0:
      return True
    
  @staticmethod
  def Create(name,weight):
    if Group.Exists(name) is True:
      cout("This group name was already exists.")
      raise ValueError("This group was already exists.")
    if weight<=0:
      cout("Group weight cannot be 0. given number was %s."%(str(weight)))
      raise ValueError("Weight cannot be under 0. we got %s."%(str(weight)))
    if len(str(name)) > 2:
      cout("Group name should under 2 letters. given name was %s."%(str(name)))
      raise ValueError("Group name should under 2 letters. given name was %s."%str(name))
    store_value("pn_"+str(name),1)
    store_value("pn_w_"+str(name),weight)
    cout("Group %s was successfully created."%(str(name)))
    return 0
  
  @staticmethod
  def SetWeight(name,weight):
    if weight<=0:
      cout("Group weight cannot be 0. given number was %s."%(str(weight)))
      raise ValueError("Weight cannot be under 0. given number was %s."%(str(weight)))
    if Group.Exists(name) is False:
      cout("Group %s does not exists."%(name))
      raise ValueError("Group %s does not exists."%(name))
    store_value("pn_w_"+str(name),weight)
    cout("New weight has set. (%s)"%(str(weight)))
    
  @staticmethod
  def Remove(name):
    if Group.Exists(name) is False:
      cout("Group %s does not exists."%(name))
      return 1
    store_value("pn_"+str(name),0)
    store_value("pn_w_"+str(name),0)
    cout("Group %s was successfully deleted."%(str(name)))
    
  @staticmethod
  def Compare(name1,name2):
    if Group.Exists(name1) is False:
      cout("Group from first argument does not exists. given: %s."%(name1))
      raise ValueError("Group from first argument does not exists. given: %s."%(name1))
      return 1
    if Group.Exists(name2) is False:
      cout("Group from second argument does not exists. given: %s."%(name2))
      raise ValueError("Group from second argument does not exists. given: %s."%(name2))
      return 1
    a=recall_value("pn_w_"+str(name1))
    b=recall_value("pn_w_"+str(name2))
    if a>b:return 1
    if a<b:return 2
    if a==b:return 3
    return -1
class Node:
  def __init__(self):pass
  
  @staticmethod
  def Exists(name,group):
    try:check=recall_value("pn_"+str(group)+"_"+str(name))
    except:return False
    if check==0:return False
    if check is not None or check != 0:
      return True
    
  @staticmethod
  def BuildNode(name,weight,fatherGroup):
    if Group.Exists(fatherGroup) is False:
      cout("Allocated group name '%s' does not exists."%(fatherGroup))
      raise ValueError("Given group '%s' does not exists."%(fatherGroup))
    if Node.Exists(name,fatherGroup) is True:
      cout("This node '%s' under the given group '%s' was already exists."%(name,fatherGroup))
      raise ValueError("This node '%s' under the given group '%s' was already exists."%(name,fatherGroup))
    if len(str(name))>2:
      cout("Node name should under 2 letters. given: %s."%(name))
      raise ValueError("Node name should under 2 letters. given: %s"%(name))
    if weight<=0:
      cout("Node weight should greater than 0. given: %s."%(str(weight)))
      raise ValueError("Node weight cannot be 0 or under 0. given: %s."%(str(weight)))
    store_value("pn_"+str(fatherGroup)+"_"+str(name),weight)
    cout("Node '%s' under group '%s' was created."%(name,fatherGroup))
    return 0

  @staticmethod
  def Compare(name1,fatherGroup1,name2,fatherGroup2):
    if Node.Exists(name1,fatherGroup1) is False:
      cout("This node under the given group does not exists in first group of given arguments. details: node1: %s, group1: %s."%(name1,fatherGroup1))
      raise ValueError("This node under the given group does not exists in first group of given arguments. details: node1: %s, group1: %s."%(name1,fatherGroup1))
    if Node.Exists(name2,fatherGroup2) is False:
      cout("This node under the given group does not exists in second group of second given arguments. details: node2: %s, group2: %s."%(name2,fatherGroup2))
      raise ValueError("This node under the given group does not exists in second group of given arguments. details: node2: %s, group2: %s."%(name2,fatherGroup2))
    a=recall_value("pn_"+str(fatherGroup1)+"_"+str(name1))
    b=recall_value("pn_"+str(fatherGroup2)+"_"+str(name2))
    if a>b:return 1
    if a<b:return 2
    if a==b:return 3
    return -1
    
  @staticmethod
  def GetWeight(name,fatherGroup):
    if Node.Exists(name,fatherGroup) is False:
      cout("This node under the given group does not exists in first group of given arguments. details: node1: %s, group1: %s."%(name,fatherGroup))
      raise ValueError("This node under the given group does not exists in first group of given arguments. details: node1: %s, group1: %s."%(name,fatherGroup))
    return recall_value("pn_"+str(fatherGroup)+"_"+str(name))
    
  @staticmethod
  def Remove(name,fatherGroup):
    if Node.Exists(name,fatherGroup) is False:
      cout("Node %s does not exists."%(name))
      return 1
    store_value("pn_"+str(fatherGroup)+"_"+str(name),0)
    cout("Node %s was successfully deleted."%(str(name)))

class User:
  def __init__(self):pass
  
  @staticmethod
  def Exists(name,group):
    try:
      a=recall_value("u_"+str(name)+"_"+str(group))
      b=Group.Exists(group)
    except: return False
    if a is None or b is False or a==0:
      return False
    return True
    
  @staticmethod
  def Create(name,fatherGroup,weight):
    if User.Exists(name,fatherGroup) is True:
      cout("This user %s under specified group %s was already exists."%(name,fatherGroup))
      raise ValueError("This user %s under specified group %s was already exists."%(name,fatherGroup))
    if Group.Exists(fatherGroup) is False:
      cout("Allocated group name '%s' does not exists."%(fatherGroup))
      raise ValueError("Given group '%s' does not exists."%(fatherGroup))
    if weight<=0:
      cout("User weight cannot be 0 or under 0. given: %s."%(str(weight)))
      raise ValueError("Weight connot be 0 or under 0. given: %s."%(str(weight)))
    if len(str(name))>2:
      cout("User name cannot be larger than 2 digits. given: %s."%(name))
      raise ValueError("User name cannot be larger than 2 digits. given: %s."%(name))
    store_value("u_"+str(name)+"_"+str(fatherGroup),1)
    store_value("u_"+str(name)+"_w_",int(weight))
  
  @staticmethod
  def AllocateNode(user,fatherGroup,node):
    if Node.Exists(node,fatherGroup) is False:
      cout("Node %s does not exists."%(node))
      raise ValueError("Node %s does not exists."%(node))
    if Group.Exists(fatherGroup) is False:
      cout("Group %s does not exists."%(fatherGroup))
      raise ValueError("Group %s does not exists."%(fatherGroup))
    if User.Exists(user,fatherGroup) is False:
      cout("User %s does not exists."%(user))
      raise ValueError("User %s does not exists."%(user))
    store_value("u_"+str(user)+"_"+str(fatherGroup)+"_"+str(node),1)
    cout("Allocated node %s from group %s to user %s."%(node,fatherGroup,user))
    return 0
  
  @staticmethod
  def RemoveNode(name,fatherGroup,node):
    if Node.Exists(node,fatherGroup) is False:
      cout("Node %s does not exists."%(node))
      raise ValueError("Node %s does not exists."%(node))
    if Group.Exists(fatherGroup) is False:
      cout("Group %s does not exists."%(fatherGroup))
      raise ValueError("Group %s does not exists."%(fatherGroup))
    if User.Exists(name,fatherGroup) is False:
      cout("User %s does not exists."%(name))
      raise ValueError("User %s does not exists."%(name))
    store_value("u_"+str(name)+"_"+str(fatherGroup)+"_"+str(node),0)
    cout("Removed node %s from group %s to user %s."%(node,fatherGroup,name))
    return 0
  
  @staticmethod
  def CheckNode(name,fatherGroup,node):
    if Node.Exists(node,fatherGroup) is False:
      cout("Node %s does not exists."%(node))
      raise ValueError("Node %s does not exists."%(node))
    if Group.Exists(fatherGroup) is False:
      cout("Group %s does not exists."%(fatherGroup))
      raise ValueError("Group %s does not exists."%(fatherGroup))
    if User.Exists(name,fatherGroup) is False:
      cout("User %s does not exists."%(name))
      raise ValueError("User %s does not exists."%(name))
    try:a=recall_value("u_"+str(name)+"_"+str(fatherGroup)+"_"+str(node))
    except:return False
    if a==0 or a==None:return False
    elif a==1:return True
    return False
  
  @staticmethod
  def Compare(user1,name1,fatherGroup1,user2,name2,fatherGroup2):
    if User.CheckNode(user1,fatherGroup1,name1) is False:
      cout("This user under the given group or node does not exists in first group of given arguments. details: node1: %s, user1: %s, group1: %s."%(name1,user1,fatherGroup1))
      raise ValueError("This user under the given group or node does not exists in first group of given arguments. details: node1: %s, user1: %s, group1: %s."%(name1,user1,fatherGroup1))
    if User.CheckNode(name2,fatherGroup2,name2) is False:
      cout("This user under the given group or node does not exists in second group of second given arguments. details: node2: %s, user2: %s, group2: %s."%(name2,user2,fatherGroup2))
      raise ValueError("This user under the given group or node does not exists in second group of given arguments. details: node2: %s, user2: %s, group2: %s."%(name2,user2,fatherGroup2))
    a=recall_value("u_"+str(user1)+"_"+str(fatherGroup1)+"_"+str(name1))
    b=recall_value("u_"+str(user2)+"_"+str(fatherGroup2)+"_"+str(name2))
    if a>b:return 1
    if a<b:return 2
    if a==b:return 3
    return -1
  
  @staticmethod
  def Remove(name,fatherGroup):
    if User.Exists(name,fatherGroup) is False:
      cout("User %s does not exists."%(name))
      return 1
    store_value("u_"+str(name)+"_"+str(fatherGroup),0)
    store_value("u_"+str(name)+"_w_",0)
    cout("User %s was successfully deleted."%(str(name)))
