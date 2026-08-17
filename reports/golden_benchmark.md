# Lab 17 Golden Set Report

- Implementation: `student`
- Kind: `golden`
- Cases: **20**
- Passed: **20/20**
- Evidence hit rate: **100.0%**
- Average retrieval latency: **1043.0 ms**
- Average token reduction vs full source context: **7.9%**
- Golden bonus: **10/10** (100% required)

| Case | Layer | Pass | Latency ms | Retrieved tokens | Token reduction | Missing / Error |
| --- | --- | --- | ---: | ---: | ---: | --- |
| G01 | short_term | PASS | 0.2 | 227 | 0.0% |  |
| G02 | short_term | PASS | 0.1 | 133 | 0.0% |  |
| G08 | long_term | PASS | 2660.8 | 764 | 0.0% |  |
| G09 | long_term | PASS | 1741.6 | 1696 | 0.0% |  |
| G12 | semantic | PASS | 217.2 | 369 | 19.6% |  |
| G14 | semantic | PASS | 213.0 | 242 | 37.5% |  |
| G15 | semantic | PASS | 358.4 | 242 | 47.3% |  |
| G19 | mixed | PASS | 1950.1 | 581 | 0.0% |  |
| G03 | long_term | PASS | 1874.0 | 1692 | 0.0% |  |
| G04 | long_term | PASS | 1242.5 | 1679 | 0.0% |  |
| G05 | long_term | PASS | 1149.7 | 1666 | 0.0% |  |
| G10 | episodic | PASS | 221.2 | 436 | 0.0% |  |
| G11 | episodic | PASS | 214.8 | 436 | 0.0% |  |
| G13 | semantic | PASS | 211.0 | 368 | 34.9% |  |
| G16 | mixed | PASS | 1834.5 | 581 | 0.0% |  |
| G18 | mixed | PASS | 687.1 | 500 | 11.5% |  |
| G20 | mixed | PASS | 2249.0 | 831 | 0.0% |  |
| G06 | long_term | PASS | 1189.2 | 1688 | 0.0% |  |
| G07 | long_term | PASS | 1350.0 | 1693 | 0.0% |  |
| G17 | mixed | PASS | 1494.8 | 581 | 8.1% |  |

## Evidence excerpts

### G01 - short_term

`<SESSION_SUMMARY> user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. | assistant: Noted standup constraint. | user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. | assistant: Noted staging constraint. | user: Filler A about button padding. | assistant: Filler A. | user: Filler B about color tokens. | assistant: Filler B. | user: Filler C about copy tone. | assistant: Filler C. </SESSION_SUMMARY> <DURABLE_NOTES> - user: Constraint HOLD-ALPHA-0900: standup is 09:00 sharp and must not be forgotten. - assistant: Noted standup constraint. - user: Constraint HOLD-BETA-STAGING: writes go to staging DB only. - assistant: Noted staging constraint. </DURA`

### G02 - short_term

`<RECENT_TURNS> user: Ten du an ca nhan cua toi la ORCHID-27. Toi thich Python va khong thich Java. Khi giai thich code, hay dung vi du ngan. assistant: Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. user: Toi dang hoc async/await va hay nham coroutine voi Task. Neu sau nay gap chu de nay, hay giai thich bang timeline. assistant: Toi se uu tien timeline khi giai thich coroutine va Task. user: TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. </RECENT_TURNS>`

### G08 - long_term

`<USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python.  Lan prefers Java and Spring Boot for backend development. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Lan Tran" }: Toi la Lan. Du an cua toi la LOTUS-88. Toi uu tien Java va Spring Boot, va khong dung Python trong vi du backend.   - Created At: 2026-08-01 11:00:20     Source: message     Content: Lab Assistant (assistant): Da hieu: LOTUS-88, Jav`

### G09 - long_term

`<USER_SUMMARY> The user is managing project ORCHID-27 and working on a benchmark report (LAB-REPORT-1600) due by Friday at 16:00. They are debugging async HTTP issues, specifically identifying connection churn. The current work focus is implementing ASYNC-FIX-20, which involves reusing the aiohttp ClientSession and setting concurrency to 20. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27. The user prefers Python and dislikes Java.  Minh prefers Python and dislikes Java. When explaining code, the user wants short examples. The user wants the explanation of async/await and the differentiation of coroutines`

### G12 - semantic

`Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. | Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. | For POST /payments, every retryable request MUST send the same Idempotency-Key. Retry only HTTP 429 or transient 5xx errors, use exponential-backoff, and stop after max-3-retries. Marker: PAYMENT-RULE-3. | {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A `

### G14 - semantic

`Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. | Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. | {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08- | {"id":"kb-context-budget","entity`

### G15 - semantic

`Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. | Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. | {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL.","source":"memory-governance-policy","updated_at":"2026-08- | {"id":"kb-context-budget","entity`

### G19 - mixed

`<LONG_TERM> <USER_SUMMARY> Lan's project is LOTUS-88. They prioritize Java and Spring Boot for backend development and do not use Python.  Lan prefers Java and Spring Boot for backend development. </USER_SUMMARY>  <EPISODES> Episodes are source message or document excerpts shown in selection order.   - Created At: 2026-08-17 13:52:17     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "Evaluation User" }: Lan uu tien stack backend nao cho LOTUS-88?   - Created At: 2026-08-01 11:00:00     Source: message     Content: [user] {   "user_id": "lan-lab17",   "first_name": "Lan",   "last_name": "Tran",   "user_alias": "La`

### G03 - long_term

`<USER_SUMMARY> The user is managing project ORCHID-27 and working on a benchmark report (LAB-REPORT-1600) due by Friday at 16:00. They are debugging async HTTP issues, specifically identifying connection churn. The current work focus is implementing ASYNC-FIX-20, which involves reusing the aiohttp ClientSession and setting concurrency to 20. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27. The user prefers Python and dislikes Java.  Minh prefers Python and dislikes Java. When explaining code, the user wants short examples. The user wants the explanation of async/await and the differentiation of coroutines`

### G04 - long_term

`<USER_SUMMARY> The user is managing project ORCHID-27 and working on a benchmark report (LAB-REPORT-1600) due by Friday at 16:00. They are debugging async HTTP issues, specifically identifying connection churn. The current work focus is implementing ASYNC-FIX-20, which involves reusing the aiohttp ClientSession and setting concurrency to 20. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27. The user prefers Python and dislikes Java.  Minh prefers Python and dislikes Java. When explaining code, the user wants short examples. The user wants the explanation of async/await and the differentiation of coroutines`

### G05 - long_term

`<USER_SUMMARY> The user is managing project ORCHID-27 and working on a benchmark report (LAB-REPORT-1600) due by Friday at 16:00. They are debugging async HTTP issues, specifically identifying connection churn. The current work focus is implementing ASYNC-FIX-20, which involves reusing the aiohttp ClientSession and setting concurrency to 20. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27. The user prefers Python and dislikes Java.  Minh prefers Python and dislikes Java. When explaining code, the user wants short examples. The user wants the explanation of async/await and the differentiation of coroutines`

### G10 - episodic

`Backend cua BLUEBIRD-42 bat buoc dung stack gi? | Voi demo ca nhan cua Minh, ngon ngu uu tien la gi? | Minh con open loop hay deadline nao chua hoan thanh? | Toi se uu tien timeline khi giai thich coroutine va Task. | Hay kiem tra connection pool, lifecycle cua client va concurrency. | Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. | Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. | Hay chon huong dan code retry payment phu hop voi preference ca nhan cua Minh. | Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. | TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. |`

### G11 - episodic

`Backend cua BLUEBIRD-42 bat buoc dung stack gi? | Voi demo ca nhan cua Minh, ngon ngu uu tien la gi? | Minh con open loop hay deadline nao chua hoan thanh? | Toi se uu tien timeline khi giai thich coroutine va Task. | Hay kiem tra connection pool, lifecycle cua client va concurrency. | Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. | Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. | Hay chon huong dan code retry payment phu hop voi preference ca nhan cua Minh. | Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. | TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REPORT-1600. |`

### G13 - semantic

`Do not persist personal data without explicit opt-in. A deletion request must remove user-scoped memory and be verified across every store. Marker: DELETE-VERIFY-ALL. | Reserve bounded context for memory. This lab uses short-term 10 percent, long-term 4 percent, episodic 3 percent, semantic 3 percent; trim lower-priority memory first. Marker: BUDGET-10-4-3-3. | When async HTTP calls time out, inspect connection pooling, downstream saturation and concurrency before increasing timeout. Reuse a long-lived client session where possible. Marker: CONN-POOL-FIRST. | {"id":"kb-memory-privacy","entity":"Agent Memory Privacy Rule","summary":"Do not persist personal data without explicit opt-in. A dele`

### G16 - mixed

`<LONG_TERM> <USER_SUMMARY> The user is managing project ORCHID-27 and working on a benchmark report (LAB-REPORT-1600) due by Friday at 16:00. They are debugging async HTTP issues, specifically identifying connection churn. The current work focus is implementing ASYNC-FIX-20, which involves reusing the aiohttp ClientSession and setting concurrency to 20. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27. The user prefers Python and dislikes Java.  Minh prefers Python and dislikes Java. When explaining code, the user wants short examples. The user wants the explanation of async/await and the differentiation o`

### G18 - mixed

`<EPISODIC> Backend cua BLUEBIRD-42 bat buoc dung stack gi? | Voi demo ca nhan cua Minh, ngon ngu uu tien la gi? | Minh con open loop hay deadline nao chua hoan thanh? | Toi se uu tien timeline khi giai thich coroutine va Task. | Hay kiem tra connection pool, lifecycle cua client va concurrency. | Da hieu: demo ca nhan ORCHID-27, uu tien Python, tranh Java, vi du ngan. | Hom nay toi debug async HTTP. Toi da thu tang timeout len 60s nhung van fail. | Hay chon huong dan code retry payment phu hop voi preference ca nhan cua Minh. | Da tach scope: BLUEBIRD-42 dung TypeScript/NestJS; ORCHID-27 van uu tien Python. | TODO: hoan thanh benchmark report truoc thu Sau luc 16:00. Day la open loop LAB-REP`

### G20 - mixed

`<LONG_TERM> <USER_SUMMARY> The user is managing project ORCHID-27 and working on a benchmark report (LAB-REPORT-1600) due by Friday at 16:00. They are debugging async HTTP issues, specifically identifying connection churn. The current work focus is implementing ASYNC-FIX-20, which involves reusing the aiohttp ClientSession and setting concurrency to 20. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27. The user prefers Python and dislikes Java.  Minh prefers Python and dislikes Java. When explaining code, the user wants short examples. The user wants the explanation of async/await and the differentiation o`

### G06 - long_term

`<USER_SUMMARY> The user is managing project ORCHID-27 and working on a benchmark report (LAB-REPORT-1600) due by Friday at 16:00. They are debugging async HTTP issues, specifically identifying connection churn. The current work focus is implementing ASYNC-FIX-20, which involves reusing the aiohttp ClientSession and setting concurrency to 20. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27. The user prefers Python and dislikes Java.  Minh prefers Python and dislikes Java. When explaining code, the user wants short examples. The user wants the explanation of async/await and the differentiation of coroutines`

### G07 - long_term

`<USER_SUMMARY> The user is managing project ORCHID-27 and working on a benchmark report (LAB-REPORT-1600) due by Friday at 16:00. They are debugging async HTTP issues, specifically identifying connection churn. The current work focus is implementing ASYNC-FIX-20, which involves reusing the aiohttp ClientSession and setting concurrency to 20. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27. The user prefers Python and dislikes Java.  Minh prefers Python and dislikes Java. When explaining code, the user wants short examples. The user wants the explanation of async/await and the differentiation of coroutines`

### G17 - mixed

`<LONG_TERM> <USER_SUMMARY> The user is managing project ORCHID-27 and working on a benchmark report (LAB-REPORT-1600) due by Friday at 16:00. They are debugging async HTTP issues, specifically identifying connection churn. The current work focus is implementing ASYNC-FIX-20, which involves reusing the aiohttp ClientSession and setting concurrency to 20. For the company project BLUEBIRD-42, the backend must use TypeScript with NestJS. Python is preferred for personal demos like ORCHID-27. The user prefers Python and dislikes Java.  Minh prefers Python and dislikes Java. When explaining code, the user wants short examples. The user wants the explanation of async/await and the differentiation o`
