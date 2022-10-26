class Tests:

    def singleBit(self, bits, validateLen=True):
        if validateLen:
            assert len(bits) == 20_000
        countBit1 = 0
        for bit in bits:
            if bit == 1:
                countBit1 += 1
        assert 9_725 < countBit1 < 10_275

    def series(self, bits, validateLen=True):
        if validateLen:
            assert len(bits) == 20_000
        zerosLengths = [0, 0, 0, 0, 0, 0, 0]
        onesLengths = [0, 0, 0, 0, 0, 0, 0]

        currentContext = bits[0]
        currentLen = 0
        for idx, bit in enumerate(bits):
            if bit == currentContext:
                currentLen += 1
            if bit != currentContext or idx == len(bits) - 1:
                lenToSave = min(currentLen, 6)
                if currentContext == 0:
                    zerosLengths[lenToSave] += 1
                elif currentContext == 1:
                    onesLengths[lenToSave] += 1
                currentContext = bit
                currentLen = 1

        assert 2_315 <= zerosLengths[1] <= 2_685
        assert 1_114 <= zerosLengths[2] <= 1_386
        assert 527 <= zerosLengths[3] <= 723
        assert 240 <= zerosLengths[4] <= 384
        assert 103 <= zerosLengths[5] <= 209
        assert 103 <= zerosLengths[6] <= 209

        assert 2_315 <= onesLengths[1] <= 2_685
        assert 1_114 <= onesLengths[2] <= 1_386
        assert 527 <= onesLengths[3] <= 723
        assert 240 <= onesLengths[4] <= 384
        assert 103 <= onesLengths[5] <= 209
        assert 103 <= onesLengths[6] <= 209

    def longSeries(self, bits, validateLen=True):
        if validateLen:
            assert len(bits) == 20_000

        currentContext = bits[0]
        currentLen = 0
        for idx, bit in enumerate(bits):
            if bit == currentContext:
                currentLen += 1
            elif bit != currentContext:
                currentContext = bit
                currentLen = 1
        assert currentLen < 26

    def poker(self, bits, validateLen=True):
        dict = {}
        if validateLen:
            assert len(bits) == 20_000
        assert len(bits) % 4 == 0

        for idx, bit in enumerate(bits):
            if (idx + 1) % 4 == 0:
                fragment = str(bits[idx - 3:idx + 1])
                currCount = dict.get(fragment, 0)
                dict[fragment] = currCount + 1
        x = (16 / 5000) * sum(pow(n, 2) for n in dict.values()) - 5000
        assert 2.16 < x < 46.17
