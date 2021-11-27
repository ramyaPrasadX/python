from hashlib import sha256

MAX_Nonce = 1000000000


# function for sha256 which is to be used in the mining on our transaction data
def oursha256(text):
    return sha256(text.encode("ascii")).hexdigest()


# defining a mining function
def mining(block_number, transactions, previous_hash, prefix_zeros):
    prefix_str = '0' * prefix_zeros
    # running the loop MAX_Nonce times to check if our generated hash matches the requirement
    for nonce in range(MAX_Nonce):
        text = str(block_number) + transactions + previous_hash + str(nonce)
        new_hash = oursha256(text)
        if new_hash.startswith(prefix_str):
            print("Yo! we did it! we are rich now, we mined a bitcoin!")
            return new_hash
    # exception case when we couldn't figure it out due to our potato PC configs, couldn't run the loop many times
    raise BaseException(f"oops, couldn't mine, still poor AF, we tried for {MAX_Nonce} times tho")





# our main function

if __name__ == '__main__':
    transactions = '''
        maya -> david -> 30,
        vish -> rorry -> 65,
        pod -> pitty -> 20
    
    '''
    # the difficulty is the number of zeros in front of the hash which we wanna check/match
    difficulty = 4
    import time

    start = time.time()
    print("start mining")
    new_hash = mining(5, transactions, '0000000xa036944e29568d0cff17edbe038f81208fecf9a66be9a2b8321c6ec7', difficulty)
    total_time = str((time.time() - start))
    print(f" ending mining, took: {total_time} seconds")
    print(new_hash)
