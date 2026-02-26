"""
Autonomous Trading Ecosystem Evolution Framework (ATEF)
A self-evolving AI ecosystem for autonomous trading strategy research and implementation.
Version: 0.1.0
"""

__version__ = "0.1.0"
__author__ = "ATEF Core Team"

from atef.master_agent import MasterAgent
from atef.research.research_agent import ResearchAgent
from atef.strategy.strategy_developer import StrategyDeveloper
from atef.execution.execution_agent import ExecutionAgent
from atef.risk.risk_manager import RiskManager

__all__ = [
    "MasterAgent",
    "ResearchAgent", 
    "StrategyDeveloper",
    "ExecutionAgent",
    "RiskManager"
]