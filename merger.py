from summarizer import call_llm

def merge_summaries(summaries: list[str]) -> str:
    """Merge multiple summaries into one cohesive final summary"""
    combined_text = "\n\n".join(f"Summary {i+1}:\n{summary}" for i, summary in enumerate(summaries))

    prompt = (
        "You are an expert analyst. Given the summaries below, write a cohesive single summary "
        "that highlights common themes and removes redundancy:\n\n"
        f"{combined_text}"
    )
    return call_llm(prompt)
