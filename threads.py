threads = []
for i in range(...):
    t = threading.Thread(target=calculate_sum_square, args=(i))
    t.start()
    # do not join() here
    threads.append(t)

# waiting for all threads to complete before continuing 
for t in threads:
    t.join()


process has the simialr syntax as thread
