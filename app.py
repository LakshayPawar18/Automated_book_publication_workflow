# === app.py ===
from playwright_scraper import scrape_chapter
from writer import ai_writer
from reviewer import ai_reviewer
from human_loop import human_feedback
from chromadb_store import save_version, retrieve_versions
from rl_retriever import rl_search
from export_pdf import export_to_pdf

url = "https://en.wikisource.org/wiki/The_Gates_of_Morning/Book_1/Chapter_1"
raw_text = scrape_chapter(url)
save_version("original", raw_text)

written = ai_writer(raw_text)
save_version("writer", written)

review = ai_reviewer(written)
print("\nAI Reviewer Feedback:\n", review)

human_edited = human_feedback(written)
save_version("human", human_edited)

print("\nBest version retrieved:")
versions = retrieve_versions()
best = rl_search(versions)
print(best)
export_to_pdf(best, title="Chapter 1 – Final Edited Version")
