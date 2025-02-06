quiz_questions = {
    "0": {
        "question": "What is the name of the paper search agent introduced in this work?",
        "answer": "PaSa",
        "reference": "We introduce PaSa, a novel paper search agent designed to provide comprehensive and accurate results for complex academic queries"
    },
    
    "1": {
        "question": "What are the two main components of the PaSa system?",
        "answer": "The Crawler and the Selector",
        "reference": "PaSa consists of two LLM agents: the Crawler and the Selector"
    },
    
    "2": {
        "question": "How many instances does the AutoScholarQuery training dataset contain?",
        "answer": "33,511 query-paper pairs",
        "reference": "The final AutoScholarQuery dataset comprises 33,551, 1,000, and 1,000 instances in the training, development, and testing splits"
    },
    
    "3": {
        "question": "What is the improvement percentage of PaSa-7b over Google with GPT-4o in Recall@20 on RealScholarQuery?",
        "answer": "37.78%",
        "reference": "PaSa-7b outperforms Google by 37.78%, 39.90%, and 39.83% in recall@20, recall@50 and recall@100, respectively"
    },
    
    "4": {
        "question": "What is the F1 score achieved by the Selector component?",
        "answer": "85%",
        "reference": "The results show that our Selector achieves an F1 score of 85%, outperforming GPT-4o by 5% and Qwen-2.5-7b by 30%"
    },
    
    "5": {
        "question": "Which conferences were used to collect papers for AutoScholarQuery?",
        "answer": "ICLR 2023, ICML 2023, NeurIPS 2023, ACL 2024, and CVPR 2024",
        "reference": "collecting all papers published at ICLR 2023, ICML 2023, NeurIPS 2023, ACL 2024, and CVPR 2024"
    },
    
    "6": {
        "question": "What happens to the Crawler's recall when removing the [Expand] action?",
        "answer": "A decrease of 22.98% on AutoScholarQuery and 32.21% on RealScholarQuery",
        "reference": "removing the [Expand] action from the Crawler leads to a significant drop in the recall: a decrease of 22.98% on AutoScholarQuery and 32.21% on RealScholarQuery"
    },
    
    "7": {
        "question": "How many real-world academic queries are included in RealScholarQuery?",
        "answer": "50 queries",
        "reference": "we constructed RealScholarQuery, a test dataset consisting of 50 real-world research queries"
    },
    
    "8": {
        "question": "What base model was used to develop PaSa-7b?",
        "answer": "Qwen2.5-7b",
        "reference": "We sequentially trained the Selector and Crawler, both based on the Qwen2.5-7b"
    },
    
    "9": {
        "question": "What percentage of queries and papers were qualified in the quality assessment of AutoScholarQuery?",
        "answer": "94.0% of queries were qualified, and among these, 93.7% had relevant papers",
        "reference": "determining that 94.0% of the queries were qualified. Among these qualified queries, 93.7% had corresponding papers that were deemed relevant and appropriate"
    }
}
