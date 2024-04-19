# GeoDynamic

## Installation

```bash
pip install --upgrade geodynamic
```

## Using

1. Preparing code `test.py`:

```python
from geodynamic.manim_dynamic import *

class TestScene(GeoDynamic):
    def construct(self):       
        self.loadGeoGebra('test.ggb', style_json_file = 'pandora.json', px_size = [400, 'auto'])    
        self.exportSVG('test.svg')
```

2. Run compilation:

```bash
manim 'test.py' TestScene
```
