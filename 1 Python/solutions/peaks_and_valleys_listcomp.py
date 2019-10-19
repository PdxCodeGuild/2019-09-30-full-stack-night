def peaks(data, indices):
    return [i for i in [i for i in indices if (i - 1) in indices and (i + 1) in indices] if data[i] >= data[i - 1] and data[i] >= data[i + 1]]

def valleys(data, indices):
    return [i for i in [i for i in indices if (i - 1) in indices and (i + 1) in indices] if data[i] <= data[i - 1] and data[i] <= data[i + 1]]

def peaks_and_valleys(peaks, valleys):
    print(peaks + valleys)

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    indices = list(range(len(data)))

    peaks_and_valleys(peaks(data, indices), valleys(data, indices))
    
main()