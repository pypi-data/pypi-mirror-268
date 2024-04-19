class TextChunker:
    def __init__(self, text, chunk_size, overlap=0):
        """
        Initializes the TextChunker instance.

        Parameters:
            text (str): The text to be chunked.
            chunk_size (int): The length of each text chunk.
            overlap (int): The number of characters that should overlap between consecutive chunks.
        """
        self.text = text
        self.chunk_size = chunk_size
        self.overlap = overlap

    def get_chunks(self):
        """
        Generates the text chunks based on the specified chunk size and overlap.

        Returns:
            list[str]: A list of chunked text segments.
        """
        chunks = []
        start = 0
        while start < len(self.text):
            # Calculate end index of the chunk
            end = start + self.chunk_size
            # Append chunk to the list
            chunks.append(self.text[start:end])
            # Update start index for the next chunk
            start = end - self.overlap if self.overlap < self.chunk_size else start + 1
            # Prevent infinite loop in case overlap is not less than chunk_size
            if self.chunk_size <= self.overlap:
                raise ValueError(
                    "Overlap must be less than chunk size to prevent infinite loops."
                )
        return chunks


class RecursiveCharacterTextSplitter:
    def __init__(self, separators, chunk_size, overlap_size=0, length_function=len):
        self.separators = separators
        self.chunk_size = chunk_size
        self.overlap_size = overlap_size
        self.length_function = length_function

    def split_text(self, text):
        return self._recursive_split(text, 0)

    def _recursive_split(self, text, separator_index):
        if separator_index >= len(self.separators):
            # If no more separators, split into chunks with potential overlap
            return [
                text[i : i + self.chunk_size]
                for i in range(0, len(text), self.chunk_size - self.overlap_size)
            ]

        separator = self.separators[separator_index]
        if self.length_function(text) <= self.chunk_size or not separator:
            # If text is within the limit or there is no valid separator, return as a single chunk
            return [text]

        parts = text.split(separator)
        chunks = []
        current_chunk = ""

        for part in parts:
            if current_chunk:  # Add separator back to all but the first chunk
                part = separator + part

            while self.length_function(part) > self.chunk_size:
                # If part itself is too large, split it using the next level of separator
                if current_chunk:
                    # Save the current chunk if not empty
                    chunks.append(current_chunk)
                    current_chunk = ""
                # Recursively split the oversized part
                more_chunks = self._recursive_split(part, separator_index + 1)
                chunks.extend(more_chunks)
                part = ""  # Clear part as it's been processed

            if self.length_function(current_chunk + part) > self.chunk_size:
                # If adding part to current chunk exceeds size, save current and reset
                chunks.append(current_chunk)
                current_chunk = part
            else:
                # If it fits, append to current chunk
                current_chunk += part

        # Add the last remaining chunk if it exists
        if current_chunk:
            chunks.append(current_chunk)

        return chunks


# Usage example:
length_function = len
splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", ""],  # Logical separators
    chunk_size=1000,
    overlap_size=100,  # 100 characters overlap between chunks
    length_function=length_function,
)
text = "foo bar baz " * 10000
splits = splitter.split_text(text)

# Print the outputs to see the splitting result
for idx, split in enumerate(splits):
    print(f"Chunk {idx+1}: {split[:50]}...")
