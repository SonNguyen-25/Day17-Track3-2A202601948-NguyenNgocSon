from __future__ import annotations

from typing import Any

from .config import settings
from .context_budget import ContextBudgetManager
from .utils import cap_query, join_nonempty
from .zep_common import prime_eval_thread, render_graph_search


class StudentMemory:
    """Only this file needs to be edited by students."""

    def __init__(self, client: Any):
        self.client = client
        self.budget = ContextBudgetManager(settings.context_tokens)

    # NOTE: Zep rejects graph.search queries longer than 400 characters. Some
    # eval queries are longer than that, so wrap every query with
    # `cap_query(query)` (see src/utils.py) before passing it to graph.search.

    def retrieve_long_term(self, user_id: str, thread_id: str, query: str) -> str:
        # LAB TODO 1/4
        # 1) prime_eval_thread(...) has already been provided as scaffolding.
        # 2) call thread.get_user_context(thread_id=...)
        # 3) return the .context string.
        # Bonus: append graph.search(scope="edges", limit>=20) facts with
        #        validity ranges (a low limit can miss deadline/open-loop facts).
        prime_eval_thread(self.client, user_id, thread_id, query)
        context = self.client.thread.get_user_context(thread_id=thread_id)
        text = context.context
        # Bonus: Context Block's summary is LLM-generated and can omit sparse
        # facts like a deadline/open-loop time on some calls. Append edge facts
        # (with validity ranges) directly from the graph so those details are
        # retrieved deterministically regardless of summarization variance.
        edges = self.client.graph.search(
            user_id=user_id, query=cap_query(query), scope="edges", limit=30
        )
        edge_text = render_graph_search(edges)
        if edge_text:
            text = f"{text}\n\n{edge_text}"
        return text

    def retrieve_episodic(self, user_id: str, query: str) -> str:
        # LAB TODO 2/4
        # Use client.graph.search(user_id=..., query=cap_query(query),
        #     scope="episodes", limit=...) then render_graph_search(...).
        # Tip: verbose session episodes can crowd out concise, marker-bearing
        # reflections under the tight episodic budget — render_graph_search
        # accepts an `episode_char_cap` to keep more distinct episodes.
        results = self.client.graph.search(
            user_id=user_id,
            query=cap_query(query),
            scope="episodes",
            limit=40,
        )
        # Sort shortest-first: under the tight episodic token budget (mixed
        # cases trim this layer to ~3% of context), verbose session episodes
        # would otherwise crowd out concise, marker-bearing reflections that
        # rank lower in raw relevance order. A compact " | " join (no repeated
        # "EPISODE:" label) squeezes in a few more distinct episodes before
        # the budget's hard character cutoff.
        episodes = sorted(results.episodes or [], key=lambda ep: len(ep.content or ""))
        parts = [(ep.content or "")[:170] for ep in episodes]
        return join_nonempty(parts, sep=" | ")

    def retrieve_semantic(self, graph_id: str, query: str) -> str:
        # LAB TODO 3/4
        # Search the standalone graph (graph_id, NOT user_id).
        # Recommended: scope="episodes" — it returns raw document text that keeps
        # literal markers (e.g. PAYMENT-RULE-3). The "auto" scope returns
        # extracted facts that DROP those literal codes, so avoid it here.
        # Fallback: scope="nodes".
        results = self.client.graph.search(
            graph_id=graph_id,
            query=cap_query(query),
            scope="episodes",
            limit=20,
        )
        # Same shortest-first strategy as retrieve_episodic: each doc is
        # ingested as both a verbose JSON blob and a short text summary
        # (see seed.py add_semantic_documents), and the tight semantic budget
        # can truncate before reaching a doc that ranks lower in raw order.
        # Prioritizing compact entries keeps more distinct markers in-budget.
        docs = sorted(results.episodes or [], key=lambda ep: len(ep.content or ""))
        parts = [(ep.content or "")[:300] for ep in docs]
        return join_nonempty(parts, sep=" | ")

    def assemble_context(self, layers: dict[str, str]) -> tuple[str, dict[str, dict[str, int]]]:
        # LAB TODO 4/4
        # Use ContextBudgetManager to enforce 10/4/3/3 budget and priority order.
        return self.budget.assemble(layers)
