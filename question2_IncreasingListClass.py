import sys
import json


class IncreasingList(list):
    def append(self, val):
        if self.__len__() == 0:
            self.extend([val])
        else:
            try:
                while self.__len__() > 0 and self[-1] > val:
                    self.pop()
                self.extend([val])
            except Exception as e:
                print(f"Erros when appendind {val} to IncreasingList: {str(e)} ")
                raise ValueError

    def pop(self):
        if self.__len__() > 0:
            del self[-1]

    def __len__(self):
        element_count = 0
        try:
            for element in self:
                element_count += 1
        except Exception as e:
            print(f"Errors when getting length of IncreasingList {str(e)}")
        return element_count


if __name__ == "__main__":
    ##initialise an increasing list instance
    increasing_list = IncreasingList()

    ##get input : number of queries from user keyboard input value
    number_of_queries = int(input("Number of queries: "))

    ##validate user input number of queries against constraint, throw error if violates the constraint
    if number_of_queries >= 1 and number_of_queries <= 10 ** 5:
        pass
    else:
        print("Provided input number of queries exceeds constraint of 1 to 100000!")
        raise ValueError

    ##get input : class oeprations from user keyboard input value
    operations = json.loads(input("List Operations: "))
    ##validate user input list of operations, throws error if input is not list or doesnt contain at least one "size" operation
    # ["size","append 2","append 4","append 5","size","append 2","size","pop","size"]
    if isinstance(operations, list) and operations.count("size") > 0:
        pass
    else:
        print(
            "Provided input operations is not a List or doenst contain at least one 'size' operation"
        )
        raise ValueError

    ##validate if std input number of operations aligns with number of queries, throw error if not equal
    if len(operations) == number_of_queries:
        pass
    else:
        print(
            f"Length of operations {len(operations)} is not aligned with number of queries {number_of_queries}"
        )

    ##loop through each operation in operations to perform actions on the Increasing List class
    for op in list(operations):
        if op.split(" ")[0] == "size":
            print(increasing_list.__len__())
        elif op.split(" ")[0] == "append":
            if int(op.split(" ")[1]) in range(1, 10 ** 5) and isinstance(
                int(op.split(" ")[1]), int
            ):
                increasing_list.append(int(op.split(" ")[1]))
            else:
                print(
                    "Non integer values provided in append operation or provided integer value exceeds 1 to 10000 constraint!"
                )
        elif op.split(" ")[0] == "pop":
            increasing_list.pop()

