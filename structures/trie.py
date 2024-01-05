from typing import Dict, List


class TrieNode:
    def __init__(self, character: str | None) -> None:
        self.character = character
        self.children: Dict = {}
        self.is_word = False


class _SoftDelete:
    def _delete(self, current: TrieNode, word: str, phrase: str):
        if current.character:
            phrase += current.character
        if word == phrase:
            current.is_word = False
        for node in current.children.values():
            self._delete(node, word, phrase)


class _HardDelete:
    def _delete(self, current: TrieNode, word: str, phrase: str) -> bool:
        raise NotImplementedError("Hard delete not implemented yet")


class _Trie:
    def __init__(self) -> None:
        self.root = TrieNode(None)

    def insert(self, word: str):
        curr = self.root
        for character in word:
            next_node = curr.children.get(character, None)
            if next_node is None:
                node = TrieNode(character)
                curr.children[character] = node
                curr = node
            else:
                curr = next_node
        curr.is_word = True

    def find(self, phrase: str):
        return self._find(self.root, phrase, "")

    def _find(self, current: TrieNode, phrase: str, current_phrase: str) -> List[str]:
        words = []
        if current.character:
            current_phrase += current.character
        if current_phrase.startswith(phrase) and current.is_word:
            words.append(current_phrase)
        for node in current.children.values():
            words.extend(self._find(node, phrase, current_phrase))
        return words

    def delete(self, word: str):
        self._delete(self.root, word, "")

    def __len__(self) -> int:
        """
        BFS to determine the "length" of the trie (the number of nodes)
        """
        length = 0
        queue = [self.root]
        while queue:
            curr = queue.pop(0)
            if curr.character:
                length += 1
            for node in curr.children.values():
                queue.append(node)
        return length


class TrieSoftDelete(_SoftDelete, _Trie):
    """
    Trie that implements a "soft" delete, where the nodes for deleted words are kept in memory.
    """


class TrieHardDelete(_HardDelete, _Trie):
    """
    Trie that implements a "hard" delete, where the nodes for deleted words are removed.
    """
