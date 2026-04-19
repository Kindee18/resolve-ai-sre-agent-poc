import unittest
import os
import sys

# Add the agent directory to sys.path
sys.path.append(os.path.join(os.path.dirname(__file__), '../agent'))
import sre_agent

class TestResolveAgent(unittest.TestCase):
    def setUp(self):
        self.agent = sre_agent.ResolveSREAgent()

    def test_closed_loop_resolution(self):
        incident = {"incident_id": "TEST-123", "issue_type": "Connectivity"}
        report = self.agent.execute_closed_loop(incident)
        
        self.assertEqual(report["status"], "RESOLVED")
        self.assertIn("verification", report["workflow"])
        self.assertEqual(report["workflow"]["verification"], "Post-fix health check PASSED")

    def test_escalation_logic(self):
        # We could add a mock here for a failed verification if needed
        pass

if __name__ == '__main__':
    unittest.main()
