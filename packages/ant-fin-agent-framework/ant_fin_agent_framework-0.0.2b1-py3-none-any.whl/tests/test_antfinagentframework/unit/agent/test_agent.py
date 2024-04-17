# !/usr/bin/env python3
# -*- coding:utf-8 -*-
# @Time    : 2024/3/18 15:27
# @Author  : heji
# @Email   : lc299034@antgroup.com
# @FileName: test_agent.py
import unittest

from antfinagentframework.agent.agent import Agent
from antfinagentframework.agent.agent_manager import AgentManager
from antfinagentframework.agent.output_object import OutputObject
from antfinagentframework.base.antfinagentframework import AntFinAgentFramework

AntFinAgentFramework().start(config_path='./config.toml')


class TestAgent(unittest.TestCase):

    def test_rag_agent(self):
        instance: Agent = AgentManager().get_instance_obj('rag_agent')
        output_object: OutputObject = instance.run(input='分析下先锋领航退出中国的原因')
        print(output_object.get_data('output'))


if __name__ == '__main__':
    unittest.main()
