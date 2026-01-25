class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        words_freq = {}

        for word in words:
            words_freq[word] = words_freq.get(word, 0) + 1
    
        word_len = len(words[0])
        words_count = len(words)
        total_window_length = word_len * words_count

        result = []

        for big_window_end in range(len(s) - total_window_length + 1):
            seen = {}

            for small_window_end in range(words_count):
                next_word_index = big_window_end + (small_window_end * word_len)
                word = s[next_word_index : next_word_index + word_len]

                if word not in words_freq:
                    break
                
                seen[word] = seen.get(word, 0) + 1

                if seen[word] > words_freq[word]:
                    break

                if small_window_end + 1 == words_count:
                    result.append(big_window_end)

        return result