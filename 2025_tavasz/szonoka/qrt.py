from itertools import combinations

def main():
    #input beolvasás
    with open("rosalind_qrt.txt") as f:
        lines = [line.strip() for line in f if line.strip()]

    taxa = lines[0].split() #taxonok listája
    matrix = lines[1:]  #karaktertábla

    quartets = set()

    for row in matrix:
        ones = [taxa[i] for i, c in enumerate(row) if c == '1']
        zeros = [taxa[i] for i, c in enumerate(row) if c == '0']
        #x-ek ignorálva
        
        if len(ones) >= 2 and len(zeros) >= 2: #2 elem szükséges mindkét oldalt egy kvartethez
            for a1, a2 in combinations(ones, 2):
                for b1, b2 in combinations(zeros, 2): #2-elemű kombinálciók generálása
                    left = tuple(sorted([a1, a2])) #sorting a duplikációk elkerülése érdekében
                    right = tuple(sorted([b1, b2]))
                    quartet = tuple(sorted([left, right])) 
                    quartets.add(quartet)

    #output generálása
    with open("rosalind_qrt_output.txt", "w") as out:
        for (a1, a2), (b1, b2) in sorted(quartets):
            out.write(f"{{{a1}, {a2}}} {{{b1}, {b2}}}\n")

if __name__ == "__main__":
    main()
