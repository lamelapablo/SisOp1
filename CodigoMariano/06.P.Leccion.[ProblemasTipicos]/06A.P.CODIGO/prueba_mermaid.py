# Creating a simple flowchart diagram
from python_mermaid.diagram import (
    MermaidDiagram,
    Node,
    Link
    
)

import mermaid as md
from mermaid.graph import Graph

# Family members
meg = Node("Meg")
jo = Node("Jo")
beth = Node("Beth")
amy = Node("Amy")
robert = Node("Robert March")

the_march_family = [meg, jo, beth, amy, robert]

# Create links
family_links = [
    Link(robert, meg),
    Link(robert, jo),
    Link(robert, beth),
    Link(robert, amy),
]

chart = MermaidDiagram(
    title="Little Women",
    nodes=the_march_family,
    links=family_links
)

#print(chart)
#* * * * * * * * * * * *  * * * * *  * * * * * * 
sequence = Graph('Sequence-diagram',"""
stateDiagram-v2
    [*] --> Still
    Still --> [*]

    Still --> Moving
    Moving --> Still
    Moving --> Crash
    Crash --> [*]
""")
render = md.Mermaid(sequence)
render # !! note this only works in the notebook that rendered the html.