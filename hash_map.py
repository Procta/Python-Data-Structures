class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        # Init empty array
        self.array = [None for item in range(array_size)]

    def hash(self, key, count_collisions=0):
        # Use the sum of bytes in the key as a hash
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code + count_collisions

    def compressor(self, hash_code):
        # Mod the hash to be an index within the array
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compressor(self.hash(key))
        current_array_value = self.array[array_index]

        # If spot in array is empty -> store value
        if current_array_value is None:
            self.array[array_index] = [key, value]
            return

        # If spot in array is taken, but has same key -> update value
        if current_array_value[0] == key:
            self.array[array_index] = [key, value]
            return

        # If spot in array is taken and has different key -> hash collision
        # Use Open Addressing scheme to find next available address
        number_collisions = 1

        while current_array_value[0] != key:
            new_hash_code = self.hash(key, number_collisions)
            new_array_index = self.compressor(new_hash_code)
            current_array_value = self.array[new_array_index]

            if current_array_value is None:
                self.array[new_array_index] = [key, value]
                return

            if current_array_value[0] == key:
                self.array[new_array_index] = [key, value]
                return

            number_collisions += 1

        return

    def retrieve(self, key):
        array_index = self.compressor(self.hash(key))
        possible_return_value = self.array[array_index]

        # If spot in array is empty -> store value
        if possible_return_value is None:
            return None

        # If spot in array is taken, but has same key -> update value
        if possible_return_value[0] == key:
            return possible_return_value[1]

        # If spot in array is taken and has different key -> hash collision
        # Use Open Addressing scheme to find next available address
        retrieval_collisions = 1

        while possible_return_value != key:
            new_hash_code = self.hash(key, retrieval_collisions)
            retrieving_array_index = self.compressor(new_hash_code)
            possible_return_value = self.array[retrieving_array_index]

            if possible_return_value is None:
                return None

            if possible_return_value[0] == key:
                return possible_return_value[1]

            retrieval_collisions += 1

        return


hash_map = HashMap(20)
hash_map.assign('ball', 'basketball')
hash_map.assign('flower', 'daisy')
hash_map.assign('ball', 'soccer')
hash_map.assign('season', 'winter')

print(hash_map.retrieve('ball'))
print(hash_map.retrieve('flower'))
print(hash_map.retrieve('season'))
