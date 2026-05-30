## WATCH THE DEMO HERE

[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/O4KMTpuMK50/0.jpg)](https://youtu.be/O4KMTpuMK50)

## songs_corpus

Consists of Billboard Year End Hot 100 singles of 2025 from Songs_list.csv
songs_corpus stores the lyrics of the songs.

### Query Outputs are stored as log files in LOGS/ folder from q1 to q13.

## QUERIES

- Fetch https://en.wikipedia.org/wiki/Claude_Shannon and tell me his birth date, death date, and three key contributions to information theory.

- Find 3 family-friendly things to do in Tokyo this weekend. Check Saturday's weather forecast there and tell me which one is most appropriate.

- My mom's birthday is 15 May 2026. Remember that and create reminders for two weeks before and on the day.
When is mom's birthday?

- Search for "Python asyncio best practices", read the top 3 results, and give me a short numbered list of the advice they agree on.

- Index the file papers/attention.md and tell me what the three key contributions of the Transformer architecture are according to this paper.

- Run 1: Index every .md file under papers/. Confirm how many chunks were indexed in total.
<br>
    Run 2 (fresh process, persisted state): Across the papers I have indexed, what do they say about chain-of-thought reasoning?

- Across these papers, how do they handle the credit assignment problem?

- Compare how the ReAct paper and the Chain-of-Thought paper differ in their treatment of intermediate reasoning.

- Index the first five files in songs_corpus and return the number of chunks.

- Explain the theme of the song Ordinary by Alex Warren

- Return the artist who has the most songs in the songs_corpus. Each song name startswith artist name.

- Run1: Index billie-eilish-birds-of-a-feather and billie-eilish-wildflower in songs_corpus
<br>
    Run2: Compare the lyrics of billie-eilish-birds-of-a-feather and billie-eilish-wildflower

- Run1: Index doechii-anxiety and doechii-denial-is-a-river .md files in songs_corpus
<br>
    Run2: Which of the songs by doechii is more appropriate for a sad mood and expresses negative emotions?