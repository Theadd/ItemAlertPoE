#!/usr/bin/env python
# -*- coding: ISO-8859-1 -*-

'''
sku wrote this program. As long as you retain this notice you
can do whatever you want with this stuff. If we meet some day, and you think
this stuff is worth it, you can buy me a beer in return.
'''


import ItemList

def shouldNotify(itemName):
    return True if not _filterItems else itemName in getNotifyItems()
    
def isGemItem(itemName):
    return True if not _filterItems else itemName in getGemItems()
    
def isFlaskItem(itemName):
    return True if not _filterItems else itemName in getFlaskItems()

def getNotifyItems():
    return _notifyItems
    
def getGemItems():
    return _gemItems
    
def getFlaskItems():
    return _flaskItems

# Recommended patch by Rhynocerous.
_notifyItems = []
keywords = ["Map", "Currency"]
for key in ItemList._items:
    if any(x in ItemList._items[key][2] for x in keywords): _notifyItems.append(ItemList._items[key][1])

#python sucks
_gemItems = []
gemwords = ["Gems"]
for key in ItemList._items:
    if any(x in ItemList._items[key][2] for x in gemwords): _gemItems.append(ItemList._items[key][1])
    
#python sucks
_flaskItems = []
flaskwords = ["Flasks"]
for key in ItemList._items:
    if any(x in ItemList._items[key][2] for x in flaskwords): _flaskItems.append(ItemList._items[key][1])

# === SETTINGS ===	

# Set this to True if you want to filter items and only announce
# items that have been added to the _notifyItems list.
# If _filterItems is False, ItemAlertPoE will announce every item drop.
_filterItems = True

# Add items that you wish to announce to this list.
# This list is only considered if _filterItems is set to True.
# If the item name countains a single quote, either escape it
# using \' or use double quotes like in the example below.
#_notifyItems.append("Driftwood Wand")
#_notifyItems.append("Driftwood Club")