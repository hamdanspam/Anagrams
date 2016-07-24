import queue


class BreadthFirstSearch(object):

    def __init__(self):
        self.seen_states = queue.Queue()
        self.word = ""
        self.anagram_list = []

    def get_word(self):
        return self.word

    def set_word(self, word):
        self.word = word

    def get_seen_states(self):
        return self.seen_states

    """Main function of the class, to be called from outside, prints all anagrams afterwards"""
    def get_anagrams(self, word):
        self.set_word(word)
        self.bfs(word)
        print(self.anagram_list)

    def bfs(self, word):
        """Iterative implementation"""
        new_states = self.get_states("")
        for elem in list(new_states): self.seen_states.put(elem) #  new_states.queue if queue
        while not self.seen_states.empty():
            temp = self.seen_states.get()

            for elem in temp:
                self.anagram_list.append(elem)
                self.seen_states.put(self.get_states(elem))


    def get_states(self, state):
        """A new state is defined as being a single letter away from the current state, meaning either replacing current
        (last) character, or adding one."""
        next_letters = self.get_remaining_letters(state)  # returns a list
        out = [] #  out = queue.Queue()  # a queue to be enqueued all together
        seen_states_list = list(self.seen_states.queue)
        for letter in next_letters:
            #out_list =  list(out.queue)
            a = state + letter  # "state" -> "statef"
            if a not in seen_states_list and a not in out and a not in self.anagram_list: # out_list  instead of out, if queue
                out.append(a) #  out.put(a)
        return out

    def get_remaining_letters(self, state):
        if state == '': return self.word

        out = list(self.word)
        for elem in list(state): #  .queue):
            # Why is this thing using a for loop? We need this to take a single state and
            if elem in out:
                del out[out.index(elem)]
        return out

    @staticmethod
    def hash_indices(indices):
        out = ""
        for elem in indices:
            out += "_" + chr(elem + 32)  # the first few ascii characters are ugly
        return out

if __name__ == "__main__":
    breadth = BreadthFirstSearch()
    breadth.get_anagrams("anagram")