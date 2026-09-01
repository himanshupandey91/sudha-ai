class LongTermMemory:
    def __init__(self):
        self.memories = []

    def store(self, experience):
        self.memories.append(experience)

    def recall(self, situation):
        matches = []

        for memory in self.memories:
            if memory["situation"] == situation:
                matches.append(memory)

        return matches

    def all_memories(self):
        return self.memories
