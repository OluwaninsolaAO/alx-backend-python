# 0x01. Python - Async

Asynchronous programming is a programming paradigm that enables non-blocking execution of code. Instead of waiting for a particular task to complete before moving on to the next one, asynchronous code can execute multiple tasks concurrently, making efficient use of system resources.

A case study to better explain the concept: Chess master Judit Polgár hosts a chess exhibition in which she plays multiple amateur players. She has two ways of conducting the exhibition: synchronously and asynchronously.

###### Assumptions:

- 24 opponents
- Judit makes each chess move in 5 seconds
- Opponents each take 55 seconds to make a move
- Games average 30 pair-moves (60 moves total)

_Synchronous version_: Judit plays one game at a time, never two at the same time, until the game is complete. Each game takes `(55 + 5) * 30 == 1800 seconds`, or `30 minutes`. The entire exhibition takes `24 * 30 == 720 minutes`, or `12 hours`.

_Asynchronous version_: Judit moves from table to table, making one move at each table. She leaves the table and lets the opponent make their next move during the wait time. One move on all 24 games takes Judit `24 * 5 == 120 seconds`, or `2 minutes`. The entire exhibition is now cut down to `120 * 30 == 3600 seconds`, or just `1 hour`.

There is only one Judit Polgár, who has only two hands and makes only one move at a time by herself. But playing asynchronously cuts the exhibition time down from 12 hours to one. So, cooperative multitasking is a fancy way of saying that a program’s event loop (more on that later) communicates with multiple tasks to let each take turns running at the optimal time.

Async IO takes long waiting periods in which functions would otherwise be blocking and allows other functions to run during that downtime. (A function that blocks effectively forbids others from running from the time that it starts until the time that it returns.)

### Learning Objectives

- `async` and `await` syntax
- How to execute an async program with `asyncio`
- How to run concurrent coroutines
- How to create `asyncio` tasks
- How to use the `random` module
