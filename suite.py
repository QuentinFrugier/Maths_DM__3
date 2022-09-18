class NotreSuite:
    

    def __init__(self):
        self.current_n = 0
        self.first_terme = 0
        self.values = []
        self.number_of_zero = 0
        self.number_of_one = 0
        self.other = []


    def compute_next(self):
        if self.values:
            self.current_n += 1
            n = self.current_n
            if n%2:
                self.values.append(1-self.values[int((n-1)/2)])
            else:
                self.values.append(self.values[int(n/2)])
        else:
            self.values.append(self.first_terme)


    def get_values(self):
        return self.values

    
    def sort_and_count(self):
        self.number_of_zero = 0
        self.number_of_one = 0
        self.other = []
        for i in self.values:
            if i==1:
                self.number_of_one += 1
            elif i==0:
                self.number_of_zero += 1
            else:
                self.other.append(i)

        return [self.number_of_zero, self.number_of_one, self.other]        
