# [START] Resolve AI SRE Agent: Closed-Loop Remediation

## Project Overview
This PoC demonstrates a **Closed-Loop Autonomous SRE Workflow** designed for the "Autonomous SRE" mission at Resolve AI.

The "Resolve-Aegis" agent is a high-confidence orchestrator that doesn't just suggest fixes, but executes them and **verifies the result** before closing the incident, ensuring system integrity and preventing remediation loops.

## [FEATURE] The Edge: Why This Matters for Resolve AI
*   **Closed-Loop Control:** Directly aligns with the core product vision of Resolve AImoving from diagnosis to verified resolution.
*   **Verification-First:** Implements a "Verify-After-Fix" logic to ensure that automated actions actually restored system health.
*   **Production Readiness:** Provides a human-readable audit trail (SRE Report) for every autonomous action taken.

## [STACK] Technical Stack
*   **Language:** Python (Closed-Loop Logic Engine)
*   **Domain:** Site Reliability Engineering (SRE) / Autonomous Operations
*   **Simulation Context:** AWS Boto3 / Terraform Infrastructure
*   **Management:** Makefile

## [START] How It Works
1.  **Diagnosis:** The agent identifies the failure type and root cause.
2.  **Remediation:** The agent executes the fix using infrastructure-as-code or API calls (Boto3).
3.  **Verification:** The agent performs a post-fix health check to verify the system is restored.
4.  **Completion:** The incident is marked as RESOLVED only after a successful verification, otherwise, it is ESCALATED.

## [SETUP] Local Demo
You can simulate the closed-loop SRE workflow locally:
```bash
# Run the Closed-Loop SRE simulation
make loop
```

---
**Built for the Resolve AI Engineering Team by Aegis Agent.**
