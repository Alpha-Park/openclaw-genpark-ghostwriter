from client import GhostwriterContentAuditorClient
import sys, json
sys.stdout.reconfigure(encoding='utf-8')

def main():
    auditor = GhostwriterContentAuditorClient()
    print("=== GHOSTWRITER CONTENT READABILITY & SEO AUDITOR ===")

    article = (
        "Autonomous AI agents are transforming how modern software systems operate. "
        "By decomposing complex workflows into deterministic functions, developers can build scalable products. "
        "Each agent runs independently and communicates using standardized protocol schemas."
    )

    res = auditor.evaluate_content(article)
    print()
    print(f"Word Count: {res['word_count']} | Sentence Count: {res['sentence_count']}")
    print(f"Reading Ease: {res['flesch_reading_ease']}/100 (Profile: {res['content_tone_profile']})")
    print(f"Flesch-Kincaid Grade: Grade {res['grade_level']}")
    print(f"Lexical Diversity: {res['lexical_diversity_ttr']} (Web Optimized: {res['is_optimized_for_web']})")

if __name__ == "__main__":
    main()
