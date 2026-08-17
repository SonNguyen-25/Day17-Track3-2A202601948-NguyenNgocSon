# README_submission.md — Lab 17 Multi-Memory Agent

## 3 câu bắt buộc

**1. Layer quan trọng nhất?**
Long-term. 4/11 case phụ thuộc trực tiếp (E02, E03, E08, E09), và đóng góp evidence cho case mixed E07 — nhiều hơn mọi layer khác. Đây cũng là layer duy nhất giữ preference/constraint xuyên suốt nhiều thread (qua Context Block), điều short-term không làm được vì chỉ scope trong 1 thread.

**2. Trade-off Context Block (Zep) vs tự build Redis + Qdrant**
Context Block tự động trích xuất, tổng hợp, cập nhật fact/preference theo thời gian (kể cả recency/conflict), đổi lại là managed service, ít kiểm soát schema/latency, tốn chi phí API. Redis + Qdrant cho toàn quyền kiểm soát dữ liệu, không phụ thuộc bên thứ ba, nhưng phải tự viết logic extract fact, conflict resolution, TTL, semantic search — tốn nhiều công hơn.

**3. Guardrail chống memory poisoning**
`AGENTS.md`: heartbeat không tự cấp quyền hay ghi preference mới vào durable memory mà không qua review (`heartbeat.py --dry-run` chỉ đề xuất ACTION); durable write giữ source/timestamp/confidence; namespace tách theo user (E09: Lan không thấy fact `ORCHID-27` của Minh); `privacy_guard.require_memory_consent` chặn ghi nếu chưa opt-in.

## 4 câu phân tích benchmark

1. **Layer hit rate thấp nhất:** cả 4 layer đều 100% (11/11 PASS). Layer dễ vỡ nhất lúc phát triển là semantic — `scope="auto"` làm mất marker literal (`PAYMENT-RULE-3`, `CONN-POOL-FIRST`), phải đổi sang `scope="episodes"`.
2. **Case retrieve nhiều token nhất:** E02/E03 (long_term) — 824 token, do Context Block trả cả user summary thay vì chỉ đoạn liên quan.
3. **E07 (mixed)** cần long-term (Python là ngôn ngữ ưu tiên của Minh) + semantic (Idempotency-Key trong payment retry rule); evidence bắt buộc: `Python`, `Idempotency-Key`.
4. **Token reduction:** memory-enabled 20.2%, no-memory 81.8%. No-memory giảm token nhiều hơn vì không lấy được gì (hit rate 18.2%). Reduction chỉ có ý nghĩa cùng hit rate — bỏ hết context thì rẻ nhưng sai.

## E08 (recency) và E10 (compaction)

- **E08:** BLUEBIRD-42 là constraint mới hơn; Context Block ưu tiên fact mới theo scope dự án (TypeScript/NestJS) mà không xóa preference Python cũ của ORCHID-27 — đúng rule "recency + scope" trong `MEMORY.md`.
- **E10:** `sliding` nén filler turns thành `SESSION_SUMMARY`, tách `REVIEW-DEADLINE-1600` vào `DURABLE_NOTES`. Giảm `max_recent_messages` xuống 4 loại raw turn deadline khỏi `RECENT_TURNS`, nhưng deadline vẫn sống sót vì đã trích xuất thành durable note từ đầu.
