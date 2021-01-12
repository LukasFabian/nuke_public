#----------------------------------------------------------------------------------------------------------
#
# AUTOMATICALLY GENERATED FILE TO BE USED BY W_HOTBOX on IBKColor
#
# NAME: create Stack
# 
#----------------------------------------------------------------------------------------------------------

nuke.nodeCopy("%clipboard%")
mainnode = nuke.selectedNode()
linkdarks = str('parent.'+mainnode.name()+'.off')
linklights = str('parent.'+mainnode.name()+'.mult')

nuke.nodePaste("%clipboard%")

currnode=nuke.selectedNode()
k=currnode.knob('multi')
patch=k.getValue()
currnode.knob('off').setExpression(linkdarks)
currnode.knob('mult').setExpression(linklights)

currnode.knob('erode').setValue(0)
if patch==0:
    k.setValue(2)
else:
    k.setValue(patch*2)

nuke.nodeCopy("%clipboard%")

for i in range(0, 7):
    nuke.nodePaste("%clipboard%")
    currnode=nuke.selectedNode()
    k=currnode.knob('multi')
    patch=k.getValue()
    k.setValue(patch*2)
    nuke.nodeCopy("%clipboard%")
