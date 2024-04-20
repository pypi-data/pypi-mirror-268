
<h1 align="center">
<b>nicegui-g6</b>
</h1>


A component of AntV [G6](https://github.com/antvis/g6) visualization engine implemented based on [NiceGUI](https://github.com/zauberzeug/nicegui)





## 🔨 Getting Started

To install `nicegui-g6`, run the following command in your terminal:

```bash
pip install nicegui-g6
```

To use `nicegui-g6`, you can simply import the `g6` function and pass the graph data to it. Here's an example:

```python
from nicegui_g6 import g6
from nicegui import ui

# define the graph data
# You can refer to the G6 documentation for more details.
data = {
    "nodes": [
        {
            "id": "node1",
            "x": 100,
            "y": 200,
        },
        {
            "id": "node2",
            "x": 300,
            "y": 200,
        },
    ],
    "edges": [
        {
            "source": "node1",
            "target": "node2",
        },
    ],
}

g6(data)

ui.run()
```
