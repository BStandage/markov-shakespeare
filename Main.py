import random
words = []

class Word:
    name = None  # string
    nextw = []  # words that may follow
    nextfreq = []  # parallel frequency table to next

    def __init__(self, name):
        self.name = name
        self.nextw = []
        self.nextfreq = []

    def __str__(self):
        return(self.name  + " - " + str(self.nextw))

def buildbase(filename):
    f = open(filename, 'r')

    text = f.read().split()
    last = None
    for s in text:
        if not any(s == w.name for w in words):
            words.append(Word(s))
        if not last is None:
            if any(s == n for n in last.nextw):
                last.nextfreq[last.nextw.index(s)] += 1
            else:
                last.nextw.append(s)
                last.nextfreq.append(1)
        for i in range(len(words)):
            if words[i].name == s:
                last = words[i]
                break

# w is of type Word
def getNextWord(w):
    candidates = []
    for i in range(len(w.nextw)):
        candidates = candidates + [w.nextw[i]] * w.nextfreq[i]
        nw = candidates[random.randrange(len(candidates))]
    for w in words:
        if w.name == nw:
            return w

def writeSentences(n):
    end = None
    for w in words:
        if w.name == "END":
            end = w
            break
    curr = end
    m_str = ""
    for i in range(10):
        curr = getNextWord(end)
        while not curr == end:
            m_str = m_str + " " + curr.name
            curr = getNextWord(curr)
        m_str = m_str + "<br />"
    print(m_str)




buildbase('sonnets_cleaned.txt')
writeSentences(1)
