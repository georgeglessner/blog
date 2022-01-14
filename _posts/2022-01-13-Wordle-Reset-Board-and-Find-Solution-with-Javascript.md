---
layout: post
title: "Wordle Reset Board and Find Solution with Javascript"
tags: 
---


## How to Reset Board
If you are down to your last attempt on the daily [wordle](https://www.powerlanguage.co.uk/wordle/) puzzle and are determined to solve it, you can use the below script to reset the board to give you more chances at guessing. Once you submit your 6th guess, the answer is displayed and the fun is over. This script is best used after you have guessed your 5th word and still don't know what the word may be. 

To execute the script, type `ctrl` + `shift` + `i` in your browser. This should bring up a developer console. Navigate to the tab that says "console". You will be able to paste the following snippet of code there to reset the puzzle board. 

```javascript
let gameState = JSON.parse(localStorage.gameState)
gameState.boardState = Array(6).fill('')
gameState.evaluations = Array(6).fill(null)
gameState.gameStatus = 'IN_PROGRESS'
gameState.rowIndex = 0
localStorage.setItem("gameState", JSON.stringify(gameState))
location.reload()
```

## How to Find Solution Right Away

The code snippet below can be used the same way the above snippet is used in the developer console that will give you the solution to the daily puzzle if you want to increase your statistics. Use at your own discretion!


```javascript
JSON.parse(localStorage.gameState).solution
```
