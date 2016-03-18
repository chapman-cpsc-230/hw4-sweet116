def count_pairs(dna, pair):

    pairs = 0

    i = 0

    while (i < len(dna)):

        index = dna.find(pair, i)

        if (index != -1):

            pairs += 1

            i = index

        i += 1

    print 'there is' , pairs, 'pairs'

count_pairs('agtagggtgata', 'ag')
