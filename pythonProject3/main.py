print("Enter algorithm number: \t(1: FIFO, 2: LRU, 3: Optimal)")
algo = input()

print("Enter  number of frames: ")
size = int(input())

print("Enter sequence: ")
myInput = input()

procs = list()
for i in myInput.split(' '):
    procs.append(i)

if algo == '1':
    # apply fifo
    firstIndex = 0
    pageFault = 'No Fault'
    frame = []
    faultsCounter = 0
    alreadyExists = False
    outOfRange = False

    for i in procs:
        if i in frame:
            alreadyExists = True
        else:
            alreadyExists = False

        if alreadyExists:
            pageFault = 'No Fault'
        else:
            if len(frame) < size:
                frame.append(i)
            else:
                frame[firstIndex] = i

                if firstIndex < size - 1:
                    outOfRange = False
                else:
                    outOfRange = True

                if not outOfRange:
                    firstIndex = firstIndex + 1
                else:
                    firstIndex = 0

            faultsCounter = faultsCounter + 1
            pageFault = 'Fault'

        print("   %s\t\t" % i, end='')
        for n in frame:
            print(n, end=' ')
        for n in range(0, size - len(frame), 1):
            print(' ', end=' ')
        print(" %s" % pageFault)
    print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" % (
        len(procs), faultsCounter, (faultsCounter / len(procs)) * 100))

elif algo == '2':
    # apply LRU
    frame = []
    indices = []
    faultsCounter = 0
    pageFault = 'No Fault'
    alreadyExists = False

    for i in procs:
        if i in frame:
            alreadyExists = True
        else:
            alreadyExists = False

        if alreadyExists:
            indices.append(indices.pop(indices.index(frame.index(i))))
            pageFault = 'No Fault'
        else:
            if len(frame) < size:
                frame.append(i)
                indices.append(len(frame) - 1)
            else:
                ind = indices.pop(0)
                frame[ind] = i
                indices.append(ind)
            pageFault = 'Fault'
            faultsCounter = faultsCounter + 1

        print("   %s\t\t" % i, end='')
        for f in frame:
            print(f, end=' ')
        for f in range(0, size - len(frame), 1):
            print(' ', end=' ')
        print(" %s" % pageFault)
    print("\nTotal Requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" % (
    len(procs), faultsCounter, (faultsCounter / len(procs)) * 100))


elif algo == '3':
    # apply optimal
    frame = []
    faultsCounter = 0
    pageFault = 'No Fault'
    alreadyExists = False
    framesFull = False

    procFrequency = [None for i in range(size)]

    for i in range(0, len(procs), 1):

        if procs[i] in frame:
            alreadyExists = True
        else:
            alreadyExists = False

        if alreadyExists:
            pageFault = 'No Fault'
        else:
            if len(frame) < size:
                framesFull = False
            else:
                framesFull = True

            if not framesFull:
                frame.append(procs[i])
            else:
                for x in range(0, len(frame), 1):
                    if frame[x] not in procs[i + 1:]:
                        frame[x] = procs[i]
                        break
                    else:
                        procFrequency[x] = procs[i + 1:].index(frame[x])
                else:
                    frame[procFrequency.index(max(procFrequency))] = procs[i]
            faultsCounter = faultsCounter + 1
            pageFault = 'Fault'

        print("   %s\t\t" % procs[i], end='')
        for x in frame:
            print(x, end=' ')
        for x in range(size - len(frame)):
            print(' ', end=' ')
        print(" %s" % pageFault)
    print("\nTotal requests: %d\nTotal Page Faults: %d\nFault Rate: %0.2f%%" % (
    len(procs), faultsCounter, (faultsCounter / len(procs)) * 100))

