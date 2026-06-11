from ddgs import DDGS


def search_web(query):

    try:

        results = []

        with DDGS() as ddgs:

            search_results = ddgs.text(
                query,
                max_results=5
            )

            for r in search_results:

                results.append(
                    r["body"]
                )

        return "\n".join(results)

    except Exception as e:

        return f"Search failed: {str(e)}"