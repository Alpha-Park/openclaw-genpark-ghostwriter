import sys, re, math
sys.stdout.reconfigure(encoding='utf-8')

class GhostwriterContentAuditorClient:
    """
    Autonomous SEO readability and content tone auditor.
    Calculates Flesch Reading Ease, Flesch-Kincaid Grade Level,
    Type-Token Ratio (TTR) lexical diversity, and engagement quality scores.
    """
    def __init__(self):
        pass

    def _count_syllables(self, word):
        word = word.lower()
        if len(word) <= 3: return 1
        word = re.sub(r'(?:[^laeiouy]|ed|es|e)$', '', word)
        word = re.sub(r'^y', '', word)
        matches = re.findall(r'[aeiouy]{1,2}', word)
        return max(1, len(matches))

    def evaluate_content(self, text):
        if not text.strip():
            return {"status": "error", "message": "Text is empty"}

        words = re.findall(r'\b[a-zA-Z]+\b', text)
        sentences = [s.strip() for s in re.split(r'[.!?]+', text) if s.strip()]

        total_words = len(words)
        total_sentences = max(1, len(sentences))
        total_syllables = sum(self._count_syllables(w) for w in words)
        unique_words = len(set(w.lower() for w in words))

        asl = total_words / total_sentences # Average Sentence Length
        asw = total_syllables / max(1, total_words) # Average Syllables per Word

        # Flesch Reading Ease: 206.835 - 1.015 * ASL - 84.6 * ASW
        reading_ease = 206.835 - (1.015 * asl) - (84.6 * asw)
        reading_ease = max(0.0, min(100.0, reading_ease))

        # Flesch-Kincaid Grade: 0.39 * ASL + 11.8 * ASW - 15.59
        fk_grade = (0.39 * asl) + (11.8 * asw) - 15.59
        fk_grade = max(1.0, fk_grade)

        # Lexical Diversity (Type-Token Ratio)
        ttr = unique_words / max(1, total_words)

        tone = "HIGHLY_ACCESSIBLE" if reading_ease >= 70 else ("STANDARD_BUSINESS" if reading_ease >= 50 else "TECHNICAL_ACADEMIC")

        return {
            "status": "success",
            "word_count": total_words,
            "sentence_count": total_sentences,
            "flesch_reading_ease": round(reading_ease, 2),
            "grade_level": round(fk_grade, 1),
            "lexical_diversity_ttr": round(ttr, 3),
            "content_tone_profile": tone,
            "is_optimized_for_web": (reading_ease >= 60.0 and ttr >= 0.45)
        }
