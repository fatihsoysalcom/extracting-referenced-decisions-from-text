import re

document_text = """
## Project Alpha Meeting Minutes - 2023-10-26

Attendees: Alice, Bob, Carol

### Discussion Points:
- Review of Q3 performance metrics.
- Proposal for new marketing campaign.

### Key Decisions:

Decision: Proceed with the new marketing campaign targeting Gen Z.
Justification: Market research indicates high potential in this demographic. (Reference: Marketing Report 2023-Q3, Section 4.2)

Decision: Allocate an additional $50,000 to the cloud infrastructure budget.
Justification: To accommodate projected growth in user base and ensure scalability. (Reference: IT Infrastructure Plan v2.0, Appendix A)

Decision: Postpone the launch of Feature X until Q2 2024.
Justification: Requires further testing and integration with legacy systems. (Reference: Development Roadmap 2023-2024, Milestone 3)

### Action Items:
- Alice to draft campaign brief.
- Bob to revise budget proposal.
"""

def extract_decisions_with_references(text):
    # This regex pattern looks for a 'Decision:' line, followed by a 'Justification:' line,
    # which then contains a '(Reference: ...)' tag. This simulates identifying a decision
    # with its context and a verifiable source, as described in the article.
    pattern = re.compile(
        r"Decision:\s*(.*?)\n"  # Capture the decision statement (Group 1)
        r"Justification:\s*(.*?)\s*\(Reference:\s*(.*?)\)", # Capture justification (Group 2) and reference (Group 3)
        re.DOTALL # Allows '.' to match newlines, useful for multi-line justifications if they were present
    )

    decisions = []
    for match in pattern.finditer(text):
        decision_statement = match.group(1).strip() # The core decision extracted
        justification = match.group(2).strip()    # The context/reason for the decision
        reference = match.group(3).strip()        # The verifiable source/reference
        decisions.append({
            "decision": decision_statement,
            "justification": justification,
            "reference": reference
        })
    return decisions

if __name__ == "__main__":
    print("--- Document Analysis: Referenced Decisions ---")
    extracted_data = extract_decisions_with_references(document_text)

    if extracted_data:
        for i, item in enumerate(extracted_data):
            print(f"\nDecision {i+1}:")
            print(f"  Statement: {item['decision']}")
            print(f"  Justification: {item['justification']}")
            print(f"  Reference: {item['reference']}")
    else:
        print("No decisions with verifiable references found in the document.")
