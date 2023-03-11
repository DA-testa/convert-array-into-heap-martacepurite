# python3

def min_h(data,i,n,s):

    smallest=i
    left=2*i+1
    right=2*i+2

    if left < n and data[left] < data[smallest]:
        smallest = left
        
    if right < n and data[right] < data[smallest]:
        smallest = right
        
    if smallest != i:
        data[i], data[smallest] = data[smallest], data[i]
        s.append([i,smallest])
        min_h(data, smallest, n,s)

    return s


def build_heap(data,n):
    swaps = []
    s=[]

    for i in range(n//2, -1, -1):
        swaps=min_h(data, i, n,s)
        
        

    
    return swaps


def main():
    
    text=input()
    text2=input()

    if(text.startswith("F")):
        filename="tests/"+text2
        if(filename.endswith("a")):return

        file=open(filename,"r")
        n=int(file.readline())
        
        data = list(map(int, file.readline().split()))

        assert len(data) == n

        swaps = build_heap(data,n)

        print(len(swaps))

        for i, j in swaps:
            print(i, j)

        file.close()

        

    elif(text.startswith("I")):
        n=int(text2)

        data = list(map(int, input().split()))

        assert len(data) == n

        swaps = build_heap(data,n)

        print(len(swaps))
        
        for i, j in swaps:
            print(i, j)

        
   

if __name__ == "__main__":
    main()