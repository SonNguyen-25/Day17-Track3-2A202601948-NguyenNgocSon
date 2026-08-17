# Lab 17 Benchmark Report

- Implementation: `student`
- Kind: `practice`
- Cases: **11**
- Passed: **11/11**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **876.7 ms**
- Average token reduction vs full source context: **15.4%**

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| E01 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| E06 | semantic | PASS | 802.5 | 127 | 72.3% |  |
| E09 | long_term | PASS | 1603.8 | 764 | 0.0% |  |
| E10 | short_term | PASS | 0.3 | 195 | 0.0% |  |
| E02 | long_term | PASS | 1447.9 | 1662 | 0.0% |  |
| E03 | long_term | PASS | 1274.0 | 1669 | 0.0% |  |
| E04 | episodic | PASS | 263.9 | 218 | 1.4% |  |
| E05 | episodic | PASS | 249.4 | 235 | 0.0% |  |
| E07 | mixed | PASS | 1796.2 | 463 | 18.1% |  |
| E11 | semantic | PASS | 411.2 | 126 | 77.7% |  |
| E08 | long_term | PASS | 1794.4 | 1669 | 0.0% |  |

## Evidence excerpts

### E01 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### E06 - semantic

`For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. | {"id":"kb-payment-retry","entity":"Payment API Retry Policy","summary":"For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3.","source":"internal-api-`

### E09 - long_term

`<USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python.  Lan prefers Java and Spring Boot for backend development. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Java + Spring Boot cho backend examples.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va k`

### E10 - short_term

`<SESSION_SUMMARY> user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. | assistant: Acknowledged review constraint. | user: Filler turn 1 about UI spacing. | assistant: Filler answer 1. | user: Filler turn 2 about naming. | assistant: Filler answer 2. | user: Filler turn 3 about logging. | assistant: Filler answer 3. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint: REVIEW-DEADLINE-1600 - project review is Friday at 16:00 and must not be forgotten. - assistant: Acknowledged review constraint. </DURABLE_NOTES> <RECENT_TURNS> user: Filler turn 4 about tests. assistant: Filler answer 4. user: Filler turn 5 about docs. assistant: Filler answe`

### E02 - long_term

`<USER_SUMMARY> The user is managing project ORCHID-27 and working on a benchmark report (LAB-REPORT-1600) due by Friday at 16:00. They are debugging async HTTP issues, specifically identifying connection churn. The current work focus is implementing ASYNC-FIX-20, which involves reusing the aiohttp ClientSession and setting concurrency to 20. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27. The user prefers Python and dislikes Java.  Minh prefers Python and dislikes Java. When explaining code, the user wants short examples. The user wants the explanation of async/await and the differentiation of coroutines`

### E03 - long_term

`<USER_SUMMARY> The user is managing project ORCHID-27 and working on a benchmark report (LAB-REPORT-1600) due by Friday at 16:00. They are debugging async HTTP issues, specifically identifying connection churn. The current work focus is implementing ASYNC-FIX-20, which involves reusing the aiohttp ClientSession and setting concurrency to 20. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27. The user prefers Python and dislikes Java.  Minh prefers Python and dislikes Java. When explaining code, the user wants short examples. The user wants the explanation of async/await and the differentiation of coroutines`

### E04 - episodic

`Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. | TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. | Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. | Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. | Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. | Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la connection churn, khong phai timeout threshold. Ma su co ASYNC-FIX-20. | C`

### E05 - episodic

`Hay kiem tra connection pool, lifecycle cua client va concurrency. | Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. | TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. | Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. | Da ghi nhan trajectory: increase timeout khong hieu qua; ClientSession + concurrency=20 giai quyet connection churn. | Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. | Cach hieu qua la reuse aiohttp ClientSession va dat concurrency=20. Reflection: loi chinh la conne`

### E07 - mixed

`<LONG_TERM> <USER_SUMMARY> The user is managing project ORCHID-27 and working on a benchmark report (LAB-REPORT-1600) due by Friday at 16:00. They are debugging async HTTP issues, specifically identifying connection churn. The current work focus is implementing ASYNC-FIX-20, which involves reusing the aiohttp ClientSession and setting concurrency to 20. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27. The user prefers Python and dislikes Java.  Minh prefers Python and dislikes Java. When explaining code, the user wants short examples. The user wants the explanation of async/await and the differentiation o`

### E11 - semantic

`When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. | {"id":"kb-async-http","entity":"Async HTTP Incident Playbook","summary":"When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST.","source":"incident-playboo`

### E08 - long_term

`<USER_SUMMARY> The user is managing project ORCHID-27 and working on a benchmark report (LAB-REPORT-1600) due by Friday at 16:00. They are debugging async HTTP issues, specifically identifying connection churn. The current work focus is implementing ASYNC-FIX-20, which involves reusing the aiohttp ClientSession and setting concurrency to 20. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27. The user prefers Python and dislikes Java.  Minh prefers Python and dislikes Java. When explaining code, the user wants short examples. The user wants the explanation of async/await and the differentiation of coroutines`
