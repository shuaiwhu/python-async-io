# python-async-io
# Async IO
## Async IO Explained
Async IO may at first seem counterintuitive and paradoxical. How does something that facilitates concurrent code use **a single thread** and **a single CPU core**? I’ve never been very good at conjuring up examples, so I’d like to paraphrase one from Miguel Grinberg’s 2017 PyCon talk, which explains everything quite beautifully:

Chess master Judit Polgár hosts a chess exhibition in which she plays multiple amateur players. She has two ways of conducting the exhibition: synchronously and asynchronously.

Assumptions:
* 24 opponents
* Judit makes each chess move in 5 seconds
* Opponents each take 55 seconds to make a move
* Games average 30 pair-moves (60 moves total)

**Synchronous version**: Judit plays one game at a time, never two at the same time, until the game is complete. Each game takes (55 + 5) * 30 == 1800 seconds, or 30 minutes. The entire exhibition takes 24 * 30 == 720 minutes, or 12 hours.

**Asynchronous version**: Judit moves from table to table, making one move at each table. She leaves the table and lets the opponent make their next move during the wait time. One move on all 24 games takes Judit 24 * 5 == 120 seconds, or 2 minutes. The entire exhibition is now cut down to 120 * 30 == 3600 seconds, or just 1 hour. [Source](https://youtu.be/iG6fr81xHKA?t=4m29s)
## Practices
* Use async IO when you can; use threading when you must.

# Multithreading vs Multiprocessing
* There can only be one thread running at any given time in a python process. 
* Multiprocessing is parallelism. Multithreading is concurrency. 
* Multiprocessing is for increasing speed. Multithreading is for hiding latency. 
* Multiprocessing is best for computations. Multithreading is best for IO. 
* If you have CPU heavy tasks, use multiprocessing with n_process = n_cores and never more. Never! 
* If you have IO heavy tasks, use multithreading with n_threads = m * n_cores with m a number bigger than 1 that you can tweak on your own. Try many values and choose the one with the best speedup because there isn’t a general rule. For instance the default value of m in ThreadPoolExecutor is set to 5 [Source](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) which honestly feels quite random in my opinion.
