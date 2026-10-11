def chunk_text(
        text: str,
        chunk_size: int = 500,
        overlap: int = 50
        ) -> list[str]:
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")
        if overlap <= 0:
            raise ValueError("overlap must be positive")
        if overlap >= chunk_size:
            raise ValueError("overlap must be less than or equal to chunk_size")
        
        text = text.strip()
            
        if not text:
            return []
        
        chunks = []
        start = 0
        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunk = text[start:end].strip()
            if chunk:
                chunks.append(chunk)
            if end == len(text):
                break
            start = end - overlap
        return chunks