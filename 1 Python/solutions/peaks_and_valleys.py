
def peaks(data):
    peaks = []
    indices = list(range(len(data)))

    for i in indices:
        if (i - 1) in indices and (i + 1) in indices:
            if data[i] >= data[i - 1] and data[i] >= data[i + 1]:
                # print(f'{i} is a peak')
                peaks.append(i)
            continue
    return peaks


def valleys(data):
    valleys = []
    indices = list(range(len(data)))

    for i in indices:
        if (i - 1) in indices and (i + 1) in indices:
            if data[i] <= data[i - 1] and data[i] <= data[i + 1]:
                # print(f'{i} is a valley')
                valleys.append(i)
            continue
    return valleys

def peaks_and_valleys(peaks, valleys):
    print(peaks + valleys)



def print_exes(data):
    highest_peak = max(data)

    

def main():
    data = [1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 5, 6, 7, 8, 9, 8, 7, 6, 7, 8, 9]
    list_of_peaks = []
    list_of_valleys  = []
    peaks = peaks(data)
    valleys = valleys(data)
    peaks_and_valleys()
    

main()