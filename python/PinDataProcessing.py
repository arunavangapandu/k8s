class PinDataProcessing:

    def data_process(self, data):
        # data is coming as list of lists
        result = []
       
        for i in range(len(data) - 2):
            #print(i)
            if data[i][1] < 99.0:
                if data[i+1][1] < 99.0 and data[i+2][1] < 99.0:
                    result.append((data[i], data[i+1], data[i+2]))

        if not result:
           print("No 3 consecutive timestamps were found in success rate less than 99.0")
        
        return result

input = [    
                
        ["2025-10-01 10:00", 45.0],
        ["2025-10-01 10:01", 65.0],
        ["2025-10-01 10:02", 100.0],
        ["2025-10-01 10:03", 100.0],
        ["2025-10-01 10:04", 98.0],
    ]
input.sort(key = lambda x:x[0])
#print(input)
result = PinDataProcessing().data_process(input)
print("Result:", result)