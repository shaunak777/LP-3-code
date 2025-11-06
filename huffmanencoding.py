import heapq

def huffman_encoding(characters, frequencies):
    heap = [[freq, [char, ""]] for char, freq in zip(characters, frequencies)]
    heapq.heapify(heap)

    while len(heap) > 1:
        low1 = heapq.heappop(heap)
        low2 = heapq.heappop(heap)
        for pair in low1[1:]:
            pair[1] = "0" + pair[1]
        for pair in low2[1:]:
            pair[1] = "1" + pair[1]
        heapq.heappush(heap, [low1[0] + low2[0]] + low1[1:] + low2[1:])

    # Final codes
    huffman_codes = sorted(heapq.heappop(heap)[1:], key=lambda p: (len(p[1]), p))
    print("\nHuffman Codes:")
    for char, code in huffman_codes:
        print(char, ":", code)


# ---- Input Section ----
n = int(input("Enter number of characters: "))

chars = []
freqs = []
for i in range(n):
    ch = input(f"Enter character {i+1}: ")
    f = int(input(f"Enter frequency of {ch}: "))
    chars.append(ch)
    freqs.append(f)

# ---- Function Call ----
huffman_encoding(chars, freqs)
