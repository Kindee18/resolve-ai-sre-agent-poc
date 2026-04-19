.PHONY: loop test help

help:
	@echo "Resolve AI SRE Agent PoC: Closed-Loop Remediation"
	@echo ""
	@echo "Usage:"
	@echo "  make loop     Run the Closed-Loop SRE simulation"
	@echo "  make test     Run unit tests for agent logic"

loop:
	@echo "[START] Starting Resolve Aegis Agent..."
	@python3 agent/sre_agent.py

test:
	@echo "[SETUP] Running logic verification..."
	@python3 -m unittest tests/test_agent.py
