import heapq

class Node:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_code(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)

        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right

        heapq.heappush(heap, merged)

    root = heap[0]
    codes = {}
    
    def generate_codes(node, current_code):
        if node is not None:
            if node.char is not None:
                codes[node.char] = current_code
            generate_codes(node.left, current_code + "0")
            generate_codes(node.right, current_code + "1")

    generate_codes(root, "")
    return codes


frequencies = {'A': 5, 'B': 9, 'C': 12, 'D': 13, 'E': 16, 'F': 45}
result = huffman_code(frequencies)
print( result)