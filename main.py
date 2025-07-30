from utils import load_documents
from summarizer import summarize_documents_parallel
from merger import merge_summaries

def main():
    # Step 1: Load document contents
    documents = load_documents("docs/")  # returns list of strings

    # Step 2: Summarize each document in parallel
    summaries = summarize_documents_parallel(documents)

    # Step 3: Merge summaries into a cohesive overview
    final_summary = merge_summaries(summaries)

    # Step 4: Output the result
    print("\n✅ Final Summary:\n")
    print(final_summary)

if __name__ == "__main__":
    main()
