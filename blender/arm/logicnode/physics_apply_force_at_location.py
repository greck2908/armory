import bpy
from bpy.props import *
from bpy.types import Node, NodeSocket
from arm.logicnode.arm_nodes import *

class ApplyForceAtLocationNode(Node, ArmLogicTreeNode):
    '''Apply force at location node'''
    bl_idname = 'LNApplyForceAtLocationNode'
    bl_label = 'Apply Force At Location'
    bl_icon = 'GAME'

    def init(self, context):
        self.inputs.new('ArmNodeSocketAction', 'In')
        self.inputs.new('ArmNodeSocketObject', 'Object')
        self.inputs.new('NodeSocketVector', 'Force')
        self.inputs.new('NodeSocketVector', 'Location')
        self.outputs.new('ArmNodeSocketAction', 'Out')

add_node(ApplyForceAtLocationNode, category='Physics')
