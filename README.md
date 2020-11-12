# python-async-io
# Multithreading vs Multiprocessing
* There can only be one thread running at any given time in a python process. 
* Multiprocessing is parallelism. Multithreading is concurrency. 
* Multiprocessing is for increasing speed. Multithreading is for hiding latency. 
* Multiprocessing is best for computations. Multithreading is best for IO. 
* If you have CPU heavy tasks, use multiprocessing with n_process = n_cores and never more. Never! 
* If you have IO heavy tasks, use multithreading with n_threads = m * n_cores with m a number bigger than 1 that you can tweak on your own. Try many values and choose the one with the best speedup because there isn’t a general rule. For instance the default value of m in ThreadPoolExecutor is set to 5 [Source](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) which honestly feels quite random in my opinion.
# Async IO
* Use async IO when you can; use threading when you must.
