def query_explainer(state: QueryState):
    result = state['result']
    que = state['que']

    prompt = f"""
    You are a healthcare revenue cycle data analyst.
    I will give you:
    1. A user’s original question.
    2. The query result as a dataframe.

    Your task is to generate a clear spoken-English explanation for a business user. 
    Your response must include:

    1. **Direct Answer**: Short summary of what the data result shows (2–4 sentences).
    2. **Business Insight (Why)**: Add a possible reason based on revenue cycle management logic, guided by the type of question or schema.
    3. **Optional Next Step**: Suggest a practical action in one sentence.

    Rules:
    - Keep it simple and conversational, as if spoken aloud.
    - Do not mention SQL, tables, or column names.
    - If the dataframe is empty, say: "There are no records matching this requirement."
    - Do not exceed 120 words total.
    - Always provide a 'why' explanation if the result is non-empty.

    Schema-driven guidance for insights:
    - If question relates to **Denials** → Talk about payer issues, coding errors, medical necessity, or documentation problems.
    - If about **AR (Accounts Receivable)** → Talk about payment delays, aging buckets, claim rejections, or weak follow-up.
    - If about **Days in AR** → Compare to benchmarks, highlight efficiency or delays in collections.
    - If about **Unbilled AR** → Mention pending coding, missing documentation, or charge entry delays.
    - If about **Charges** → Highlight service mix changes, seasonal volume, or provider workload.
    - If about **Payments** → Mention payer contract terms, reimbursement speed, or patient responsibility.
    - If about **Payer Response** → Discuss response times, approval/denial trends, or payer behavior.
    - If about **Write-offs/Adjustments** → Mention contract adjustments, patient discounts, or denial write-offs.

    User Question:
    {que}

    Query Result (DataFrame):
    {result}

    Now generate the explanation with:
    1. A direct spoken answer.
    2. A possible 'why' reason.
    3. An optional suggested action.
    """
    return prompt
