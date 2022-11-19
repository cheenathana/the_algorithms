class Array:
    def __init__(self):
        self._len = 0
        self._data = {}


    @property
    def len(self):
        return self._len


    @property
    def data(self):
        return self._data


    def __repr__(self):
        return f"Array(length: {self._len}, Data: {self._data})"


    def _outofbound(self, index):
        if index >= self._len:
            raise Exception("Out of Bound")


    def _validate_val(self, val):
        # not elements are there, the the passed in val is first element
        # so no type check is needed
        if not self._len:
            return

        if type(val) != type(self._data[0]):
            raise Exception("Invalid data type")


    def _drestructure(self, index):
        for i in range(index, self._len - 1):
            self._data[i] = self._data[i+1]
        self.pop()


    def _irestructure(self, index, val):
        for i in range(self._len, index, -1):
            self._data[i] = self._data[i-1]
        self._data[index] = val


    def get(self, index):
        self._outofbound(index)
        return data.get(index)


    def push(self, val):
        self._validate_val(val)

        self._data[self._len] = val
        self._len += 1


    def pop(self):
        if not self._len:
            raise Exception("No Elements to pop")

        tmp = self._data[self._len - 1]
        del self._data[self._len - 1]
        self._len -= 1
        return tmp


    def insert(self, index, val):
        self._outofbound(index)
        self._validate_val(val)

        self._irestructure(index, val)
        self._len += 1


    def delete(self, index):
        # checking passed in index value
        self._outofbound(index)

        del self._data[index]

        if index < self._len - 1:
            self._drestructure(index)
        else:
            self._len -= 1
        

