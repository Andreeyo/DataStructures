class HashMap(object):

    def __init__(self):
        self.hashmap = [[] for _ in range(25)]

    def hash_func(self, key):
        hash_val = len(key) % 256
        for i in key:
            hash_val = self.hashmap[hash_val ^ ord(i)]
        return hash_val

    def insert(self, key, value):
        hash_key = hash(key) % len(self.hashmap)
        key_exists = False
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            bucket[i] = key, value
        else:
            bucket.append((key, value))

    def search(self, key):
        hash_key = hash(key) % len(self.hashmap)
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                return v
            else:
                print('Key does not exist:')

    def delete(self, key):
        hash_key = hash(key) % len(self.hashmap)
        key_exists = False
        bucket = self.hashmap[hash_key]
        for i, kv in enumerate(bucket):
            k, v = kv
            if key == k:
                key_exists = True
                break
        if key_exists:
            del bucket[i]
            print('Key {} deleted'.format(key))
        else:
            print('Key {} not found'.format(key))

    def __getitem__(self, key):
        return self.search(key)


if __name__ == "__main__":

    H = HashMap()
    while True:
        action = input("Action?\n"
                       "Elements inserted must be in the range 25\n"
                       "[1]Insert"
                       "[2]Search"
                       "[3]Delete"
                       "[4]Display HashTable")
        if action not in "1234" or len(action) != 1:
            print("Enter input from 1-4")
            continue
        if action == "1":
            H.insert(key=input("Input key: "), value=input("Enter value: "))
            print("Key and Value added")
        elif action == "2":
            print(H.search(key=input("Enter key to be searched: ")))
            continue
        elif action == "3":
            H.delete(key=input("Enter key to be deleted: "))
            print(H.hashmap)
        elif action == "4":
            print(H.hashmap)