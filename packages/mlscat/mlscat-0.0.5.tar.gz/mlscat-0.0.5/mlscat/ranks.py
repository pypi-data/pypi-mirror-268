# re. The Need for Speed: A Fast Guessing Entropy Calculation for Deep Learning-Based SCA
# author: Guilherme Perin, Lichao Wu and Stjepan Picek

import numpy as np


'''
> get mean rank after attack
give the model.prediction nparray to predictions,
we calculate times rank, use number of n_trace attack traces finish rank cal,
if verbose==1:
    plot the rank curve and return mean rank
else:
    return mean rank
'''
def rank(predictions, targets, key:int, times:int, num_trace:int, interval:int, verbose=1):
    # 只写这一次 别的方法直接返回报错就行
    assert type(times) == type(num_trace) == type(interval) == type(verbose) == type(key) == int
    
    predictions = np.log(predictions + 1e-40)
    rank_array = np.zeros(shape=(times, num_trace/interval))
    for i in range(times):
        tmp_rank = np.zeros(num_trace/interval)
        pred = np.zeros(256)
        idx = np.random.randint(predictions[0], size=num_trace)
        for random_index, trace_index in enumerate(idx):
            for key_value in range(256):
                # ergodic every keys prob
                pred[key_value] += predictions[trace_index, targets[trace_index, key_value]]
            
            if random_index % interval == 0:
                ranked = np.argsort(pred)[::-1]
                tmp_rank[i/interval] = list(ranked).index(key)
        rank_array[i] = tmp_rank
    return np.mean(rank_array, axis=0)