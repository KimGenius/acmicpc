# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

inputList = []
while(True):
  line = sys.stdin.readline().strip()
  if line == "":
    break
  inputList.append(line)

line = inputList
inputCount = int(line[0])
wordList = []
wordData = {}
for i in range(1, inputCount + 1):
  wordLen = len(line[i])
  if wordLen not in wordData:
    print('없')
    wordData[wordLen] = []
  wordData[wordLen].append(line[i])

print(wordData)
listData = []
for i in range(inputCount + 1, len(line)):
  saveList = {}
  target = line[i]
  targetWordList = target.split()
  for word in targetWordList:
    compareWordList = wordData[len(word)]
    print(compareWord)
    for j in range(0, len(word)):
      saveList[compareWord[j]] = word[j]
    # for char in word:
    #   print(char)
# print(saveList)