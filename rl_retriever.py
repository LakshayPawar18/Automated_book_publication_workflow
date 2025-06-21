def rl_search(versions):
    # Correctly pair text with its metadata
    scored = [
        (doc, 2 if meta["role"] == "human" else 1)
        for doc, meta in zip(versions["documents"], versions["metadatas"])
    ]
    scored.sort(key=lambda x: x[1], reverse=True)
    return scored[0][0] if scored else "No versions available"

